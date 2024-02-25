from resources.base_resources import BaseArn


class distribution(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "cloudfront delete-distribution --id"

