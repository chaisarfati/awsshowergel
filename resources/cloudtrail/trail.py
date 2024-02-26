from resources.base_resources import BaseAwsResource


class trail(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "cloudtrail delete-trail --name"

