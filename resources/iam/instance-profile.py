from resources.base_resources import BaseArn


class instanceprofile(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "iam delete-instance-profile --instance-profile-name"

