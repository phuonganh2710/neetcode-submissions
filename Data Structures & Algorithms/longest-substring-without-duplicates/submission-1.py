class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        seenChar = set()
        while r < len(s):
            # check if next char is valid or should we reset our seq
            if s[r] in seenChar:
                # shrink by moving l up til char == s[r]
                while s[l] != s[r]:
                    seenChar.remove(s[l])
                    l+= 1
                l+=1
            else:
            
                # assume here both l,r are valid
                # so calculate curLen
                curLen = r - l + 1
                
                # check if curLen better than max
                if curLen > maxLen:
                    maxLen = curLen

                seenChar.add(s[r])

            # now, advance forward
            r+=1

                

        return maxLen
    
        