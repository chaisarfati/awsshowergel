from resources.base_resources import BaseArn


class networkinsightspath(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-network-insights-path --network-insights-path-id"

