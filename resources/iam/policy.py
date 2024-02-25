from resources.base_resources import BaseArn


class policy(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "iam delete-policy --policy-arn"

