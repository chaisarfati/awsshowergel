import arn_retriever
import cli_argument_parser
import dependency_resolver
import dynamic_import_classes
import resource_deleter


# Parse the arguments of the command line
cli_args = cli_argument_parser.CliArguments()

# Get a map that maps aws resources names to the address of its corresponding class in this project
resource_classes = dynamic_import_classes.get_resource_to_class_map()

# Get a dependency graph representing the resources deletion dependencies (e.g. delete kms-alias before delete kms-key)
#valid_order_resources_deletion = dependency_resolver.get_valid_order_of_deletion(resource_classes)
valid_order_resources_deletion = dependency_resolver.DependencyResolver(resource_classes).get_valid_order_of_resource_deletion()

# Get the list of the ARNs of the resources we want to delete
#resources_to_delete_arns = arn_retriever.get_arns_of_resources_to_delete(cli_args)
resources_to_delete_arns = arn_retriever.AwsResourceRetriever(cli_args.tag_filters_tuple_list, cli_args.id_filters_map).get_arns_of_resources_to_delete()

rs_deleter = resource_deleter.ResourceDeleter(resources_to_delete_arns, resource_classes, valid_order_resources_deletion, cli_args.auto_approve, cli_args.dry_run)
rs_deleter.delete_resources()
# Delete the resources according to a valid order (considering dependencies)
#resource_deleter.delete_resources(resources_to_delete_arns, resource_classes, valid_order_resources_deletion, cli_args.dry_run)
