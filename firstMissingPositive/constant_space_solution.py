def firstMissingPositive(nums):
    n = len(nums)
    for i in range(len(nums)):
        # only sort in range: 1 <= i <= len(nums)
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    print(nums)

    # but when find for the position, I need to consider 0 and not negative number
    for k in range(n):
        if nums[k] >= 0 and nums[k] != k + 1:
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
print(firstMissingPositive([-1, 4, 2, 1, 9, 10]))
