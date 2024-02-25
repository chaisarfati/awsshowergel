from resources.base_resources import BaseArn


class vpnconnection(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpn-connection --vpn-connection-id"

