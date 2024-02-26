from resources.base_resources import BaseAwsResource


class networkinterface(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-network-interface --network-interface-id"

