from resources.base_resources import BaseAwsResource


class taskdefinition(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ecs deregister-task-definition --task-definition"

