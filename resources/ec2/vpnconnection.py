from resources.base_resources import BaseAwsResource


class vpnconnection(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpn-connection --vpn-connection-id"

