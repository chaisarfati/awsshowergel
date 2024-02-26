from resources.base_resources import BaseAwsResource


class secret(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "secretsmanager delete-secret --secret-id"

