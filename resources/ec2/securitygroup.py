from resources.base_resources import BaseArn


class securitygroup(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-security-group --group-id"

