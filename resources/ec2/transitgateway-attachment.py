from resources.base_resources import BaseAwsResource


class transitgatewayattachment(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-transit-gateway-attachment --transit-gateway-attachment-id"

