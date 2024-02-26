from resources.base_resources import BaseAwsResource


class document(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ssm delete-document --name"

