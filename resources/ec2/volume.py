from resources.base_resources import BaseArn
from resources.ec2.snapshot import snapshot


class volume(BaseArn):

    DEPENDENT_ON_RESOURCES = [snapshot]

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-volume --volume-id"
