import Practic_3
def create_list(*args, **kwargs):
    c = []
    for i in range(len(args)):
        c.append(f"Point_{i} = {Practic_3.gms(args[i])}")
    for k, val in kwargs.items():
        c.append(f"{k} = {Practic_3.gms(val)}")
    return c

print(create_list(12.9801, 35.1273, 162.0873, pole=15.3842, put=169.0521))