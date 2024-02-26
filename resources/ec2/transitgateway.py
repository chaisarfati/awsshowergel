from resources.base_resources import BaseAwsResource


class transitgateway(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-transit-gateway --transit-gateway-id"

