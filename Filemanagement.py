def replace_word(change,new):
    name_to_change = str(change)
    name_new = str(new)
    with open("practice.txt" , "r") as f:
        content = f.read()
    content = content.replace(name_to_change , name_new)
    
    with open("practice.txt" , "w") as f:
        f.write(content)
        return content
def read():
    with open("practice.txt","r") as f:
        content = f.read()
        return content

def search_word(name_word):
    line_count = 0
    word = name_word
    with open("practice.txt", "r") as f:
        content = f.read()
        for content in f:
            line_count += 1
            if word in content:
                print(f"'{word}' found at line number: {line_count}")
                return line_count
    print(f"'{word}' not found in file")
    return
function_perform = input("Enter 's' to search a word or 'r' to replace a word or 'R' to read the file: ")
if function_perform == 'r':
    change = input("Enter the word to be replaced: ")
    new = input("Enter the new word: ")
    new_data = replace_word(change , new)
    print(new_data)
elif function_perform == 's':
    name_word = input("Enter the word to be searched: ")
    line_num = search_word(name_word)
    print(line_num)
elif function_perform == "R":
    reading = read()
    print(reading)
else:
    print("Invalid input")
