from resources.base_resources import BaseAwsResource
from resources.ec2.subnet import subnet
from resources.ec2.routetable import routetable


class vpc(BaseAwsResource):
    DEPENDENT_ON_RESOURCES = [subnet, routetable]

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-vpc --vpc-id"

