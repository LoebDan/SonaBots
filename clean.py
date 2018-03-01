x = 'SONA180222.txt'
sorted = []
file = open(x, 'rt')
with open(x) as f:
    for line in f.readlines():
       temp = line[(line.index(' ')+1):]
       temp =  temp[:temp.rindex(' ')]
       temp = temp.title()
       temp = temp.replace((" "), '')
       if(temp[0] != "#"):
           temp = "#" + temp
       sorted.append(temp)
f.close()
file = open(x, 'w')
for item in sorted:
    file.write("%s\n" % item)
file.close