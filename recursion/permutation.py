def permute(result, arr, r, depth):
    if r == depth:
        if arr not in result:
            result.append(arr[:])
    else:
        for i in range(depth, r+1):
            arr[i], arr[depth] = arr[depth], arr[i]
            permute(result, arr, r, depth+1)
            arr[i], arr[depth] = arr[depth], arr[i]


def solution(arr):
    result = list()
    permute(result, arr, len(arr)-1, 0)
    return result


print solution(['A', 'B', 'C'])
print
print solution(['A', 'C', 'B', 'C'])
