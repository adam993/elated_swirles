import random

kolone = ['Blood color', 'Flow days', 'Indication']

values_bloodcolor = ['normal red', 'brown red', 'dark red', 'light red']
values_flowdays = [1, 2, 3, 4]
values_indication = ['healthy', 'anemia', 'anorexia', 'Hypothyroidism']

file = open("data.txt", "w")

s = ""
for a in kolone:
	s+=a
	s+=','

s = s[:-1] #remove last char
s+='\n'
file.write(s)

for i in range(0,300): 
	s=""
	s += random.choice(values_bloodcolor)
	s +=','
	s += str(random.choice(values_flowdays))
	s +=','
	s += random.choice(values_indication)
	s +='\n'
	file.write(s)

file.close()
