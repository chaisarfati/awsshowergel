from resources.base_resources import BaseAwsResource


class filesystem(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "efs delete-file-system --file-system-id"

