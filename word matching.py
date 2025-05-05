def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(words)>1 and word[0]== word[-1]:
            ctr+=1
            lst.append(word)

    print("list of words withe the first and last letterbeing the same\n", lst)
    return ctr

count=match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("number of words having the same first and last letter is", count)