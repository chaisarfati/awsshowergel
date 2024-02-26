from resources.base_resources import BaseAwsResource


class stateMachine(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "stepfunctions delete-state-machine --state-machine-arn"

