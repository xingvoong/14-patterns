/*
:Given an integer array nums sorted in non-decreasing order
return an array of the squares of each : number sorted in non-decreasing order



Example 1:
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation:  After squaring, the array becomes [16, 1, 0, 9, 100].
After sorting, it becomes [0, 1, 9, 16, 100].

Example 2:
Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Constraints:
- 1<= nums.length <= 10 ^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order

Follow up: squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
*/

var sortedSquares = function(nums) {
  var n = nums.length
  result = new Array(n);
  var right = n - 1
  var left = 0
  for(var i = result.length - 1; i > -1; i--) {
    var toSquare = nums[right]

    if (Math.abs(nums[left]) < Math.abs(nums[right])) {
      right -= 1
    } else {
      toSquare = nums[left]
      left += 1
    }
    result[i] = toSquare * toSquare
  }

  return result
};

var test = function() {
  var input = [[-3, -2, -1, 4, 5, 6], [-7,-3,2,3,11]]
  var expected = [[1, 4, 9, 16, 25, 36 ], [4,9,9,49,121]]
  for(var i = 0; i < input.length; i++) {
    var actual = sortedSquares(input[i])
    if (actual.reduce((a, b) => a && expected[i].includes[b]), false) {
      console.log(`Wrong at input: ${i}`)
      console.log(`Expected: ${expected[i]} but got ${actual}`)
      return
    }
  }
  console.log('Passed test')
}

test()

/*
Solution with 2 pointers
runtime: O(n)
a for loop that loops through the array
space: O(n)
the result array
*/

