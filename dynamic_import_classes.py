import importlib.util
import pkgutil

# Directory containing the resource files
resource_dir = 'resources'


def build_resource_to_class_map():
    resource_classes = {}

    # Iterate over modules in the package
    package = importlib.import_module(resource_dir)

    # Get the package path
    package_path = package.__path__[0]


    for importer, modname, ispkg in pkgutil.walk_packages(path=[package_path], prefix=package.__name__ + '.'):
        module = importlib.import_module(modname)

        # Add the classes to the resource_classes dictionary
        for name, obj in module.__dict__.items():
            if isinstance(obj, type):
                resource_classes[modname] = getattr(module, name)

    return resource_classes

