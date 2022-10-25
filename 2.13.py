line = 'Język Python jest najlepszy'
words_in_line = line.split()
words_in_line_length = [len(word) for word in words_in_line]

print ('Suma długości wyrazów w wierszu wynosi - ' + str(sum(words_in_line_length)))
