import argparse


class CliArguments:
    def __init__(self):
        self._parser = argparse.ArgumentParser(prog="awsshowergel", description="Simple CLI tool to batch-delete AWS resources by Tags and by IDs pattern")
        self._args = self._parse_arguments()
        self.tag_filters_tuple_list = self._init_tag_filters()
        self.id_filters_map = self._init_id_filers_map()
        self.auto_approve = self._init_auto_approve()
        self.only_delete_filtered_ids = self._init_only_delete_filtered_ids()
        self.dry_run = self._init_dry_run()
        self.print_deletion_filters()

    def _parse_arguments(self):
        self._parser.add_argument('--tag-filters', nargs='+', metavar=('KEY=VALUE'), action='append', help="Tag filters")
        self._parser.add_argument('--id-filters', nargs='+', metavar=('KEY=VALUE'), action='append', help="ID filters")
        self._parser.add_argument("--only-delete-filtered-ids", action='store_true', help="If true, awsshowergel will only delete resources matching the given --id-filters")
        self._parser.add_argument("--dry-run", action='store_true', help="If true, awsshowergel will only show you resources it would delete but will not delete them.")
        self._parser.add_argument("--auto-approve", action='store_true', help="If true, awsshowergel will not ask your approval before each resource deletion")

        return self._parser.parse_args()

    def _init_tag_filters(self):
        tag_filters_tuple_list = []
        if self._args.tag_filters:
            for filter_arg in self._args.tag_filters:
                key, value = filter_arg[0].split('=')
                tag_filters_tuple_list.append((key, value))
        return tag_filters_tuple_list

    def print_deletion_filters(self):
        if self.dry_run:
            print("Running in DRY RUN mode... Noting will be deleted")

        print(f".......Planning to delete AWS resources with tags: {self.tag_filters_tuple_list}\n")
        print(f".......Planning to delete AWS resources with IDs matching regex: {self.id_filters_map}\n")

    def _init_id_filers_map(self):
        id_filters_map = {}
        if self._args.id_filters:
            for filter_arg in self._args.id_filters:
                for item in filter_arg:
                    key, value = item.split('=')
                    id_filters_map[key] = value
        return id_filters_map

    def _init_auto_approve(self):
        if self._args.auto_approve:
            return True
        return False

    def _init_dry_run(self):
        if self._args.dry_run:
            return True
        return False

    def _init_only_delete_filtered_ids(self):
        if self._args.only_delete_filtered_ids:
            return True
        return False


