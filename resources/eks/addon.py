from resources.base_resources import BaseArn


class addon(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "eks delete-addon --cluster-name"

