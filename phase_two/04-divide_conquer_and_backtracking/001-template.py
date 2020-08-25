# 分治代码模版


def divide_conquer(problem, param1, param2):
    # recursion terminator
    if problem is None:
        print_result
        return

    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer sub-problems
    subresult1 = self.divide_conquer(subproblems[0], param1, param2)
    subresult2 = self.divide_conquer(subproblems[1], param1, param2)
    subresult3 = self.divide_conquer(subproblems[2], param1, param2)

    # process and generate/merge the final result
    result = process_result(subresult1, subresult2, subresult3)

    # revert the current level states
