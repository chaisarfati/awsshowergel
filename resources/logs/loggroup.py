from resources.base_resources import BaseAwsResource


class loggroup(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "logs delete-log-group --log-group-name"

