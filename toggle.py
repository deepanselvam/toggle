class ToggleStringconversion:
    def toggle(self, str):
        str1 = ""
        for i in range(len(str)):
            str1 += chr(ord(str[i]) ^ (1 << 5))
        return str1

str = input()
tt = ToggleStringconversion()
print(tt.toggle(str))
