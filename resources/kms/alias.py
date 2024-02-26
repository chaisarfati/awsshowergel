from resources.base_resources import BaseAwsResource

class alias(BaseAwsResource):

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "kms delete-alias --alias-name"

