def firstMissingPositive(nums):
  toReturn = 1
  for i in range(len(nums)):
    if nums[i] > 0 and nums[i] != i+1 and nums[i] < len(nums):
      temp = nums[i]
      nums[i] = nums[temp - 1]
      nums[temp - 1] = temp
  for i in nums:
    if i == toReturn:
      toReturn += 1
  print(nums)
  return toReturn

# def test():
#     inputs = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [1]]
#     expected = [3, 2, 1, 2]

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
print(firstMissingPositive([-1,4,2,1,9]))
