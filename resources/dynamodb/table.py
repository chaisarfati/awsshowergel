from resources.base_resources import BaseAwsResource


class table(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "dynamodb delete-table --table-name"

