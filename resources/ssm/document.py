from resources.base_resources import BaseArn


class document(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ssm delete-document --name"

