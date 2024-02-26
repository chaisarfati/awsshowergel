from resources.base_resources import BaseAwsResource


class distribution(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "cloudfront delete-distribution --id"

