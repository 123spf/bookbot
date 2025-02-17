book = "books/frankenstein.txt"

def main():
    words = get_text(book)
    #count_words(words)
    #new_variable = count_char(words)
    #print(new_variable)
    new_dict = count_char(words)
    list_dict = create_list(new_dict)
    for new in list_dict:
        if new["char"].isalpha():
            print(f"The '{new["char"]}' character was found {new["num"]} times")
        else:
            continue


def get_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def count_words(words):
    word = words.split()
    print(len(word))

def count_char(words):
    words = words.lower()
    new_dict = {}
    for word in words:
        #count = 0
        if word in new_dict:
            #continue
            new_dict[word]+= 1
        else:
            new_dict[word]=1
            #for i in range(len(words)):
             #   if word == words[i]:
              #      count += 1
               # new_dict[word]= count
    return new_dict

def sort_on(d):
    return d["num"]

def create_list(new_dict):
    list_dict = []
    for new in new_dict:
        list_dict.append({"char" : new, "num" : new_dict[new] })
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
        
main()

