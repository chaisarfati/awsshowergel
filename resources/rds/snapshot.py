from resources.base_resources import BaseArn


class snapshot(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "rds delete-db-snapshot --db-snapshot-identifier"

