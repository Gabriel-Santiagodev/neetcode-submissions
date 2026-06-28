class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for i in strs:
            str_len = len(i)
            encoded_list.extend([str(str_len), "#", i])
        return "".join(encoded_list)


    def decode(self, s: str) -> List[str]:
        str_final = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            str_len = s[i:j]
            i = j + 1
            j = i + int(str_len)
            str_final.append(s[i:j])
            i = j 
        return str_final
