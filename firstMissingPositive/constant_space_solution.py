def firstMissingPositive(nums):
    n = len(nums)
    i = 0
    while i < n:
        print("i", i)
        # only sort in range: 1 <= nums[i] <= len(nums)
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # while i < n:
    #     j = nums[i] - 1
    #     # put num[i] to the correct place if nums[i] in the range [1, n]
    #     if 0 <= j < n and nums[i] != nums[j]:
    #         nums[i], nums[j] = nums[j], nums[i]
    #     else:
    #         i += 1

    # but when find for the position, I need to consider 0 and not negative number
    for k in range(n):
        if nums[k] != k + 1:
            return k + 1
    return n + 1


# def test():
#     inputs = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [1], [-1, 4, 2, 1, 9, 10]]
#     expected = [3, 2, 1, 2, 3]

#     count = 0
#     for i in range(len(inputs)):
#         actual = firstMissingPositive(inputs[i])
#         if actual != expected[i]:
#             print("Wrong at input: {count}").format(count=count)
#             temp = expected[i]
#             print("Expected: {temp} but got {actual}").format(temp=temp, actual=actual)
#             return
#         count += 1

#     print("Passed test")


# test()

print(firstMissingPositive([1, 1]))

"""
if I do a for loop,
every postion get one swap, but after swapping, one value may not be at the right position.
So I need to use while loop,
    I need to swap until all the values are at the right position
"""
