def main():    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def num_words(text):
    words = text.split()
    print (f"{len(words)} words found in the document")


num_words(main())