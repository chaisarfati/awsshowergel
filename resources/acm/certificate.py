from resources.base_resources import BaseAwsResource


class certificate(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "acm delete-certificate --certificate-arn"

