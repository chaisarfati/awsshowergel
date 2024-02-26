from resources.base_resources import BaseAwsResource


class stack(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "cloudformation delete-stack --stack-name"

