from resources.base_resources import BaseAwsResource


class project(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "codebuild delete-project --name"

