from resources.base_resources import BaseAwsResource


class hostedzone(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "route53 delete-hosted-zone --id"

