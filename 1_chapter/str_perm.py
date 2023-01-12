from itertools import permutations


call_count = 0


def string_permutations(chars: list[str]) -> list[str]:
    """
    Given a list of characters, return a list of all strings that can be made
    by using each character exactly once.
    """
    return list(permutations(chars))


def string_permutations_scratch(chars: list[str], start_index: int = 0, all_perms: list[str] = None) -> list[str]:
    """
    Given a list of characters, return a list of all string that can be made
    by using each character exactly once. But implemented from scratch.
    """
    global call_count
    call_count += 1
    str_len = len(chars)
    # print(f"chars is {chars} start_index is {start_index}, all_perms is {all_perms}")
    if all_perms is None:
        all_perms = []
    if start_index == str_len:
        # print("start_index = end_index, appending", "".join(chars))
        perm = "".join(chars)
        all_perms.append(perm)
    else:
        for loop_counter in range (start_index, str_len):
            # print(f"i is {loop_counter}")
            print(f"swapping chars[start_index], chars[loop_counter]", chars[start_index], chars[loop_counter], start_index, loop_counter)
            chars[start_index], chars[loop_counter] = chars[loop_counter], chars[start_index]
            string_permutations_scratch(chars, start_index+1, all_perms)
            chars[start_index], chars[loop_counter] = chars[loop_counter], chars[start_index]

    return all_perms


def string_permutations_scratch_1(chars: list[str], start_index: int = 0, all_perms: list[str] = None) -> list[str]:
    """
    Given a list of characters, return a list of all string that can be made
    by using each character exactly once. But implemented from scratch.
    """
    global call_count
    call_count += 1
    str_len = len(chars)
    if all_perms is None:
        all_perms = []
    for loop_counter in range(start_index, str_len):
        if loop_counter == str_len - 1 and start_index == str_len - 1:
            perm = "".join(chars)
            all_perms.append(perm)
        else:
            chars[start_index], chars[loop_counter] = chars[loop_counter], chars[start_index]
            string_permutations_scratch_1(chars, start_index+1, all_perms)
            # chars[start_index], chars[loop_counter] = chars[loop_counter], chars[start_index]

    return all_perms


if __name__ == "__main__":
    # print(string_permutations_scratch(["a", "b", "c",]))
    # print(f"call count is {call_count}")
    # call_count = 0
    print(f"call count is {call_count}")
    print(string_permutations_scratch_1(["a", "b", "c",]))
    print(f"call count is {call_count}")
