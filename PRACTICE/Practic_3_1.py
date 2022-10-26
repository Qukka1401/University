import Practic_3
def create_list(*args, **kwargs):
    r = []
    for idx, val in enumerate(args):
        r.append(f"Point_{idx} = {Practic_3.gms(val)}")

    for k, v in kwargs.items():
        r.append(f"{k} = {Practic_3.gms(v)}")
    return r


print(
    create_list(
        172.25899161,
        321.42304971,
        12.697987681352,
        pole=21.89617856,
        put_1=140.85706440,
    )
)