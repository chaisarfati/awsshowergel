<p align="center">
    <img alt="awsweeper" src="https://github.com/chaisarfati/awsshowergel/blob/master/img/logo.png" height="150" />
    <h2 align="center">awsshowergel</h2>
    <p align="center">awsshowergel is a command-line tool for managing AWS resources with ease and simplicity.</p>

</p>


## How to Download

You can download the latest version of awsshowergel using curl:

```bash
curl -LO https://github.com/chaisarfati/awsshowergel/releases/latest/download/awsshowergel
```

## How to Use
Once downloaded, you can run awsshowergel directly from the command line. 
Here's are some basic usage examples:

_This command will list you all the resources tagged [Environment=Development, Team=SRE] but will not delete anything 
(due to the --dry-run option)_ 
```bash
./awsshowergel --dry-run --tag-filters Environment=Development --tag-filters Team=SRE
```

_This command will delete all the resources tagged [Environment=Development, Team=SRE]_
```bash
./awsshowergel --tag-filters Environment=Development --tag-filters Team=SRE
```

_This command will delete all the resources tagged [Env=Stagging] but among the cloudfront:distribution and ec2:instance 
resources it will only delete those whose id match the patterns dist-stag* and i-04* respectively_
```bash
./awsshowergel --tag-filters Env=Stagging --id-filters cloudfront:distribution=dist-stag* --id-filters ec2:instance=i-04*
```

_Delete only the resources cloudfront:distribution and ec2:instance tagged [Env=Stagging] and id matching patterns dist-stag* and i-04* respectively_ 
```bash
./awsshowergel --tag-filters Env=Stagging --id-filters cloudfront:distribution=dist-stag* --id-filters ec2:instance=i-04* 
--only-delete-filtered-ids
```

_Delete only the s3 buckets and sqs queues tagged [Env=Stagging] and id matching patterns bucket-stag* and queue-stag* respectively_ 

```bash
./awsshowergel --auto-approve --tag-filters Env=Stagging --id-filters s3:s3=bucket-stag* --id-filters sqs:sqs=queue-stag* 
--only-delete-filtered-ids
```

For more information on how to use awsshowergel, refer to the documentation or run awsshowergel --help.

## Contributing
If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on GitHub.

## Disclaimer
Be **extremely careful** when using this tool. 
**Always run it with the --dry-run option first** to have an idea of what you will delete.
You are using this tool at your own risk! **I am not responsible for any critical deletion performed by this tool**.

