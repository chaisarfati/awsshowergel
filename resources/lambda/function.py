from resources.base_resources import BaseArn


class function(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "lambda delete-function --function-name"

