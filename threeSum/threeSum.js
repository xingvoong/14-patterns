/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Example 4:
Input: nums = [-4, -1, -1, 0, 1, 4]
Output:

Constraints:
- 0 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
*/

var twoSum = function(i, nums, result) {
  var left = i + 1
  var right = nums.length - 1
  count = 0
  while (left < right) {
    var sum = nums[i] + nums[left] + nums[right]
    if (sum < 0) {
      left += 1
    } else if (sum > 0) {
      right -= 1
    } else {
      result.push([nums[i], nums[left], nums[right]])
      left += 1
      right -= 1
      // to avoid duplicate triplet, increase left
      while (left < right && nums[left] == nums[left - 1]) {
        left += 1
      }
    }
  }
  return result
}

var threeSum = function(nums) {
  var n = nums.length
  nums.sort((a, b) => a - b)
  var result = []

  for(var i = 0; i < n; i++) {
    if (nums[i] > 0) {
      break
    }
    //i == 0 so that we do not go off bound.
    if (i == 0 || nums[i] != nums[i-1]) {
      twoSum(i, nums, result)
    }
  }
  return result
}

var test = function() {
  var input = [[0, 1, -1, -4, -1, 2], [], [0], [0, 1, -1, -4, -1, 2, -3, 3]]
  var expected = [[[ -1, -1, 2 ], [ -1, 0, 1 ]], [], [], [
  [ -4, 1, 3 ],
  [ -3, 0, 3 ],
  [ -3, 1, 2 ],
  [ -1, -1, 2 ],
  [ -1, 0, 1 ]
]]
  for(var i = 0; i < input.length; i++) {
    var actual = threeSum(input[i])
    if (actual.length !== 0 && actual.reduce((a,b) => a && expected[i].includes[b]), false) {
      console.log(`Wrong at input: ${i}`)
      console.log(`Expected: ${expected[i]} but got ${actual}`)
      return
    }
  }
  console.log('Passed test')
}

test()
/*
time: O(N^2):
twoSum is O(N), we call it N time
space:
O(N) for array result
and stack for sorting.
*/