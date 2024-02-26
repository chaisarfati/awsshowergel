from resources.base_resources import BaseAwsResource


class task(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ecs stop-task --task"

