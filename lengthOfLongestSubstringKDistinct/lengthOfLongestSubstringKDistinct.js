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
Takeaways:
- need a hashMap of key/value: character: last seen position
- slide window.
- move the left pointer after deleting a character: left = leftMost + 1

Algo
-	return 0 if the string is empty or k is equal to zero
-	Set both pointers in the beginning of the string left = 0 and right = 0 and init max substring length max_len = 1
-	While right pointer is less than N:
o	Add the current character s[right] in the hashmap and move right pointer to the right.
o	If hashmap contains k + 1 distinct characters,
  - remove the left most character (the one have the smallest index) from the hashmap and move the left pointer so that sliding window contains again k distinct characters only
    - aka: left = leftMost + 1
o	Update max_len
*/

var lengthOfLongestSubstringKDistinct = function(s, k) {
  var n = s.length
  var right = 0
  var left = 0
  var solution = 0
  var seen_lastPosition = {}

  if (s.length == 0 || k == 0) {
    return 0
  }

  while (right < n) {
    var character = s[right]
    seen_lastPosition[character] = right

    if (Object.keys(seen_lastPosition).length > k) {
      var leftMost = n + 1
      var toDelete = undefined
      for (var key in seen_lastPosition) {
        if (seen_lastPosition[key] < leftMost) {
          leftMost = seen_lastPosition[key]
          toDelete = key
        }
      }
      delete seen_lastPosition[toDelete]
      left = leftMost + 1
    }
    solution = Math.max(solution, right - left + 1)
    right += 1
  }

  return solution
};

var test = function() {
  var input = [["eceba", 2], ["aa", 1], ["abcabcabc", 3], ["a", 1], ["aa", 2], ["abaccc", 2]]
  var expected = [3, 2, 9, 1, 2, 4]
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

/*
Runtime:  O(kN)
- need to find leftMost to delete
- can be improve if the hashMap is ordered.
Space: O(k)
- for hasMap
*/