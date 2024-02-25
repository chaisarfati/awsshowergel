from resources.base_resources import BaseArn


class subgrp(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "rds delete-db-subnet-group --db-subnet-group-name"

