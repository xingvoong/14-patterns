'''
left_half = findBestSubarray(nums, left, mid - 1)
right_haft = findBestSubarray(nums, mid + 1, right)

if I do not do this, I only consider move forward, with a
continuous sum.
The goal is to break down the main array,
to smaller arrays and sum arrays.

'''
def max_subarray(nums):
  # import math
  def findBestSubarray(nums, left, right):
    if left > right:
      return -float('inf')

    mid = (left + right) // 2
    curr = best_left_sum = best_right_sum = 0

    # iterate from the middle to the beginning.
    for i in range(mid - 1, left - 1, -1):
      curr += nums[i]
      best_left_sum = max(best_left_sum, curr)

    # reset curr and iterate from the middle to the end
    curr = 0
    for i in range(mid + 1, right + 1):
      curr += nums[i]
      best_right_sum = max(best_right_sum, curr)

    # The best_combined sum uses the middle element and
    # the best possible sum from each haft.
    best_combined_sum = nums[mid] + best_left_sum + best_right_sum

    # Find the best subarray possible from both halves
    left_half = findBestSubarray(nums, left, mid - 1)
    right_haft = findBestSubarray(nums, mid + 1, right)

    # The largest of the 3 is the answer for any given input array
    return max(best_combined_sum, left_half, right_haft)

  return findBestSubarray(nums, 0, len(nums) - 1)

def test():
  input = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]
  expected = [6, 1, 23]
  for i in range(len(input)):
    actual = max_subarray(input[i])
    if (actual != expected[i]):
      print('Wrong at input: {i}').format(i = i)
      temp = expected[i]
      print('Expected: {temp} but got {actual}').format(temp=temp,actual=actual)
      return

  print('Passed test')

test()