from resources.base_resources import BaseAwsResource


class alarm(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "cloudwatch delete-alarms --alarm-names"

