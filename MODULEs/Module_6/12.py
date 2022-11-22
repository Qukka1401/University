str = input()

f = str.find("h")
l = str.rfind("h")
new_str = list(str.replace("h", "H"))
new_str[f], new_str[l] = "h", "h"

print("".join(new_str))