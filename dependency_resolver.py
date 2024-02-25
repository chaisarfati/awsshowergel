class DependencyResolver:
    def __init__(self, resource_classes):
        self._resource_classes = resource_classes
        self._class_name_to_class_map = self._init_class_name_to_class_map()
        self._dependency_graph = self._build_dependency_graph()

    # This method constructs a mapping from the full class name (module.class_name) to a class
    # object. This is a sort of Bean dictionary that maps the name of the bean to the class
    # address. This prevents us from having two class objects of the same class since those
    # class objects would not be equal under '==' or 'is' operators. Having beans solves this.
    def _init_class_name_to_class_map(self):
        self._class_name_to_class_map = {}
        for class_name, class_type in self._resource_classes.items():
            self._class_name_to_class_map[f"{class_type.__module__}.{class_type.__name__}"] = class_type
        return self._class_name_to_class_map

    # Build a dict representing the dependencies between resources deletion
    def _build_dependency_graph(self):
        self._dependency_graph = {}
        for class_name, class_type in self._resource_classes.items():
            if hasattr(class_type, 'DEPENDENT_ON_RESOURCES') and class_type.DEPENDENT_ON_RESOURCES:
                for depending_class in class_type.DEPENDENT_ON_RESOURCES:
                    dependence_class_bean = self._get_class_bean(depending_class)
                    dependent_class_bean = self._get_class_bean(class_type)
                    if dependent_class_bean in self._dependency_graph:
                        self._dependency_graph[dependent_class_bean].append(dependence_class_bean)
                    else:
                        self._dependency_graph[dependent_class_bean] = [dependence_class_bean]
        return self._dependency_graph

    # Get a unique representation of class name
    def _get_class_bean(self, clazz):
        return self._class_name_to_class_map[get_full_class_name(clazz)]

    # Get a list that indicates the order in which resources could be deleted taking into accounts dependencies
    def get_valid_order_of_resource_deletion(self):
        reverse = {}
        for key, nodes in self._dependency_graph.items():
            for node in nodes:
                reverse.setdefault(node, []).append(key)

        return topological_sort(reverse)


def get_full_class_name(clazz):
    return clazz.__module__ + "." + clazz.__name__


# https://stackoverflow.com/questions/52432988/python-dict-key-order-based-on-values-recursive-solution
def topological_sort(graph):
    # init the indegree for each noe
    nodes = graph.keys() | set([node for adjacent in graph.values() for node in adjacent])
    in_degree = {node: 0 for node in nodes}

    # compute the in_degree
    for k, adjacent in graph.items():
        for node in adjacent:
            in_degree[node] += 1

    # init the heap with the nodes with indegree 0 and priority given by key
    heap = [node for node, degree in in_degree.items() if degree == 0]

    top_order = []
    while heap:  # heap is not empty
        node = heap.pop()  # get the element with the highest priority and remove from heap
        top_order.append(node)  # add to topological order
        for adjacent in graph.get(node, []):  # iter over the neighbors of the node
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:  # if the node has in_degree 0 add to the heap with priority given by key
                heap.append(adjacent)

    return top_order
