salario = float(input("Introduzca cantidad de salario en $ mxn: "))
edad = int(input("Introduzca su edad: "))

if salario <= 20000:
    if edad < 18:
        print("Exento de impuestos")
    else:
        print("Pague 5% de impuestos")
        print(salario * 0.05)
else:
    if salario <= 50000:
        print("Pague 10% de impuestos")
        print(salario * 0.10)
    else:
        print("Pague 20% de impuestos")
        print(salario * 0.2)

