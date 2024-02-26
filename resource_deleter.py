import re

from arn_retriever import ArnParser


class ResourceDeleter(object):
    def __init__(self, arn_list_to_delete, resource_classes, order_of_deletion, auto_approve=False, dry_run=False):
        self._arn_parser = ArnParser()
        self._arn_list_to_delete = arn_list_to_delete
        self._resource_classes = resource_classes
        self._order_of_deletion = order_of_deletion
        self._auto_approve = auto_approve
        self._dry_run = dry_run

    def print_order_of_deletion(self):
        print(f"Ordered deletion: {self._order_of_deletion}")

    def _ask_user_approval_before_deletion(self, aws_resource):
        if not self._dry_run and not self._auto_approve:
            if input(f"Are you sure to delete {type(aws_resource).__name__} with ID {aws_resource.resource_id} ? (y/n)") != "y":
                exit()

    def _delete_aws_resource(self, aws_resource):
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
                    self._ask_user_approval_before_deletion(n)
                    self._delete_aws_resource(n)

        print("\n2) Second, removing all the dependent resources...")
        for res_to_del in self._order_of_deletion:
            if res_to_del in to_delete.keys():
                res_arns = to_delete[res_to_del]
                for res_arn in res_arns:
                    self._ask_user_approval_before_deletion(res_arn)
                    self._delete_aws_resource(res_arn)

    def get_resources_to_delete(self):
        map_of_resources_to_delete = {}

        for arn in self._arn_list_to_delete:
            service, resource_type = self._arn_parser.get_service_and_resource_type(arn)

            if resource_type:
                resource_type = resource_type.replace("-", "", -1)
                resource_class = self._resource_classes["resources." + service + "." + resource_type]
            else:
                resource_class = self._resource_classes["resources." + service + "." + service]

            if resource_class in map_of_resources_to_delete:
                map_of_resources_to_delete[resource_class].append(resource_class(arn))
            else:
                map_of_resources_to_delete[resource_class] = [resource_class(arn)]

        return map_of_resources_to_delete



