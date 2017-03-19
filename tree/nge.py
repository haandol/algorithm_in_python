# http://www.geeksforgeeks.org/next-greater-element/

def solution(L, q):
    query_element = None
    for i, el in enumerate(L):
        if el == q:
            query_element = el

        if query_element is None:
            continue
        else:
            if el > query_element:
                return el
    return -1


if __name__ == '__main__':
    L = [4, 5, 2, 25]
    assert 5 == solution(L, 4)
    assert 25 == solution(L, 5)
    assert 25 == solution(L, 2)
    assert -1 == solution(L, 25)

    L = [13, 7, 6, 12]
    assert -1 == solution(L, 13)
    assert 12 == solution(L, 7)
    assert 12 == solution(L, 6)
    assert -1 == solution(L, 12)
