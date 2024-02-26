from resources.base_resources import BaseAwsResource


class subgrp(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "rds delete-db-subnet-group --db-subnet-group-name"

