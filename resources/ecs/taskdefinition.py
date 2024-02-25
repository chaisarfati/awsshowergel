from resources.base_resources import BaseArn


class taskdefinition(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ecs deregister-task-definition --task-definition"

