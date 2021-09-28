/*
Algo:
- a hashmap for frequency, only store k distinct character.
- go through the string
- while left < right and seen.keys.length > k:
  - decrease the frequency of the left windown
  - if the frequency is 0: remove the character
*/

var lengthOfLongestSubstringKDistinct = function(s, k) {
  var n = s.length
  var right = 0
  var left = 0
  var solution = 0
  // frequency hashmap
  var seen = {}
  while (right < s.length) {
    if (seen[s[right]] === undefined) {
      seen[s[right]] = 1
    } else {
      seen[s[right]] += 1
    }

    while (left <= right && Object.keys(seen).length > k) {
      var leftChar = s[left]
      seen[leftChar] -= 1
      if (seen[leftChar] === 0) {
        delete seen[leftChar]
      }
      left += 1
    }

    solution = Math.max(solution, right - left + 1)
    right +=  1
  }
  return solution
}

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