from resources.base_resources import BaseAwsResource


class cluster(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "eks delete-cluster --name"

