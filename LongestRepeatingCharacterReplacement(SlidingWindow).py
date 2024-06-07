class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(0, len(s)):
            count[s[r]] += 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] += count.get(s[l], 0) - 1
            res = max(res, r - l + 1)
        return res