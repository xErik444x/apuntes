def l100kmtompg(litros):
    galones = litros / 3.785411784
    millas = 100 * 1000 / 1609.344
    return millas / galones
    
def mpgtol100km(millas):
    km100 = millas * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / km100


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))