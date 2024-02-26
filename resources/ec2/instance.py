from resources.base_resources import BaseAwsResource


class instance(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 terminate-instances --instance-ids"

