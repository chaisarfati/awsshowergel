from resources.base_resources import BaseAwsResource


class service(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ecs delete-service --service"

