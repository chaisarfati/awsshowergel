from resources.base_resources import BaseAwsResource


class target(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "inspector delete-assessment-target --assessment-target-arn"

