from resources.base_resources import BaseArn


class customergateway(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-customer-gateway --customer-gateway-id"

