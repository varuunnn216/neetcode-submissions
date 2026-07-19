class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left_pointer = 0
        max_freq = 0
        longest_valid_window = 0

        for right_pointer in range(len(s)):
            current_char = s[right_pointer]
            char_count[current_char] = char_count.get(current_char, 0) + 1

            max_freq = max(max_freq, char_count[current_char])

            window_len = right_pointer - left_pointer + 1
            characters_needing_replacement = window_len - max_freq

            if characters_needing_replacement > k:
                left_char = s[left_pointer]
                char_count[left_char] -= 1
                left_pointer += 1

            longest_valid_window = right_pointer - left_pointer + 1

        return longest_valid_window
        