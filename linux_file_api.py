# Strategy Pattern combined with some Composite Pattern
from abc import ABC, abstractmethod

# File class representing a file with name, extension, and size
class File:
    def __init__(self, name, type, size):
        self.name = name
        self.extension = type
        self.size = size

    def get_name(self):
        return self.name

    def get_extension(self):
        return self.extension

    def get_size(self):
        return self.size


# Abstract base class for filters
class Filter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def match(self, file):
        pass


# Name-based filter implementation
class NameFilter(Filter):
    def __init__(self, name):
        self.name = name

    def match(self, file):
        return file.get_name() == self.name


# Size-based filter implementation
class SizeFilter(Filter):
    def __init__(self, properties):
        self.size = properties[0]
        self.operator = properties[1]

    def match(self, file):
        # Use eval to apply the operator dynamically
        return eval(str(file.get_size()) + str(self.operator) + str(self.size))


# Extension-based filter implementation
class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def match(self, file):
        return file.get_extension() == self.extension


# FileSystem class to represent directories and files
class FileSystem:
    def __init__(self, name, isDirectory=False, subDirectories=[], files=[]):
        self.name = name
        self.isDirectory = isDirectory
        self.subDirectory = subDirectories
        self.files = files

    def add_file(self, directory, sub_directory, file):
        pass

    def delete_file(self, directory, sub_directory, file):
        pass


# Search class to handle file searching with filters
class Search:
    def __init__(self, directory, filter, fileSystem, condition=None):
        self.directory = directory
        self.filters = filter
        self.fileSystem = fileSystem
        self.condition = condition

    def check_conditions(self, file, instances, condition):
        if condition is None:
            return instances[0].match(file)
        elif condition == "AND":
            return all([instance.match(file) for instance in instances])
        else:
            return any([instance.match(file) for instance in instances])

    def find_files(self):
        root = self.fileSystem
        queue = [root]

        filter_classes = []
        for filter, value in self.filters.items():
            # Dynamically create filter instances using globals()
            filter_classes.append(globals().get(filter)(value))
        res = []

        # BFS traversal
        while queue:
            for each_file in root.files:
                if self.check_conditions(each_file, filter_classes, self.condition):
                    res.append(each_file.get_name())
            node = queue.pop(0)
            for each_subdirectory in node.subDirectory:
                queue.append(each_subdirectory)

        return res


# Main execution for simulation
if __name__ == "__main__":
    # Create sample files
    f1 = File("abc", "txt", 10)
    f2 = File("cde", "txt", 20)
    f3 = File("def", "pdf", 30)
    f4 = File("ghi", "py", 5)
    f5 = File("uvw", "java", 10)

    # Create a file system with sample files
    directory_files = [f1, f2, f3, f4, f5]
    fileSystem = FileSystem("/", True, [], directory_files)

    # Test various search filters
    # Example: Search by name
    # res = Search(directory_files, {"NameFilter": "abc"}, fileSystem).find_files()
    # print(res)

    # Example: Search by size
    # res = Search(directory_files, {"SizeFilter": (10, ">=")}, fileSystem).find_files()
    # print(res)

    # Example: Search by extension and size with OR condition
    res = Search(directory_files, {"ExtensionFilter": "java", "SizeFilter": (10, ">=")}, fileSystem, "OR").find_files()
    print(res)