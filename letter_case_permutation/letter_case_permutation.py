'''
given a string s, can you transform every letter individually to be lowercase or uppoercase to create another string

return a list of all possible strings we could create.  Return the outout in any order

example 1:
Input: s = "a1b2"
Output: ["a1b2", "a1b2", "A1b2", "A1B2"]

exampl 2:
input: "3z4"
output: ["3z4", "3Z4"]

backtracking template

def backtracking(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    #iterate all possible candidates
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):

            # place
            place(next candidate)

            # explore
            backtracking(next_candidate)

            # backtrack
            remove(next_candidate)

'''
'''

- make all lowercase
- use backtracking:
    the goal is to create string that match,
    the length of the input string.
    Also, be able to permutae the solution

- place

- explore

- remove
always place, always explore
alternate between lowercase and uppercase depend on whether the current s is
lowercase of uppercase
'''

def letterCasePermutation(s):
    result = []
    n = len(s)
    s = s.lower()

    def backtracking(start, cur_permutation):
        # if string meets the condition
        # output the result
        if len(cur_permutation) == n:
            result.append(cur_permutation)

        # iterate all possible solution
        for i in range(start, n):

            # alternate between lowercase and uppercase
            if s[i].islower():
                backtracking(i+1, cur_permutation + s[i].upper())
            backtracking(i + 1, cur_permutation + s[i])

    backtracking(0, "")
    return result


print(letterCasePermutation("a1b2"))
print(letterCasePermutation("3z4"))


'''
runtime: O(N * 2**N):

2**n: number of subset, N to create a new string

space: O(N * 2**N)

'''