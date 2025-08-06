### Push your code

Once you complete these steps, commit your content to the local repository and deploy it:

```bash
git add .
git commit -m "First deploy"
clever deploy
clever open
```

You can display your website's URL or add a custom domain to it (you'll need to configure DNS):

```bash
clever domain
clever domain add your.website.tld
```

### 404 page location

If you need to use a specific page for 404 errors, define its location with `SERVER_ERROR_PAGE_404` environment variable from Static Web Server, used as default in `static` runtime. For example : `SERVER_ERROR_PAGE_404=404.html`.
