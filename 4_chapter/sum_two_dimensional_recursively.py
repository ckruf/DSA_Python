def sum_matrix(matrix):
    print(f"sum_matrix called with _{matrix}")
    if not matrix:
        return 0
    else:
        return sum(matrix[0]) + sum_matrix(matrix[1:])





if __name__ == "__main__":
    test_matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(sum_matrix(test_matrix))