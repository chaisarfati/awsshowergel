from resources.base_resources import BaseAwsResource


class workgroup(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "athena delete-work-group --work-group"

