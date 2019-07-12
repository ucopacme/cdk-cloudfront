from aws_cdk import (
    cdk
)


class CdkCloudTrailStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
