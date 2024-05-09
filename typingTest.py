import random
import time

with open('/full_path_to_/words.txt') as file:
	data = file.readlines()

counter = 0
letters = 0
wrong_letters=0

t = int(time.perf_counter())

while int(time.perf_counter()) - t <= 60:
	#print('\033c')
		
	i = random.randint(0,len(data))
	j = random.randint(0,10) # adding 20% capitals 

	if j <= 1:
		try:
			d = data[i].title()
		except:
			d = data[i]
	else:
		d = data[i] 

	d = d.strip('\n')
	
	print(d, end='\r')

	word = input()
	#print('\033c')
	#os.system('clear')
	
	k=0
	if word != d:
		for i in d:
			try:
				if i == word[k]:
					letters+=1
				else:
					wrong_letters+=1
				k+=1
			except:
				letters+=0	
		
		#print('wrong')
		
	else:
		letters +=len(d)
		counter+=1

print('Words: ' + str(counter))
print('Correct Letters: ' + str(letters))
print('Misspells: ' + str(wrong_letters))
