from resources.base_resources import BaseAwsResource


class oidcprovider(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "iam delete-open-id-connect-provider --open-id-connect-provider-arn"

