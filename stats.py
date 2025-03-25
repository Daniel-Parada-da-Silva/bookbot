def get_num_words(contents):
    words = contents.split()
    return len(words)

def count_characters(contents):
    dic = {}
    for cha in contents:
        ch = cha.lower()
        is_char_in_dic = ch in dic
        if is_char_in_dic == True:
            dic[ch] += 1
        else:
            dic[ch] = 1
    
    return dic

dic = {"char" : "e", "times" : 10}