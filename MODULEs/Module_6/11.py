str = input()
word = str[:str.find('h')]
word += str[str.find('h')+1:str.rfind('h')+1][::-1]
word += str[str.rfind('h'):]
print(word)