from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
overpass = Overpass()
#, '"building"="apartments"', '"building"="service"', '"building"="school"', '"building"="kindergarten"', '"building"="industrial"'

list_txts = ['yes', 'apartments', 'service', 'school', 'kindergarten', 'industrial']
x1 = input('Input bottom number: ')
y1 = input('Input left number: ')
x2 = input('Input top number: ')
y2 = input('Input right number: ')
for i in range(1,7):
	exec(f'query{i} = overpassQueryBuilder(bbox=[{x1}, {y1}, {x2}, {y2}], elementType=\'way\', selector=\'"building"="{list_txts[i-1]}"\', out=\'body\')')
	exec(f'yestxt{i} = open(\'{list_txts[i-1]}.txt\', \'w\', encoding=\'utf-8\')')
	exec(f'yestxt{i}.write("")')
	exec(f'result{i} = overpass.query(query{i})')
	exec(f'res_{i} = 0')

for item in result1.elements():
	try:
		if item.tags()['building:levels'] != '0':
			pass
	except Exception:
		#print(item.tags())
		res_1 += 1
		r_write = ''
		try:
			r_write = item.tags()['addr:street'] + ' ' + item.tags()['addr:housenumber'] + '\n'
			yestxt = open('yes.txt', 'a', encoding='utf-8')
			yestxt.write(r_write)
		except Exception:
			pass
for item in result2.elements():
	try:
		if item.tags()['building:levels'] != '0':
			pass
	except Exception:
		#print(item.tags())
		res_2 += 1
		r_write = ''
		try:
			r_write = item.tags()['addr:street'] + ' ' + item.tags()['addr:housenumber'] + '\n'
			yestxt = open('apartments.txt', 'a', encoding='utf-8')
			yestxt.write(r_write)
		except Exception:
			pass
for item in result3.elements():
	try:
		if item.tags()['building:levels'] != '0':
			pass
	except Exception:
		#print(item.tags())
		res_3 += 1
		r_write = ''
		try:
			r_write = item.tags()['addr:street'] + ' ' + item.tags()['addr:housenumber'] + '\n'
			yestxt = open('service.txt', 'a', encoding='utf-8')
			yestxt.write(r_write)
		except Exception:
			pass
for item in result4.elements():
	try:
		if item.tags()['building:levels'] != '0':
			pass
	except Exception:
		#print(item.tags())
		res_4 += 1
		r_write = ''
		try:
			r_write = item.tags()['addr:street'] + ' ' + item.tags()['addr:housenumber'] + '\n'
			yestxt = open('school.txt', 'a', encoding='utf-8')
			yestxt.write(r_write)
		except Exception:
			pass
for item in result5.elements():
	try:
		if item.tags()['building:levels'] != '0':
			pass
	except Exception:
		#print(item.tags())
		res_5 += 1
		r_write = ''
		try:
			r_write = item.tags()['addr:street'] + ' ' + item.tags()['addr:housenumber'] + '\n'
			yestxt = open('kindergarten.txt', 'a', encoding='utf-8')
			yestxt.write(r_write)
		except Exception:
			pass
for item in result6.elements():
	try:
		if item.tags()['building:levels'] != '0':
			pass
	except Exception:
		#print(item.tags())
		res_6 += 1
		r_write = ''
		try:
			r_write = item.tags()['addr:street'] + ' ' + item.tags()['addr:housenumber'] + '\n'
			yestxt = open('industrial.txt', 'a', encoding='utf-8')
			yestxt.write(r_write)
		except Exception:
			pass

print(f'Building = yes          =  {result1.countElements()}, without height = {res_1}')
print(f'Building = apartments   =  {result2.countElements()}, without height = {res_2}')
print(f'Building = service      =  {result3.countElements()}, without height = {res_3}')
print(f'Building = school       =  {result4.countElements()}, without height = {res_4}')
print(f'Building = kindergarten =  {result5.countElements()}, without height = {res_5}')
print(f'Building = industrial   =  {result6.countElements()}, without height = {res_6}')
print('Sum of all  =  ' + str(int(result1.countElements())+int(result2.countElements())+int(result3.countElements())+int(result4.countElements())+int(result5.countElements())+int(result6.countElements())))
print('Sum of only without height  =  ' + str(int(res_1+res_2+res_3+res_4+res_5+res_6)))
