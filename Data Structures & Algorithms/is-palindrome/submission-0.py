class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        newS = []
        for letter in st:
            if not letter.isalnum() or letter == " ":
                continue
            newS.append(letter)
        i, j = 0, len(newS) - 1
        while i < j:
            if newS[i] != newS[j]:
                return False
            i+=1
            j-=1
        return True