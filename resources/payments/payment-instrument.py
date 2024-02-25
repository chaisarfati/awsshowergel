from resources.base_resources import BaseArn


class paymentinstrument(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "payments delete-payment-instrument --id"

