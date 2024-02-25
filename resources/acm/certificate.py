from resources.base_resources import BaseArn


class certificate(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "acm delete-certificate --certificate-arn"

