import json
import subprocess
from resources.base_resources import BaseAwsResource
from resources.ec2.natgateway import natgateway


class internetgateway(BaseAwsResource):
    DEPENDENT_ON_RESOURCES = [natgateway]

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-internet-gateway --internet-gateway-id"

    def preliminary_work(self):
        # First retrieve the vpc-id it is attached to
        result = subprocess.run(f"aws ec2 describe-internet-gateways --internet-gateway-ids {self.resource_id}",
                                shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            # Parse the JSON response
            response = json.loads(result.stdout)
            # Extract the VpcId from the response
            if 'InternetGateways' in response and len(response['InternetGateways']) > 0:
                attachments = response['InternetGateways'][0].get('Attachments', [])
                if attachments:
                    vpc_id = attachments[0].get('VpcId')
            else:
                print("No Internet Gateway found with the specified ID.")
        else:
            print("Error:", result.stderr)

        # Now detach the igw from the vpc
        result = subprocess.run(
            f"aws ec2 detach-internet-gateway --internet-gateway-id {self.resource_id} --vpc-id {vpc_id}",
            capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            print(f"Successfully detached internet-gateway {self.resource_id} from vpc {vpc_id}")
        else:
            print(result)
            raise ValueError(f"Failed to detach the internet-gateway {self.resource_id} from vpc {vpc_id}")
