from resources.base_resources import BaseArn


class elasticip(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 release-address --allocation-id"

