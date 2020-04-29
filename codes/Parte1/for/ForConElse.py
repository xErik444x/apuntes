#cuando el for llegue a 4, este va a ir al else

for i in range(5):
    print(i)
else:
    print("else:", i)

#En este caso no va a pasar por el for y va directo al else
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i) 