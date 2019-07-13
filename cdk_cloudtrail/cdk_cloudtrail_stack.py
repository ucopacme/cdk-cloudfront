from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_cloudtrail as cloudtrail,
)


class CdkCloudTrailStack(core.Stack):

    def __init__(self, app: core.App, id: str, *args, **kwargs) -> None:
        super().__init__(app, id, *args, **kwargs)
        bucket = s3.Bucket(self, 'CloudtrailBucket', encryption=s3.BucketEncryption.KMS)
        trail = cloudtrail.Trail(self, 'CdkCloudTrail',
            trail_name='cdk-cloudtrail',
            send_to_cloud_watch_logs=True,
        )
