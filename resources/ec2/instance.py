from resources.base_resources import BaseArn


class instance(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 terminate-instances --instance-ids"

