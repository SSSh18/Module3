def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower and root_word_lower != word_lower:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Able', 'Disablement', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('colour', 'Discolour', 'column', 'colourist', 'colourful')
print(result1)
print(result2)
print(result3)

