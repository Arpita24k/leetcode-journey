class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        cnt = [0] * 10  # digit balance 0..9

        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                s = int(s_ch)
                g = int(g_ch)

                if cnt[s] < 0:  # unmatched g==s seen before
                    cows += 1
                if cnt[g] > 0:  # unmatched s==g seen before
                    cows += 1

                cnt[s] += 1
                cnt[g] -= 1

        return f"{bulls}A{cows}B"
