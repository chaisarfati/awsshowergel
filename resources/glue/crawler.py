from resources.base_resources import BaseAwsResource


class crawler(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "glue delete-crawler --name"

