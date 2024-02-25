from resources.base_resources import BaseArn


class table(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "dynamodb delete-table --table-name"

