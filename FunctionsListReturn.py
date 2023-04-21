#Write a Python function to return the list of words that are longer than nnn from a given list of words

#List = ["cow, pig, frog, sheep, chicken, dog, duck, bull, llama, alpaca"]

def words(n, str):
    word_len = []
    txt = str.split(",")
    for x in txt:
        if len(x.strip()) > 3:
            word_len.append(x.strip())
    return word_len
print (words(3 , "cow, pig, frog, sheep, chicken, dog, duck, bull, llama, alpaca"))
