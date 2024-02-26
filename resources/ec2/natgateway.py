from resources.base_resources import BaseAwsResource


class natgateway(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-nat-gateway --nat-gateway-id"

