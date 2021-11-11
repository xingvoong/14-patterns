def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def test():
    inputs = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [0]]
    expected = [2, 2, 8, 1]
    count = 0
    for i in range(len(inputs)):
        actual = missingNumber(inputs[i])
        if actual != expected[i]:
            print("Wrong at input: {count}").format(count=count)
            temp = expected[i]
            print("Expected: {temp} but got {actual}").format(temp=temp, actual=actual)
            return
        count += 1

    print("Passed test")


test()

"""
runtime: O(N), depends on how I take the sum
space: O(1)

"""
