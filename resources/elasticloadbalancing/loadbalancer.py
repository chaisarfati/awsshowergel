from resources.base_resources import BaseArn


class loadbalancer(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "elasticloadbalancing delete-load-balancer --load-balancer-name"

