from datetime import datetime


def current_date(s_date):
    day = datetime.strptime(s_date, "%m %d %Y").strftime("%A").upper()
    print(day)


if __name__ == '__main__':
    s_date = input()
    current_date(s_date)
