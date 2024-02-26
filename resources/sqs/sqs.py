import json
import subprocess

from resources.base_resources import BaseAwsResource


class sqs(BaseAwsResource):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "sqs delete-queue --queue-url"

    def get_object_identifier(self):
        result = subprocess.run(f"aws sqs get-queue-url --queue-name {self.resource_id}", capture_output=True,
                                text=True, shell=True)
        if result.returncode == 0:
            queue_info = json.loads(result.stdout.strip())
            queue_url = queue_info.get("QueueUrl")
            if queue_url:
                return queue_url
            else:
                raise ValueError("Queue URL not found in response")
        else:
            raise ValueError("Failed to retrieve queue URL")
