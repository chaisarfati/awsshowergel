from resources.base_resources import BaseAwsResource


class recoverypoint(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "backup delete-recovery-point --recovery-point-arn"

