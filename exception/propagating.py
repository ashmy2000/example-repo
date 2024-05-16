def get_day(user_info):
    try:
        day = int(input("enter day"))
        user_info.append(day)
    except:
        print("get_day")

def get_month(user_info):
    month = int(input("enter month"))
    user_info.append(month)

def get_year(user_info):
    year = int(input("enter year"))
    user_info.append(year)


def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print(f"so you're bday is {user_info}")
    except:
        print("get_user_info")


get_user_bday([])