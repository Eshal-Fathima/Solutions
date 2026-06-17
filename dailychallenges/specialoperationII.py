class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        # lengths[i] = length after processing s[:i]
        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            L = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = L + 1

            elif ch == '*':
                lengths[i + 1] = max(0, L - 1)

            elif ch == '#':
                lengths[i + 1] = L * 2

            else:  # '%'
                lengths[i + 1] = L

        if k >= lengths[n]:
            return '.'

        # Work backwards
        for i in range(n - 1, -1, -1):
            ch = s[i]

            cur_len = lengths[i + 1]
            prev_len = lengths[i]

            if 'a' <= ch <= 'z':
                # This character was appended at the end
                if k == cur_len - 1:
                    return ch

            elif ch == '*':
                # Removing last character does not affect indices < cur_len
                pass

            elif ch == '#':
                # result = old + old
                if k >= prev_len:
                    k -= prev_len

            else:  # '%'
                # result = reverse(old)
                k = prev_len - 1 - k

        return '.'