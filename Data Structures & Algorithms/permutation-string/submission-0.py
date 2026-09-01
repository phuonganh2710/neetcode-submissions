class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_s1 = [0 for _ in range(26)]
        freq_s2 = [0 for _ in range(26)]

        
        for s in s1:
            freq_s1[ord(s)-ord('a')] += 1
        
        l = 0
        r = len(s1) - 1
        i = l
        while i <= r:
            freq_s2[ord(s2[i]) - ord('a')] += 1
            i+=1
        

        while r < len(s2):
            if freq_s2 == freq_s1:
                return True
            
            freq_s2[ord(s2[l]) - ord('a')] -= 1
            l+=1
            r+=1
            if r < len(s2):
                freq_s2[ord(s2[r]) - ord('a')] += 1

        
        #print(freq_s1)
        return False