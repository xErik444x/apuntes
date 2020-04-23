#si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
min += dura #cantidad de minutos
print(min)
hora = hora + min // 60
print(hora)
min %= 60
hora %= 24
print(hora, ":", min, sep='')
