line = 'Język Python jest najlepszy'
words_in_line = line.split()

print('Wyrazy posortowane alfabetycznie - ' + str(sorted(words_in_line, key=str.lower)))
print('Wyrazy posortowane pod względem dlugości - ' + str(sorted(words_in_line, key=len)))