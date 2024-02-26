from resources.base_resources import BaseAwsResource


class targetgroup(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "elasticloadbalancing delete-target-group --target-group-arn"

