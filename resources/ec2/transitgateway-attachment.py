from resources.base_resources import BaseArn


class transitgatewayattachment(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-transit-gateway-attachment --transit-gateway-attachment-id"

