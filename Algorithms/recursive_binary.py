def recursive_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_search(list[midpoint + 1:], target)
        elif list[midpoint] > target:
            return recursive_search(list[:midpoint], target)
    return False


def verify(result):
    print("Target Status: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

results = recursive_search(numbers, 1)
verify(results)
