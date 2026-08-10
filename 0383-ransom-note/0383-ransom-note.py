class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag=list(magazine)
        for i in range(len(ransomNote)):

            if ransomNote[i] not in mag:
                return False
            else:
                mag.remove(ransomNote[i])

        return True




        