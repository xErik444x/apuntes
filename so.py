import platform as pl
import psutil as ps
import math
def convert_size(size_bytes): 
    if size_bytes == 0: 
        return "0B" 
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB") 
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i) 
    size = round(size_bytes / power, 2) 
    return "%s %s" % (size, size_name[i])


print("---"*20)
print("Windows: ",pl.platform())
print("CPU: ",pl.processor())
print("Nombre: ",pl.node())
print("Ram: ",convert_size(ps.virtual_memory()[0]))
print("---"*20)



