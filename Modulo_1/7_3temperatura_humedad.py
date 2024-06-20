
# Inicializar contador

contador = 0

while contador < 3:
    temperatura = float(input('Ingrese la temperatura: '))
    humedad = float(input('Ingrese la humedad: '))

    if temperatura > 30:
        if humedad >= 30:
            accion = 'Se recomienda ventilación'
        else:
            accion = 'Se recomienda Riego y ventilacion'
    else:
        if humedad < 30:
            accion = "Se recomienda riego"
        else:
            accion = "No se necesita accion"
    
    print(accion)

    contador += 1
