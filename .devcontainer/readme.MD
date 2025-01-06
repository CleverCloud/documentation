Project Documentation
Overview
This project comprises two modular engines, imaginerunner.cpp and codingrabbitai.cpp, designed for dynamic task execution and CI/CD workflow automation. The project also includes a robust setup for Clever Cloud .devcontainer configuration and automation scripts.

Engines
imaginerunner.cpp
Description
A modular engine designed for task execution with a focus on:

Concurrency: Executes tasks in parallel using threads.
Dynamic Configuration: Manages environment configurations dynamically.
API Integration: Supports authenticated API requests with OAuth via libcurl.
Key Features
Task Management: Modular tasks with error handling, executed in parallel.
Environment Handling: Dynamically loads and manages variables from configuration files.
API Requests: Authenticated interactions with external services.
Error Handling: Ensures robust execution with detailed logging.
codingrabbitai.cpp
Description
An automation engine focused on RabbitProtocol CI/CD workflows with capabilities such as:

Building modular components.
Running tests.
Deploying to external systems like Azure.
Key Features
CI/CD Automation: Encapsulates build, test, and deploy workflows.
Environment Integration: Dynamically loads .env files for flexible configurations.
Task Modularization: Pre-defined, reusable tasks (e.g., building with gcc, deploying to Azure).
Detailed Logging: Logs command execution and errors for troubleshooting.
Comparison of Core Features
Feature	imaginerunner.cpp	codingrabbitai.cpp
Task Management	Modular tasks with parallel execution.	Encapsulates CI/CD steps.
Environment Handling	Dynamic file-based variable management.	Manages .env files dynamically.
API Integration	OAuth via libcurl.	No explicit API integration.
Concurrency	Parallel task execution with threads.	Sequential execution.
Error Handling	Exception-safe task execution.	Logs errors for task/command failures.
Build & Deployment	Generic task execution logic.	Pre-defined CI/CD workflows.
Strengths
imaginerunner.cpp
Concurrency: Efficient parallel task execution with thread management.
API Integration: Modular OAuth interactions with external services.
Dynamic Configuration: Flexible environment variable handling.
Error Resilience: Robust handling with detailed logs.
codingrabbitai.cpp
Automation Focus: Comprehensive CI/CD workflow automation.
Modular Tasks: Reusable and pre-defined for common CI/CD steps.
Environment Integration: Seamless .env file handling.
Detailed Logging: Comprehensive logs for debugging.
Areas for Improvement
imaginerunner.cpp
Task Dependencies: Add support for task dependencies to improve workflow coordination.
CI/CD Support: Introduce specific modules for builds and deployments.
Task State Management: Implement status tracking for tasks (e.g., success, failure).
codingrabbitai.cpp
Concurrency: Introduce parallel execution for independent tasks.
Error Handling: Add retries for transient failures (e.g., network issues).
API Integration: Include modular API handlers like in imaginerunner.cpp.
Code Organization: Refactor repetitive logic into reusable utilities.
Potential Enhancements
Merge Engine Strengths:

Combine imaginerunner.cpp’s API integration and concurrency features with codingrabbitai.cpp’s CI/CD focus.
Unified Scheduler:

Develop a task scheduler capable of handling both parallel and sequential tasks with dependency resolution.
Dynamic Task Loading:

Enable dynamic task configuration via JSON or YAML files for flexibility.
Enhanced Logging:

Include timestamps, task statuses, and execution summaries in logs.
Cross-Platform Support:

Ensure compatibility across Linux, macOS, and Windows.
Improved Error Handling:

Add categorized handling for specific errors (e.g., network or command failures).
Clever Cloud .devcontainer Configuration
Description
The Clever Cloud .devcontainer setup defines consistent development environments for Ubuntu 24.04 and Windows Server 2025.

Files to Include
Dockerfile.ubuntu
Dockerfile
Copy code
FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    git \
    cmake \
    clang \
    && apt-get clean

COPY clangfile.ubuntu.json /workspace/
WORKDIR /workspace
Dockerfile.windows
Dockerfile
Copy code
FROM mcr.microsoft.com/windows/server:ltsc2025

SHELL ["cmd", "/S", "/C"]

RUN powershell -Command \
    "Install-PackageProvider -Name NuGet -Force; \
    Install-Module -Name DockerMsftProvider -Repository PSGallery -Force; \
    Install-Package -Name docker -ProviderName DockerMsftProvider -Force"

COPY clangfile.windows.json C:/workspace/
WORKDIR C:/workspace
.devcontainer.json
json
Copy code
{
  "name": "Clever Cloud Dev Environment",
  "context": "..",
  "dockerComposeFile": [
    "./docker-compose.yml"
  ],
  "service": "ubuntu",
  "workspaceFolder": "/workspace",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.cpptools",
        "ms-azuretools.vscode-docker"
      ]
    }
  }
}
docker-compose.yml
yaml
Copy code
version: '3.8'

services:
  ubuntu:
    build:
      context: .
      dockerfile: Dockerfile.ubuntu
    volumes:
      - .:/workspace
    network_mode: none
    command: sleep infinity

  windows:
    build:
      context: .
      dockerfile: Dockerfile.windows
    volumes:
      - .:/workspace
    network_mode: none
    command: cmd /c "ping -t localhost"
Clang Configuration Files
clangfile.ubuntu.json

json
Copy code
{
  "compiler": "clang-14",
  "flags": ["-Wall", "-Wextra"],
  "includes": ["/usr/include", "/usr/local/include"]
}
clangfile.windows.json

json
Copy code
{
  "compiler": "clang-cl",
  "flags": ["/Wall"],
  "includes": ["C:/Program Files (x86)/Windows Kits/10/Include"]
}
Benefits of This Setup
Reproducible Development Environment:

Consistent environments across systems for Ubuntu and Windows.
Clever Cloud Integration:

Seamless deployment and container management.
Scalable Setup:

Easily extendable to new OS configurations or tools.
