def firstMissingPositive(nums):
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        # put num[i] to the correct place if nums[i] in the range [1, n]
        # condition on j: I did condition on i instead
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # so far, all the integers that could find their own correct place
    # have been put to the correct place, next thing is to find out the
    # place that occupied wrongly.
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


def test():
    inputs = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [1], [-1, 4, 2, 1, 9, 10]]
    expected = [3, 2, 1, 2, 3]

    count = 0
    for i in range(len(inputs)):
        actual = firstMissingPositive(inputs[i])
        if actual != expected[i]:
            print("Wrong at input: {count}").format(count=count)
            temp = expected[i]
            print("Expected: {temp} but got {actual}").format(temp=temp, actual=actual)
            return
        count += 1

    print("Passed test")


test()


"""
if I do a for loop,
every postion get one swap, but after swapping, one value may not be at the right position.
So I need to use while loop,
    I need to swap until all the values are at the right position
"""
