from resources.base_resources import BaseArn


class stateMachine(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "stepfunctions delete-state-machine --state-machine-arn"

