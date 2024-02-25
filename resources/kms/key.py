from resources.base_resources import BaseArn
from resources.kms.alias import alias


class key(BaseArn):
    DEPENDENT_ON_RESOURCES = [alias]

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "kms delete-key --key-id"

