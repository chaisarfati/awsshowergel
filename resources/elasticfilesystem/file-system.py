from resources.base_resources import BaseArn


class filesystem(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "efs delete-file-system --file-system-id"

