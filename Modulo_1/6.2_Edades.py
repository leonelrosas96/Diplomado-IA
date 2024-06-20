edad = float(input("Introduce edad de la persona: "))

if edad < 13:
    print('Niño')
elif edad < 18:
    print('Adolescente')
elif edad < 65:
    print('Adulto')
else: 
    print('Adulto Mayor')
