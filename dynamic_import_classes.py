import importlib.util
import os


# Directory containing the resource files
resource_dir = 'resources'


# Function to recursively find Python files
def find_python_files(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                python_files.append(os.path.join(root, file))
    return python_files


def build_resource_to_class_map():
    resource_classes = {}

    # Iterate over Python files in the resource directory
    for file_path in find_python_files(resource_dir):
        # Construct the module name
        module_name = os.path.relpath(file_path, resource_dir)[:-3].replace(os.path.sep, '.')
        module_name = resource_dir + "." + module_name
        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Add the classes to the resource_classes dictionary
        for name, obj in module.__dict__.items():
            if isinstance(obj, type):
                resource_classes[module_name] = getattr(module, name)

    return resource_classes
