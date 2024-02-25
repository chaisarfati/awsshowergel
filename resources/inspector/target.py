from resources.base_resources import BaseArn


class target(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "inspector delete-assessment-target --assessment-target-arn"

