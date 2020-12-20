unranked_list = [4, 500, 2, 1, 666, -5, 788, -69, 99999, 2, 3]
size = len(unranked_list)
rank_transform = [0] * size


def rank_it(lst: list[int]):
    sorted_list = sorted(lst)
    for i in range(size):
        for j in range(size):
            if unranked_list[i] == sorted_list[j]:
                rank_transform[i] = j + 1

    return rank_transform


print(f"Original list: \n{unranked_list}")
print(f"Ranked list: \n{rank_it(unranked_list)}")
