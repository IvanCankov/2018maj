athaladas = {}
athaladasok = []
legtobben = 0
szamlalo = 0
helye = 0
with open('ajto.txt') as file:
    for index, line in enumerate(file):
        line = line.strip().split()
        athaladas['ora'] = int(line[0])
        athaladas['perc'] = int(line[1])
        athaladas['szemely'] = int(line[2])
        if 'ki' in line[3]: 
            athaladas['ki'] = True
            szamlalo -= 1
            if szamlalo > legtobben:
                legtobben = szamlalo
                helye = index
        else:
            athaladas['ki'] = False
            szamlalo += 1
            if szamlalo > legtobben:
                legtobben = szamlalo
                helye = index
        athaladasok.append(athaladas)
        athaladas = {}

print('2. feladat')
belepett_e = False
utolso_tavozo = None
for athaladas in athaladasok:
    if not athaladas['ki'] and not belepett_e:
        print(f"Az első belépő: {athaladas['szemely']}")
        belepett_e = True
    if athaladas['ki']:
        utolso_tavozo = athaladas['szemely']
print(f'Az utolsó kilépő: {utolso_tavozo}')

print('4. feladat')
bent_maradt = set()
for athaladas in athaladasok:
    if not athaladas['ki']:
        bent_maradt.add(athaladas['szemely'])
    else:
        bent_maradt.remove(athaladas['szemely'])

for line in sorted(bent_maradt):
    print(line, end=' ')

print(' ')
print('5. feladat')
print(f"{athaladasok[helye]['ora']}:{athaladasok[helye]['perc']}")

print('6. feladat')
ido = []
o = False
azonosito = int(input('adja meg a szemely azonositojat: '))
print('7. feladat')
for athaladas in athaladasok:
    if athaladas['szemely'] == azonosito and not o:
        print(f"{athaladas['ora']}:{athaladas['perc']}", end = '-')
        o = True
    elif athaladas['szemely'] == azonosito and o:
        print(f"{athaladas['ora']}:{athaladas['perc']}", end = '\n')
        o = False











hanyszor = {}
for athaladas in athaladasok:
    if athaladas['szemely'] not in hanyszor:
        hanyszor[athaladas['szemely']] = 1
    else:
        hanyszor[athaladas['szemely']] += 1

with open('athaladas.txt', 'w') as file:
    for szemely in sorted(hanyszor):
        file.write(str(szemely) + ' ' + str(hanyszor[szemely]) + '\n')
