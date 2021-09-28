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

'''
Time: O(N.logN), where N is the length of nums.

On our first call to findBestSubarray, we use for loops to visit every element of nums.  Then, we split the array in half and call findBestSubarray with each half.  Both those calls will then iterate through element in that half, which combined is every element of nums again.  Then, both those halves wil be split in half, and 4 more calls to findBestSubarray will happen, each with a quarter of nums.
Every time the array is split, we still need to handle every element of the original input nums.
We have to do this log N times since that's how many times an array can be split in half.

Space: O(logN), where N is the length of nums
the extra space we use relative to input size is solely occupied by the recursion stack.
Each time the array gets split in half, another call of findBestSubarray will be added to the recursion stack, until calls start to get resolved by the base case -  remember, the base case happens at an empty array, which occurs after log N calls.

'''