from resources.base_resources import BaseArn


class vpngateway(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpn-gateway --vpn-gateway-id"

