contraseña_correcta = "Leomaster"
contraseña_ingresada = ""

while (contraseña_ingresada != contraseña_correcta):
    contraseña_ingresada = str(input("Ingrese su contraseña, no utilice numeros: "))
    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta, intente de nuevo")
    
