#!/usr/bin/env bash
#-------------------------------------------------------------------------------------------------------------
# CMake Installation Script with Enhanced Logging and Retry Mechanism
#-------------------------------------------------------------------------------------------------------------
set -e

CMAKE_VERSION=${1:-"none"}

if [ "${CMAKE_VERSION}" = "none" ]; then
    echo "No CMake version specified, skipping CMake reinstallation."
    exit 0
fi

cleanup() {
    EXIT_CODE=$?
    set +e
    if [[ -n "${TMP_DIR}" ]]; then
        echo "Executing cleanup of temporary files..."
        rm -Rf "${TMP_DIR}"
    fi
    exit $EXIT_CODE
}
trap cleanup EXIT

echo "Installing CMake version ${CMAKE_VERSION}..."
apt-get -y purge --auto-remove cmake || echo "No existing CMake installation found to purge."
mkdir -p /opt/cmake

architecture=$(dpkg --print-architecture)
case "${architecture}" in
    arm64) ARCH=aarch64 ;;
    amd64) ARCH=x86_64 ;;
    *) echo "Unsupported architecture: ${architecture}." && exit 1 ;;
esac

CMAKE_BINARY_NAME="cmake-${CMAKE_VERSION}-linux-${ARCH}.sh"
CMAKE_CHECKSUM_NAME="cmake-${CMAKE_VERSION}-SHA-256.txt"
TMP_DIR=$(mktemp -d -t cmake-XXXXXXXXXX)

echo "Temporary directory: ${TMP_DIR}"
cd "${TMP_DIR}"

echo "Downloading CMake binary..."
curl --retry 3 --retry-connrefused -sSL "https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/${CMAKE_BINARY_NAME}" -O
curl --retry 3 --retry-connrefused -sSL "https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/${CMAKE_CHECKSUM_NAME}" -O

echo "Verifying checksum..."
if ! sha256sum -c --ignore-missing "${CMAKE_CHECKSUM_NAME}"; then
    echo "Checksum verification failed. Aborting installation."
    exit 1
fi

echo "Installing CMake..."
sh "${TMP_DIR}/${CMAKE_BINARY_NAME}" --prefix=/opt/cmake --skip-license

ln -sf /opt/cmake/bin/cmake /usr/local/bin/cmake
ln -sf /opt/cmake/bin/ctest /usr/local/bin/ctest

echo "CMake ${CMAKE_VERSION} installed successfully."

#!/bin/bash
#-------------------------------------------------------------------------------------------------------------
# Script to Build and Run Runner Images for Ubuntu 24.04 and Windows Server 2025 with Clang
#-------------------------------------------------------------------------------------------------------------

# Variables
UBUNTU_IMAGE_NAME="runner-images-ubuntu-24.04"
WINDOWS_IMAGE_NAME="runner-images-windows-2025"
CONTAINER_NAME="runner-images-container"
UBUNTU_DOCKERFILE_PATH="./Dockerfile.ubuntu"
WINDOWS_DOCKERFILE_PATH="./Dockerfile.windows"
CONTEXT_DIR="."
WORKSPACE_DIR="$(pwd)"
UBUNTU_CLANGFILE_PATH="clangfile.ubuntu.json"
WINDOWS_CLANGFILE_PATH="clangfile.windows.json"
LOG_FILE="runner-images-build.log"
PARALLEL_MODE=false

# Functions

# Cleanup Function
cleanup() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Cleaning up any existing container with the same name..."
    docker rm -f ${CONTAINER_NAME} &>/dev/null && echo "Container ${CONTAINER_NAME} removed." || echo "No container to remove."
}

# Build Image Function
build_image() {
    local image_name="$1"
    local dockerfile_path="$2"
    local clangfile_path="$3"

    if [ ! -f "${dockerfile_path}" ]; then
        echo "[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: Dockerfile not found at ${dockerfile_path}. Aborting."
        exit 1
    fi

    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Building Docker image: ${image_name}..."
    docker build -t ${image_name} -f ${dockerfile_path} --build-arg CLANGFILE=${clangfile_path} ${CONTEXT_DIR} | tee -a ${LOG_FILE}
}

# Run Container Function
run_container() {
    local image_name="$1"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Running Docker container: ${CONTAINER_NAME} for ${image_name}..."
    docker run -it --rm \
        --name ${CONTAINER_NAME} \
        --mount type=bind,source=${WORKSPACE_DIR},target=/workspace \
        --network none \
        ${image_name}
}

# Parallel Execution Wrapper
parallel_execution() {
    local ubuntu_job=$(build_image ${UBUNTU_IMAGE_NAME} ${UBUNTU_DOCKERFILE_PATH} ${UBUNTU_CLANGFILE_PATH} &)
    local windows_job=$(build_image ${WINDOWS_IMAGE_NAME} ${WINDOWS_DOCKERFILE_PATH} ${WINDOWS_CLANGFILE_PATH} &)
    wait $ubuntu_job $windows_job
}

# Main Execution Workflow
echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting Runner Image Setup for Ubuntu and Windows with Clang configurations..."
cleanup

if $PARALLEL_MODE; then
    echo "Running in parallel mode..."
    parallel_execution
else
    build_image ${UBUNTU_IMAGE_NAME} ${UBUNTU_DOCKERFILE_PATH} ${UBUNTU_CLANGFILE_PATH}
    run_container ${UBUNTU_IMAGE_NAME}

    build_image ${WINDOWS_IMAGE_NAME} ${WINDOWS_DOCKERFILE_PATH} ${WINDOWS_CLANGFILE_PATH}
    run_container ${WINDOWS_IMAGE_NAME}
fi

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Runner Image Setup completed successfully."
