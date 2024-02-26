from resources.base_resources import BaseAwsResource


class addon(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ecs delete-addon --addon-name"

