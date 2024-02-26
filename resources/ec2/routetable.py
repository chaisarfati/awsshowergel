from resources.base_resources import BaseAwsResource
from resources.ec2.subnet import subnet


class routetable(BaseAwsResource):
    DEPENDENT_ON_RESOURCES = [subnet]

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-route-table --route-table-id"

