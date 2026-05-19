def word_replacement():
    str="Hey huyz!Hello how are you? hey hey hey hey"
    word_to_replace=input("Enter a word to replace: ")
    replace_word=input("Enter a replace word: ")
    print(str.lower().replace(word_to_replace,replace_word))

word_replacement()