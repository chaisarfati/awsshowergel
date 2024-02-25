from resources.base_resources import BaseArn


class accesspoint(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "efs delete-access-point --access-point-id"

