from resources.base_resources import BaseAwsResource


class nodegroup(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "eks delete-nodegroup --nodegroup-name --cluster-name"

