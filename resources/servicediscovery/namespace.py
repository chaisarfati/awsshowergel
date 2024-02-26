from resources.base_resources import BaseAwsResource


class namespace(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "servicediscovery delete-namespace --id"

