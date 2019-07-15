from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_kms as kms,
    aws_sns as sns,
    aws_cloudtrail as cloudtrail,
)


class CdkCloudTrailStack(core.Stack):

    def __init__(self, app: core.App, id: str, *args, **kwargs) -> None:
        super().__init__(app, id, *args, **kwargs)

        key = kms.Key(self, 'CloudTrailKey',
            description='cdk-cloudtrail',
            enable_key_rotation=True,
        )

        bucket = s3.Bucket(self, 'CloudtrailBucket',
            encryption=s3.BucketEncryption.KMS,
            encryption_key=key,
        )

        topic = sns.Topic(self, 'CloudTrailTopic',
            display_name='cdk-cloudtrail',
        )

        #trail = cloudtrail.Trail(self, 'CdkCloudTrail',
        #    trail_name='cdk-cloudtrail',
        #    send_to_cloud_watch_logs=True,
        #    sns_topic=topic.topic_name,
        #    kms_key=key,
        #)
