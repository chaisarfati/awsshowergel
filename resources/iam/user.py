from resources.base_resources import BaseAwsResource


class user(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "iam delete-user --user-name"

