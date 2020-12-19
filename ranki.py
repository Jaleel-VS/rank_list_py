""""
Algorithm:
- Identify original list
- create empty list given size of the original list
- Loop through original list
    - find smallest value and keep track of its index
    - insert rank in empty list at said index 
    - increase rank
    - check if all values are filled with is_full function
"""

test_lst = [4, 500, 2, 1, 666, -5, 788, -69, 99999, 2, 3]
ranked_lst = [0] * (len(test_lst))
big_num = (2**63) - 1  # max value  of 64_bit int


def is_full(lst):
    for val in lst:
        if val == 0:
            return False
    return True


def rank_list(raw_list: list[int]) -> list[int]:
    copy_list = raw_list.copy()
    size = len(copy_list)
    smallest_index = 0
    rank = 0
    while not is_full(ranked_lst):
        smallest = big_num
        for i in range(size):
            if copy_list[i] < smallest:
                smallest = copy_list[i]
                smallest_index = i
        rank += 1
        # replace the smallest value in the test list with big_num
        copy_list[smallest_index] = big_num
        # insert smallest index in ranked list
        ranked_lst[smallest_index] = rank

    return ranked_lst


print(f"Original list: \n{test_lst}")
print(f"Ranked list: \n{rank_list(test_lst)}")
