#задача вынуть ключи по значению в формате "Ivan любит город Moscow и Vladivostok"
mans=[]	
favorite_places = {
	'Moscow':['ivan', 'maria', 'ibragim'],
	'Leningrad':['artem', 'sveta', 'maria'],
	'Vladivostok':['ivan', 'gendos', 'viktor'],
	}
for city, names in favorite_places.items():
	for name in names:
		print(f"{name.title()}'s favorite place is {city}.")

def get_key(d, value): #функция которая вынимает ключ по значению(не нужна)
	for k, v in d.items():
		for v1 in v:
			if v1 == value:
				return k

for names in favorite_places.values(): #тут создаем список всех имен словаря
	for name in names:
		mans.append(name)
print(mans)
	
def f(l): #функция которая убирает повторяющиеся элементы списка
	n=[]
	for i in l:
		if i not in n:
			n.append(i)
	return n
new_man=f(mans) #новый список без повторений
#тут наконец программа находит ключи по значению и выводит их
for new_man1 in new_man:
	print(f"{new_man1.title()}'s favorite place:")
	for city, names in favorite_places.items():
			if new_man1 in names:
				print(city) 
