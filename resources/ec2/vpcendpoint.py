from resources.base_resources import BaseArn


class vpcendpoint(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpc-endpoints --vpc-endpoint-ids"

