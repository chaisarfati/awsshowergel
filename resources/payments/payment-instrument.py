from resources.base_resources import BaseAwsResource


class paymentinstrument(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "payments delete-payment-instrument --id"

