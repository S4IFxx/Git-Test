class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = ""
        for i in str(x):
            number += i
        if number == number[::-1]:
            return True
        else:
            return False

check = Solution()
print(check.isPalindrome(10))