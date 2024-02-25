from resources.base_resources import BaseArn


class project(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "codebuild delete-project --name"

