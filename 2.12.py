line = "Język Python jest najlepszy"
first_characters = [x[0] for x in line.split()]
last_characters = [x[-1] for x in line.split()]

print('To są piersze litery wyrazów w wierszu - ' + str("".join(first_characters)))
print('To są ostatnie litery wyrazów w wierszu - ' + str("".join(last_characters)))





#print( list(x)[:2]) #dwa pierwsze znaki
#print( list(x)[2:]) #dwa ostatnie znaki
#+ str(line[1][:1]) + str(line[2][:1]) + str(line[-1][:1])
