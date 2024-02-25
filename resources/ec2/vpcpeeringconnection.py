from resources.base_resources import BaseArn


class vpcpeeringconnection(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpc-peering-connection --vpc-peering-connection-id"

