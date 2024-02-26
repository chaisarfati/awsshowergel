from resources.base_resources import BaseAwsResource


class db(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "rds delete-db --db-instance-identifier"

