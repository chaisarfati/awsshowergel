from resources.base_resources import BaseAwsResource


class function(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "lambda delete-function --function-name"

