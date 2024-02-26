from resources.base_resources import BaseAwsResource


class rule(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "events delete-rule --name"

