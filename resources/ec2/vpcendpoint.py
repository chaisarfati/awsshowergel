from resources.base_resources import BaseAwsResource


class vpcendpoint(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpc-endpoints --vpc-endpoint-ids"

