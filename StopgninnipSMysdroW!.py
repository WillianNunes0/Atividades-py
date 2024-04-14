# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    sentence_final = ''
    sentence_split = sentence.split()
    for palavra in sentence_split:
        if len(palavra) >= 5:
            palavra_invertida = palavra[::-1]
            sentence_final += f'{palavra_invertida} '
        else:
            sentence_final += f'{palavra} '
    
    return sentence_final[:-1]


print(spin_words('Hey fellow warriors'))