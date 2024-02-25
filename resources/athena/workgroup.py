from resources.base_resources import BaseArn


class workgroup(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "athena delete-work-group --work-group"

