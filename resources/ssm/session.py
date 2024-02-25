from resources.base_resources import BaseArn


class session(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ssm terminate-session --session-id"

