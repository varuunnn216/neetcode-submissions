class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need_count = {}

        for char in t:
            need_count[char] = need_count.get(char, 0) + 1

        char_needed = len(need_count)
        char_satisfied = 0

        window_count = {}
        lp = 0

        best_length = float("inf")
        best_left = 0

        for rp in range(len(s)):
            right_char = s[rp]
            window_count[right_char] = window_count.get(right_char, 0) + 1

            if right_char in need_count and window_count[right_char] == need_count[right_char]:
                char_satisfied += 1
            
            while char_satisfied == char_needed:
                current_length = rp - lp + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = lp

                left_char = s[lp]
                window_count[left_char] -= 1

                if left_char in need_count and window_count[left_char] < need_count[left_char]:
                    char_satisfied -= 1
                
                lp += 1

        if best_length == float("inf"):
            return ""
        return s[best_left : best_left + best_length]
        