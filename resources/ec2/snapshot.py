from resources.base_resources import BaseArn


class snapshot(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-snapshot --snapshot-id"

