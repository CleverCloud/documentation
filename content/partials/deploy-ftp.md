## FTP Deployment

Make sure you have [Filezilla](https://filezilla-project.org/) or an other FTP software installed in your machine.

When you have chosen to deploy your application via FTP at the application creation, a free [FS Bucket]({{< ref "doc/deploy/addon/fs-bucket.md" >}}) has been created with an ID matching your application's ID.

You will find the FTP credentials in the configuration tab of this particular FS Bucket.

Just follow the instructions of your FTP Software to send code to Clever Cloud.

{{< alert "warning" "Warning" >}}
<p>An FTP application is automatically started once the application is created, even if no code has been sent.</p>
{{< /alert >}}

Refer to  our [Quick Start - FTP deployment]({{< ref "doc/getting-started/quickstart.html#ftp-deployment" >}}) for more details.
