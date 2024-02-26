import re
import subprocess


class BaseAwsResource:

    def __init__(self, arn):
        self.arn = arn
        self.arn_regex = r'^arn:(?P<Partition>[^:\n]*):(?P<Service>[^:\n]*):(?P<Region>[^:\n]*):(?P<AccountID>[^:\n]*):(?P<Ignore>(?P<ResourceType>[^:\/\n]*)[:\/])?(?P<Resource>.*)'
        self.resource_id = self.get_resource_id()
        self.object_identifier = self.get_object_identifier()
        self.deletion_method = None

    def get_resource_id(self):
        match = re.match(self.arn_regex, self.arn)
        if match:
            return match.group('Resource')
        else:
            raise ValueError("Invalid ARN format")

    # This method sets the object_identifier that will be used to reference the resource to delete.
    # By default, resources are referred by ID but some are not (e.g. sqs queue is identified by queue URL)
    def get_object_identifier(self):
        return self.get_resource_id()

    def delete_resource(self):
        self.preliminary_work()
        deletion_command = f"aws {self.deletion_method} {self.object_identifier}"
        print(f"Deleting {self._class_name()}:{self.resource_id}.......", end="")
        cmd_result = subprocess.run(deletion_command, shell=True)
        if cmd_result.returncode == 0:
            print("Success!")
        else:
            print(f"Failure during deletion. {cmd_result}")

    # This method would include tasks to performs before being able to delete the resource. Indeed, some
    # resources require such preliminary tasks (e.g. ec2:internet-gateway first detaches from its vpc)
    def preliminary_work(self):
        pass

    def _class_name(self):
        return type(self).__name__
