from math import pi
def gms(deg):
    degrees = int(deg) #целую часть градусов
    mint = int((deg-degrees) * 60)
    sec = ((((deg-degrees) * 60)- mint)*60)


def deg(deg, mint, sec):
    return deg+(mint/60)+(sec/3600)

def deg_to_rad(deg):
    return def * (pi/180)

def rad_to_deg(rad):
    return rad* (180/pi)

print(gms(36))
print(deg(36,58,12))
print(deg_to_rad(36))
print(rad_to_deg())