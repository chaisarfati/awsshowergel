import json
import re
import subprocess


class ArnParser:
    def __init__(self):
        self._arn_regex = (r'^arn:(?P<Partition>[^:\n]*):(?P<Service>[^:\n]*):(?P<Region>[^:\n]*):(?P<AccountID>['
                           r'^:\n]*):(?P<Ignore>(?P<ResourceType>[^:\/\n]*)[:\/])?(?P<Resource>.*)')

    def get_service_and_resource_type(self, arn):
        # Match the ARN against the regex pattern
        match = re.match(self._arn_regex, arn)
        if match:
            # Extract service and resource type from the match
            service = match.group('Service')
            resource_type = match.group('ResourceType')
        else:
            raise ValueError("Invalid ARN format")

        return service, resource_type


def print_deletion_plan(arns):
    if len(arns) == 0:
        print("No resources found to delete with the given filters.")
        return

    print(f"Will delete the {len(arns)} resources with ARNs:")
    i = 1
    for arn in arns:
        print(f"  {i}.\t\t{arn}")
        i += 1

    if input(f"Do you want to continue ? (y/n)") != "y":
        exit()


class AwsResourceRetriever:
    def __init__(self, tag_filters, id_pattern_filters, resource_tag_filters=None, service_tag_filters=None):
        self._arn_parser = ArnParser()
        self._tag_filters = tag_filters
        self._service_tag_filers = service_tag_filters
        self._resource_tag_filters = resource_tag_filters
        self._resource_id_filters = id_pattern_filters

    def get_arns_of_resources_to_delete(self):
        arns = get_arns_by_tag(self._tag_filters)
        arns = self._filter_arns_by_id_filters(arns)
        print_deletion_plan(arns)
        return arns

    def _filter_arns_by_id_filters(self, arns_list):
        arns_matching_id_filter = []
        for arn in arns_list:
            service, resource_type = get_service_and_resource_type(arn)
            if resource_type and resource_type in self._resource_id_filters:
                if re.search(self._resource_id_filters[resource_type], arn):
                    arns_matching_id_filter.append(arn)
            elif service in self._resource_id_filters:
                if re.search(self._resource_id_filters[service], arn):
                    arns_matching_id_filter.append(arn)
            else:
                arns_matching_id_filter.append(arn)
        return arns_matching_id_filter


def get_arns_of_resources_to_delete(cli_args):
    arns = get_arns_by_tag(cli_args.tag_filters_tuple_list)
    arns = filter_arns_by_id_filters(arns, cli_args)
    return arns


def get_arns_by_tag(tags):
    tag_filters = create_tag_filters_string(tags)
    command = f"aws resourcegroupstaggingapi get-resources {tag_filters} --query ResourceTagMappingList[].ResourceARN"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        arns_json = result.stdout.strip()
        try:
            arns_list = json.loads(arns_json)
            return arns_list
        except json.JSONDecodeError:
            print("Error: Unable to parse JSON response")
            return []
    else:
        print("Error:", result.stderr)
        return []


def create_tag_filters_string(tags):
    tag_filters = ""
    for key, value in tags:
        tag_filters += f" --tag-filters Key={key},Values={value} "
    return tag_filters


def filter_arns_by_id_filters(arn_list, cli_args):
    arns_matching_id_filter = []
    for arn in arn_list:
        service, resource_type = get_service_and_resource_type(arn)
        if resource_type and resource_type in cli_args.id_filters_map:
            if re.search(cli_args.id_filters_map[resource_type], arn):
                arns_matching_id_filter.append(arn)
        elif service in cli_args.id_filters_map:
            if re.search(cli_args.id_filters_map[service], arn):
                arns_matching_id_filter.append(arn)
        else:
            if not cli_args.only_delete_filtered_ids:
                arns_matching_id_filter.append(arn)
    return arns_matching_id_filter


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

