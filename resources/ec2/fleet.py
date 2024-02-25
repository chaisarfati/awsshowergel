from resources.base_resources import BaseArn


class fleet(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-fleet --fleet-id"

