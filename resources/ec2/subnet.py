import json
import subprocess

from resources.base_resources import BaseArn
from resources.ec2.internetgateway import internetgateway


class subnet(BaseArn):
    DEPENDENT_ON_RESOURCES = [internetgateway]

    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = "ec2 delete-subnet --subnet-id"

    def preliminary_work(self):
        self.detach_and_delete_network_interfaces_for_subnet()


    def detach_and_delete_network_interfaces_for_subnet(self):
        # Run AWS CLI command to describe the network interfaces associated with the subnet
        describe_command = f"aws ec2 describe-network-interfaces --filters Name=subnet-id,Values={self.resource_id}"
        describe_result = subprocess.run(describe_command, shell=True, capture_output=True, text=True)

        if describe_result.returncode == 0:
            # Parse the JSON response
            response = json.loads(describe_result.stdout)

            # Extract the Network Interface IDs
            for interface in response['NetworkInterfaces']:
                interface_id = interface['NetworkInterfaceId']
                attachment_id = interface['Attachment']['AttachmentId']

                # Detach the Network Interface
                detach_command = f"aws ec2 detach-network-interface --attachment-id {attachment_id}"
                detach_result = subprocess.run(detach_command, shell=True, capture_output=True, text=True)
                if detach_result.returncode == 0:
                    print(f"Successfully detached Network Interface {interface_id}")
                else:
                    print(f"Failed to detach Network Interface {interface_id}. Error: {detach_result.stderr}")

                # Delete the Network Interface
                delete_interface_command = f"aws ec2 delete-network-interface --network-interface-id {interface_id}"
                delete_result = subprocess.run(delete_interface_command, shell=True, capture_output=True, text=True)
                if delete_result.returncode == 0:
                    print(f"Successfully deleted Network Interface {interface_id}")
                else:
                    print(f"Failed to delete Network Interface {interface_id}. Error: {delete_result.stderr}")
        else:
            print("Error:", describe_result.stderr)
