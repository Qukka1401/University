s = input()
dl = len(s)
print(s[dl//2 + dl%2 :] + s[: dl//2 +dl%2])