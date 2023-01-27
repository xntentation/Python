line = 'Język Python jest najlepszy'
a = max(line.split(), key=len)          #longest_word
b = len(max(line.split(), key=len))     #longest_word_length

print('(a) - ' + str(a))
print('(b) - ' + str(b))