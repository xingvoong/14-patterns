/*
Given a string a and an integer k, return the length of the longest substring of a that contains at most k distinct characters

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation:  The substring is "ece" with length 3

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation:  The substring is "aa" with length 2

Constraints:
- 1 <= s.length <= 5 * 10 ^ 4
- 0 <= k <= 50
I: string, k: number of distinct character
O: integer, the length of the longest substring
of a that contains at most k distinct characters
C:
E:  what if there is no solution?
example: s = "aa", k = 2
return 0?
*/

var lengthOfLongestSubstringKDistinct = function(s, k) {
  var n = s.length
  var right = 0
  var left = 0
  var solution = 0
  var seen = []

  while (right < n) {
    if (!seen.includes(s[right])) {
      seen.push(s[right])
    }

    while (seen.length > k) {
      solution = Math.max(solution, right - 1 - left + 1)
      left += 1
      seen.shift()
    }

    right += 1
  }
  if (k > seen.length) {
    return 0
  }
  if (k == 1) {
    return right
  }
  return solution
};

var test = function() {
  var input = [["eceba", 2], ["aa", 1], ["abcabcabc", 3]]
  var expected = [3, 2, 9]
  for(var i = 0; i < input.length; i++) {
    var actual = lengthOfLongestSubstringKDistinct(input[i][0], input[i][1])
    if (actual != expected[i]) {
      console.log(`Wrong at input: ${i}`)
      console.log(`Expected: ${expected[i]} but got ${actual}`)
      return
    }
  }
  console.log('Passed test')
}

test()