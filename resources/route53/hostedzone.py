from resources.base_resources import BaseArn


class hostedzone(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "route53 delete-hosted-zone --id"

