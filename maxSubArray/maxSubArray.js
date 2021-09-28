/*
Given an integter array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: 5 + 4 + (-1) + 7 + 8 = 23

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

DP solution
- go through the loop, since there are negative number:
  - either start at nums[0] or infinite negative
- if I hit a number that is greater than currentSum,
I use that number as the currentSum
- currentSum = max(currentSum, currentNumber)
- compare the currentSum with the bestSum to find the solution
*/

var maxSubArray = function(nums) {
  var bestSum = nums[0]
  var curSum = nums[0]
  for(var i = 1; i < nums.length; i++) {
    var curNum = nums[i]
    var curSum = Math.max(curNum, curNum + curSum)
    bestSum = Math.max(bestSum, curSum)
  }
  return bestSum
}

var test = function() {
  var input = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]
  var expected = [6, 1, 23]
  for(var i = 0; i < input.length; i++) {
    var actual = maxSubArray(input[i])
    if (actual != expected[i]) {
      console.log(`Wrong at input: ${i}`)
      console.log(`Expected: ${expected[i]} but got ${actual}`)
      return
    }
  }
  console.log('Passed test')
}

test()

/*
Time:  O(N), where N is the length of nums
We iterate through every element of nums exactly once.

Space complexity: O(1)
no matter how long the input is, we are only using 2 variables.

*/