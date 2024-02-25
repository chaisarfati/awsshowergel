from resources.base_resources import BaseArn


class task(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ecs stop-task --task"

