failas = open('./SimpleText.txt')
nuskaitytasTekstas = failas.read()
print(nuskaitytasTekstas)
failas.close()

print('----------------------------------')
failas = open('./SimpleText.txt')
nuskaitytasTekstas = failas.read()
print('Nuskaitytas:', nuskaitytasTekstas)
print()

kitasTekstas = failas.read()
print('Kitas', kitasTekstas)

failas.close()

print('----------------------------------')
failas = open('./SimpleText.txt')
nuskaitytasTekstas = failas.read()
print('Nuskaitytas:', nuskaitytasTekstas)
print()

failas.seek(0)
perNaujo = failas.read()
print('Per naujo:', perNaujo)

failas.close()

print('----------------------------------')
with open('./SimpleText.txt') as file:
    tekstas = file.read()
    print(tekstas)

print('----------------------------------')
with open('./SimpleText.txt') as file:
    row = file.readline()
    print(row)
    row = file.readline()
    print(row)
    row = file.readline()
    print(row)

print('----------------------------------')
with open('./SimpleText.txt') as file:
    allText = file.readlines()
    print(allText)

print('----------------------------------')
with open('./SimpleText.txt') as file:
    allText = file.readlines()
    print('Visas tekstas:', allText)
    corectedText = [ row.rstrip('\n') for row in allText ]
    print('Sutvarkytas tekstas:', corectedText)

# print(' 18 pvz. ----------------------------------')
# employees = []
# with open('./Employees.txt') as file:
#     for row in file:
#         row = row.rstrip('\n')
#         splited = row.split(';')
#         employee = dict(
#             name = splited[0],
#             age = splited[1],
#             salary = splited[2],
#             employement = splited[3],
#             gender = splited[4]
#         )
#         employees.append(employee)
# print(employees)