from datetime import datetime


def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    td = int((t1 - t2).total_seconds())
    if td <= 0:
        td *= -1
    return td

