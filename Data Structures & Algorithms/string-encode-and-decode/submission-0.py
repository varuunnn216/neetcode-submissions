class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for current_str in strs:
            str_length = len(current_str)
            encoded_str += str(str_length) + "#" + current_str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        pointer = 0

        while pointer < len(s):
            hash_position = s.find("#", pointer)
            str_length = int(s[pointer:hash_position])

            str_start = hash_position + 1
            str_end = str_start + str_length
            current_str = s[str_start:str_end]

            decoded_strs.append(current_str)

            pointer = str_end
        return decoded_strs
