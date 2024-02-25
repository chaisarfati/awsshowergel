from resources.base_resources import BaseArn


class recoverypoint(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "backup delete-recovery-point --recovery-point-arn"

