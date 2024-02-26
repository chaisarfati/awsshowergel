from resources.base_resources import BaseAwsResource


class topic(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "sns delete-topic --topic-arn"

