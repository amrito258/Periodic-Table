import json

element = input('Enter element name: ')
element = element.capitalize()

print(f'What do you want to know about {element}?')
print('''
1. Atomic Number
2. Symbol
3. Atomic Mass
4. Electron Configuration
5. Group Number
6. Density
7. Melting Point
8. Boiling Point
9. Discoverer
10. The Nomenclature
11. Appearance
12. Summary''')

term = input('Enter the number: ')
file = json.loads(open('elements.json', 'r').read())

if '1' in term:
  info = file[element]['atomic_number']
  print(f'The atomic number of {element} is {info}')

elif '2' in term:
  info = file[element]['symbol']
  print(f'The symbol of {element} is {info}')

elif '3' in term:
  info = file[element]['atomic_mass']
  print(f'The atomic mass of {element} is {info}')

elif '4' in term:
  info = file[element]['electron_configuration']
  print(f'The electron configuration of {element} is {info}')

elif '5' in term:
  info = file[element]['group']
  print(f'The group number of {element} is {info}')

elif '6' in term:
  info = file[element]['density']
  print(f'The density of {element} is {info} g/m³')

elif '7' in term:
  info = file[element]['melting_point']
  print(f'The melting point of {element} is {info} °C')

elif '8' in term:
  info = file[element]['boiling_point']
  print(f'The boiling point of {element} is {info} °C')

elif '9' in term:
  info = file[element]['discovered_by']
  print(f'The discoverer of {element} is {info}')

elif '10' in term:
  info = file[element]['named_by']
  print(f'{element} is named by {info}')

elif '11' in term:
  info = file[element]['appearance']
  print(f'Appearance of {element}: {info}')

elif '12' in term:
  info = file[element]['summary']
  print(f'Summary of {element}: {info}')