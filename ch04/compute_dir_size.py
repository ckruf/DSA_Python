import os
import pathlib


def total_dir_size(dir_path: str | pathlib.Path) -> tuple[int, set]:
    """
    Given a path to a directory, return the total size of that directory in bytes, by recursively
    computing the sizes of all its subdirectories.

    :param dir_path: path to directory whose total size we want to know
    :return: total size of directory, including all its subdirectories
    """
    total = 0
    files = set()
    for child in os.listdir(dir_path):
        child_full_path = os.path.join(dir_path, child)
        if os.path.isdir(child_full_path):
            size, subdir_files = total_dir_size(child_full_path)
            total += size
            files.update(subdir_files)
        else:
            total += os.path.getsize(child_full_path)
            files.add(child_full_path)
    return total, files


def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents."""
  total = os.path.getsize(path)                  # account for direct usage
  if os.path.isdir(path):                        # if this is a directory,
    for filename in os.listdir(path):            # then for each child:
      childpath = os.path.join(path, filename)   # compose full path to child
      total += disk_usage(childpath)             # add child's usage to total

#   print ('{0:<7}'.format(total), path)           # descriptive output (optional)
  return total                                   # return the grand total


if __name__ == "__main__":
    total_size, files = total_dir_size("/Users/ckruf/Books")
    print(f"total size is {total_size} bytes")
    total_size = disk_usage("/Users/ckruf/Books")
    print(f"total size is {total_size} bytes")
    