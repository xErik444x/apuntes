ingreso=float(input("Ingrese el ingreso anual:"))


if ingreso < 85528:
    porcentaje = ingreso * 18 /100
    impuesto = porcentaje - 556.2
    if impuesto < 0:
        impuesto = 0
else:
    ex = ingreso - 85528
    ex = ((ex * 32)/ 100)
    impuesto = 14839.2  + ex
    

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
