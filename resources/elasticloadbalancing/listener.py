from resources.base_resources import BaseArn


class listener(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "elasticloadbalancing delete-listener --listener-arn"

