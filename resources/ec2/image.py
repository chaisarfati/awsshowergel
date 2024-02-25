from resources.base_resources import BaseArn


class image(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 deregister-image --image-id"

