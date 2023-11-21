"""
File containing a side project - iterating over a file system, and
reporting the size of each file and folder.
"""

import os

current_dir_name = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir_name)

excluded_directories = {".git", "env", "__pycache__", ".pytest_cache", ".idea"}

total_calls = 0

def compute_directory_size(directory_location: os.PathLike) -> int:
    """
    Given a path-like directory location, return the size of the directory 
    (including all the files and sub-directories it contains).
    """
    sub_total = 0
    for name in os.listdir(directory_location):
        path = os.path.join(directory_location, name)
        if os.path.isfile(path):
            sub_total += os.path.getsize(path)
        elif os.path.isdir(path):
            sub_total += compute_directory_size(path)
    return sub_total

def compute_and_print_directory_sizes(directory_location: os.PathLike, depth: int = 0) -> None:
    """
    Given a path-like directory location, go through all the files and 
    sub-directories, and print out the total file size of all (sub)directories.
    """
    global total_calls
    total_calls += 1
    sub_total = 0
    for name in os.listdir(directory_location):
        if name in excluded_directories:
            continue
        path = os.path.join(directory_location, name)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            # print(f"File: {filename}, Size: {size} bytes")
            sub_total += size
        elif os.path.isdir(path):
            sub_dir_size = compute_and_print_directory_sizes(path, depth + 1)
            print(2 * depth * " ", end="")  # print indentation
            print(f"{path} size: {sub_dir_size}")
    return sub_total

def pretty_print_directory_sizes_fail(
        directory_location: os.PathLike,
        depth: int = 0
) -> None:
    """
    Failed attempt to pretty print sizes of directory.
    This particular implementation does not work, because
    calling os.path.getsize() on a directory does not reutrn the total size of
    all the contents of the directory.

    But the general challenge is that you'd want to print the directories
    by doing a preorder traversal, but to compute the size of the directory,
    you need to do a postorder traversal.
    """
    if os.path.isdir(directory_location):
        directory_contents = os.listdir(directory_location)
        directory_contents.sort()
        print(2 * depth *  " ", end="")
        print(directory_location, os.path.getsize(directory_location))
        for name in directory_contents:
            if name in excluded_directories:
                continue
            path = os.path.join(directory_location, name)
            pretty_print_directory_sizes_fail(path, depth + 1)


def pretty_print_directory_sizes_second_fail(
        directory_location: os.PathLike,
        depth: int = 0,
) -> int:
    """
    Another attempt to pretty print sizes of a directory (and its subdirs).
    This one fails, because the name of the directory gets printed first,
    which is then interrupted by output from the subtree, after which the 
    size is printed.
    """
    global total_calls
    total_calls += 1
    print(2 * depth * " ", end="")
    print(directory_location, end="")
    sub_total = 0
    directory_contents = os.listdir(directory_location)
    directory_contents.sort()
    for name in directory_contents:
        if name in excluded_directories:
            continue
        full_path = os.path.join(directory_location, name)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            sub_total += size
        elif os.path.isdir(full_path):
            sub_total += pretty_print_directory_sizes_second_fail(full_path, depth + 1)
    print(f" {sub_total} bytes")
    return sub_total


def pretty_print_directory_sizes(root_location: os.PathLike) -> None:
    """
    This one succeeds, but uses a dict to store auxilliary data, so O(n) memory used
    """

    def collect_results(
        directory_location: os.PathLike,
        results: dict,
        depth: int,
    ) -> int:
        """
        Another attempt to pretty print sizes of a directory (and its subdirs).
        """
        global total_calls
        total_calls += 1
        location_string = 2 * depth * " " + directory_location
        results[location_string] = 0
        sub_total = 0
        directory_contents = os.listdir(directory_location)
        directory_contents.sort()
        for name in directory_contents:
            if name in excluded_directories:
                continue
            full_path = os.path.join(directory_location, name)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                sub_total += size
            elif os.path.isdir(full_path):
                sub_total += collect_results(full_path, results, depth + 1)
        results[location_string] = sub_total
        return sub_total
    
    def pretty_print_dict(results: dict) -> None:
        for key, value in results.items():
            print(f"{key} {value} bytes")

    dirs_and_sizes = {}
    collect_results(root_location, dirs_and_sizes, 0)
    pretty_print_dict(dirs_and_sizes)


def pretty_print_directory_size_GPT(directory_location: os.PathLike, depth: int = 0, calculate_only: bool = False) -> int:
    """
    This one is by ChatGPT, it succeeds, but is very inefficient, because it calculates the entire
    subtree separately for each directory.
    """
    global total_calls
    total_calls += 1
    sub_total = 0
    directory_contents = os.listdir(directory_location)
    directory_contents.sort()

    # First pass: Calculate total size
    for name in directory_contents:
        full_path = os.path.join(directory_location, name)
        if os.path.isfile(full_path):
            sub_total += os.path.getsize(full_path)
        elif os.path.isdir(full_path) and name not in excluded_directories:
            sub_total += pretty_print_directory_size_GPT(full_path, depth + 1, calculate_only=True)

    # Second pass: Print directory and its total size
    if not calculate_only:
        indent = " " * (2 * depth)
        print(f"{indent}{directory_location} {sub_total} bytes")
        for name in directory_contents:
            full_path = os.path.join(directory_location, name)
            if os.path.isdir(full_path) and name not in excluded_directories:
                pretty_print_directory_size_GPT(full_path, depth + 1)

    return sub_total

if __name__ == "__main__":
    # compute_directory_sizes(parent_dir)
    # pretty_print_directory_sizes(parent_dir)
    # pretty_print_directory_sizes_second_fail(parent_dir)
    # pretty_print_directory_size_GPT(parent_dir)
    pretty_print_directory_sizes(parent_dir)
    # print(total_calls)
    print(parent_dir)
    print(compute_directory_size(parent_dir))