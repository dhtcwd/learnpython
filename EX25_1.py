import EX25
sentence = "All good things come to those who wait."

words = EX25.break_words(sentence)
print words

sorted_words = EX25.sort_words(words)
print sorted_words

EX25.print_first_word(words)
EX25.print_last_word(words)
EX25.print_first_word(sorted_words)
EX25.print_last_word(sorted_words)

sorted_words = EX25.sort_sentence(sentence)
print sorted_words

EX25.print_first_and_last(sentence)
EX25.print_first_and_last_sorted(sentence)

