'''
You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"
Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

Output: 8

Explanation:

First Transformation (t = 1):

'a' becomes 'bc' as nums[0] == 2
'z' becomes 'ab' as nums[25] == 2
'b' becomes 'cd' as nums[1] == 2
'k' becomes 'lm' as nums[10] == 2
String after the first transformation: "bcabcdlm"
Final Length of the string: The string is "bcabcdlm", which has 8 characters.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 109
nums.length == 26
1 <= nums[i] <= 25
Question number 2 
date 14/05/2025S
'''


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def mat_mult(A, B):
            size = 26
            res = [[0]*size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res

        def mat_pow(mat, exp):
            size = 26
            res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]  # identity matrix
            while exp > 0:
                if exp % 2 == 1:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                exp //= 2
            return res

        
        trans = [[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(nums[i]):
                trans[i][(i + 1 + j) % 26] += 1

        
        final_mat = mat_pow(trans, t)

        
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        
        result = 0
        for i in range(26):
            for j in range(26):
                result = (result + freq[i] * final_mat[i][j]) % MOD

        return result