
is_running = True
startin_year = 1400
starting_month = 1
starting_day = 1

class User:
    def __init__(self, name):
        self.user_name = name
        self.car_list = []
        self.penalty_amount = 0
        self.balance_amount = 0
        self.license_day_count = 1


def day_counter(date):
    weekdays = ["Sat", "Sun", "Mon", "Tues", "Wed", "Thurs", "Fri"]
    year, month, day = date.split("/")
    a = int(year) - startin_year
    b = int(month)+a*12-starting_month
    c = int(day)+b*30 - starting_day
    i = 0
    j = 0
    day = ""
    while j <= c:
        day = weekdays[i]
        i += 1
        if i == len(weekdays):
            i = 0
        j += 1
    return day

def day_checker(day):
    if day in ["Sat", "Mon", "Wed"]:
        return "even_day"
    elif day in ["Sun", "Tues", "Thurs"]:
        return "odd_day"
    else:
        return "friday"


def car_number_checker(car_number):
    if int(car_number) % 2 == 0:
        return "is_even"
    else:
        return "is_odd"


user_list = []
car_number_list = []
car_dict = {}

while is_running:
    command, *data = input().split()

    if command == "REGISTER":
        for user in user_list:
            if data[0] == user.user_name:
                print("INVALID USERNAME")
                break
        else:
            print("REGISTER DONE")
            user_list.append(User(data[0]))

    elif command == "REGISTER_CAR":
        for user in user_list:
            car_dict.update({user.user_name: user.car_list})

        if data[0] not in car_dict.keys():
            print("INVALID USERNAME")
        elif data[1] in car_number_list:
            print("INVALID CAR PLATE")
        else:
            for user in user_list:
                if data[0] == user.user_name:
                    user.car_list.append(data[1])
                    car_number_list.append(data[1])
                    print("REGISTER CAR DONE")
                    break

    elif command == "NEW_RECORD":
        if data[0] not in car_number_list:
            print("INVALID CAR PLATE")
        else:
            day = day_checker(day_counter(data[1]))
            number = car_number_checker(data[0])
            
            
            if (number == "is_even" and day == "even_day") or day == "friday":
                print("NORMAL RECORDED")
            elif (number == "is_odd" and day == "odd_day") or day == "friday":
                print("NORMAL RECORDED")
            else:
                for user in user_list:
                    if data[0] in user.car_list:
                        print("PENALTY RECORDED")
                        user.penalty_amount += 100
    elif command == "BUY_LICENSE":
        for user in user_list:
            if data[0] == user.user_name:
                print("INVALID USERNAME")
                break
            elif data[1] not in car_number_list:
                print("INVALID CAR PLATE")
                break
            elif user.user_name == data[0] and user.balance_amount < 70:
                print("NO ENOUGH MONEY")
                break
            else:
                print("BUY LICENSE DONE")
                
    elif command == "ADD_BALANCE":
        if data[0] not in car_dict.keys():
            print("INVALID USERNAME")
        else:
            for user in user_list:
                if data[0] == user.user_name:
                    user.balance_amount += int(data[1])
                    print("ADD BALANCE DONE")
                    break
    elif command == "GET_BALANCE":
        if data[0] not in car_dict.keys():
            print("INVALID USERNAME")
        else:
            for user in user_list:
                if data[0] == user.user_name:
                    print(user.balance_amount)
                    break
    elif command == "GET_PENALTY":
        if data[0] not in car_dict.keys():
            print("INVALID USERNAME")
        else:
            for user in user_list:
                if data[0] == user.user_name:
                    print(user.penalty_amount)
                    break
    elif command == "GET_LICENSE_DEADLINE":
        pass

    elif command.upper() == "END":
        is_running = False
