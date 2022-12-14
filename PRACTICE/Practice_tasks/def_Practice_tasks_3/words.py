from manager import locked_symbol

def lock_word(word: str) -> str:
    word_list: list = [a for a in word]
    output: str = ''
    for i in range(0, len(word)):
        word_list[i] = locked_symbol
    return output.join(word_list)

def unlock_part_of_word(un_word: str, locked_word: str, part: str) -> str:
    all_part_indexs: list = []

    locked_word_list: list = [a for a in locked_word]
    output: str = ''
    for i in range(0, len(un_word)):
        if un_word[i] == part:
            all_part_indexs.append(i)
    for j in all_part_indexs:
        locked_word_list[j] = part
    return output.join(locked_word_list)