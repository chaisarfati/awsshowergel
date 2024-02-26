from resources.base_resources import BaseAwsResource


class keypair(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-key-pair --key-name"

