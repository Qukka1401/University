from math import pi
def gms(deg):
    '''
    :param degrees: Грудусы в десятичном представлении
    :return: Градусы, минуты, секунды
    '''
    degrees = int(deg) #целую часть градусов
    mint = int((deg-degrees) * 60)
    sec = ((((deg-degrees) * 60) - mint) * 60)
    sec = round(sec,5)
    return f"{degrees}° {mint}′ {sec}″"

def deg(deg, mint, sec):
    '''
    :param deg: Градусы
    :param mint: Минуты
    :param sec: Секунды
    :return: Градусы в десятичном представлении
    '''
    return deg+(mint/60)+(sec/3600)

def deg_to_rad(deg):
    '''
    :param deg: Градусы
    :return: Радианы
    '''
    return deg * (pi/180)

def rad_to_deg(rad):
    '''
    :param rad: Радианы
    :return: Градусы в десятичном представлении
    '''
    return rad* (180/pi)

if __name__ == "__main__":
    print(__name__)

    print(gms(36.97))
    print(deg(36, 58, 12))
    print(deg_to_rad(36.97))
    print(rad_to_deg(0.6452482244623036))
    print((dir()))