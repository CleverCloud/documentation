## Git Deployment on Clever Cloud

*You need Git on your computer to deploy via this tool. Here is the official website of Git to get more information: [git-scm.com](https://git-scm.com)*

### Setting up your remotes

1. The "Information" page of your app gives you your Git deployment URL, it looks like this:
   1. `git+ssh://git@push.clever-cloud.com/<your_app_id>.git`
   2. Copy it in your clipboard

2. Locally, under your code folder, type in `git init` to set up a new git repository or skip this step if you already have one

3. Add the deploy URL with `git remote add <name> <your-git-deployment-url>`

4. Add your files via `git add <files path>` and commit them via `git commit -m <your commit message>`

5. Now push your application on Clever Cloud with `git push <name> master`

Refer to [git deployments](/developers/doc/quickstart) for more details.
