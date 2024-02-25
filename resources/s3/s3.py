from resources.base_resources import BaseArn


class s3(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)  # Call the __init__ method of the parent class
        self.deletion_method = "s3api delete-bucket --bucket"


