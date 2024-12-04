calls = 0

def count_calls():
    global calls
    calls+=1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

#print(string_info('Capibara'))
#print(string_info('Armageddon'))
#print(is_contains('Urban', ['ban', 'BaNaN', 'urBan'])) #Urban~urBan
#print(is_contains('cicle', ['recicling', 'ciclic'])) #Nomatches
#print(calls)

print(string_info('Andromeda'))
print(string_info('Mercab'))
print(is_contains('Mercab', ['cab', 'cabMer', 'Marcar']))
print(is_contains('cicle', ['recicling', 'ciclic']))
print(calls)
