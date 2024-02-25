import dependency_resolver
import re


class ResourceDeleter(object):
    def __init__(self, arn_list_to_delete, resource_classes, order_of_deletion, auto_approve=False, dry_run=False):
        self._arn_list_to_delete = arn_list_to_delete
        self._resource_classes = resource_classes
        self._order_of_deletion = order_of_deletion
        self._auto_approve = auto_approve
        self._dry_run = dry_run

    def print_order_of_deletion(self):
        print(f"Ordered deletion: {self._order_of_deletion}")

    def ask_user_approval_before_deletion(self, aws_resource):
        if not self._dry_run and not self._auto_approve:
            if input(f"Are you sure to delete {type(aws_resource).__name__} with ID {aws_resource.resource_id} ? (y/n)") != "y":
                exit()

    def delete_aws_resource(self, aws_resource):
        if self._dry_run:
            print(f"..[Dry run] Would delete AWS resource {type(aws_resource).__name__} with ID {aws_resource.resource_id}")
        else:
            aws_resource.delete_resource()

    def delete_resources(self):
        to_delete = get_resources_to_delete(self._arn_list_to_delete, self._resource_classes)

        print("\n1) First, removing all the resources with no dependencies...")
        for key, ress in to_delete.items():
            # It has not dependencies
            if key not in self._order_of_deletion:
                for n in ress:
                    self.ask_user_approval_before_deletion(n)
                    self.delete_aws_resource(n)

        print("\n2) Second, removing all the dependent resources...")
        for res_to_del in self._order_of_deletion:
            if res_to_del in to_delete.keys():
                res_arns = to_delete[res_to_del]
                for res_arn in res_arns:
                    self.ask_user_approval_before_deletion(res_arn)
                    self.delete_aws_resource(res_arn)


def delete_resources(arn_list, resource_classes, ordered_deletion, dry_run):
    to_delete = get_resources_to_delete(arn_list, resource_classes)

    print(f"Ordered deletion: {ordered_deletion}")

    print("\n1) First, removing all the resources with no dependencies...")
    for key, ress in to_delete.items():
        # It has not dependencies
        if key not in ordered_deletion:
            for n in ress:
                n.delete_resource()

    print("\n2) Second, removing all the dependent resources...")
    for res_to_del in ordered_deletion:
        if res_to_del in to_delete.keys():
            res_arns = to_delete[res_to_del]
            for res_arn in res_arns:
                res_arn.delete_resource()


def get_service_and_resource_type(arn):
    # Define the regex pattern
    arn_regex = r'^arn:(?P<Partition>[^:\n]*):(?P<Service>[^:\n]*):(?P<Region>[^:\n]*):(?P<AccountID>[^:\n]*):(?P<Ignore>(?P<ResourceType>[^:\/\n]*)[:\/])?(?P<Resource>.*)'

    # Match the ARN against the regex pattern
    match = re.match(arn_regex, arn)
    if match:
        # Extract service and resource type from the match
        service = match.group('Service')
        resource_type = match.group('ResourceType')
    else:
        raise ValueError("Invalid ARN format")

    return service, resource_type


# def delete_resource(arn, resource_classes):
#     service, resource_type = get_service_and_resource_type(arn)
#
#     if resource_type:
#         resource_type = resource_type.replace("-", "", -1)
#         resource_class = resource_classes[resource_type]
#     else:
#         resource_class = resource_classes[service]
#
#     resource_class(arn).delete_resource()


def get_resources_to_delete(arn_list, resource_classes):
    map_of_resources_to_delete = {}

    for arn in arn_list:
        service, resource_type = get_service_and_resource_type(arn)

        if resource_type:
            resource_type = resource_type.replace("-", "", -1)
            resource_class = resource_classes["resources." + service + "." + resource_type]
        else:
            resource_class = resource_classes["resources." + service + "." + service]

        if resource_class in map_of_resources_to_delete:
            map_of_resources_to_delete[resource_class].append(resource_class(arn))
        else:
            map_of_resources_to_delete[resource_class] = [resource_class(arn)]

    return map_of_resources_to_delete
