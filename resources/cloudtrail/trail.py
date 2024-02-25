from resources.base_resources import BaseArn


class trail(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "cloudtrail delete-trail --name"

