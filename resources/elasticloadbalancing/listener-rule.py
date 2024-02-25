from resources.base_resources import BaseArn


class listenerrule(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "elasticloadbalancing delete-listener-rule --rule-arn"

