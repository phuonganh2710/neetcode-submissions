class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        seen = {s[l]: 1}
        while r < len(s):
            print(r)
            maxf = self.findMax(seen)
            curLen = r-l +1
            diff = curLen - maxf
            if diff <= k:
                # valid substring
                res = max(res, curLen)
                # expand
                if r < len(s) - 1:
                    r+=1
                    seen[s[r]] = seen.get(s[r],0) +  1
                else:
                    break
            else:
                #shrink
                seen[s[l]] -=1
                l+=1
        return res


    def findMax(self, seen):
        res = 0
        for k in seen:
            res = max(res, seen[k])

        return res

        