# -*- coding: utf-8 -*-


def is_positive_number(integer_str_value):
    try:
        copy = int(integer_str_value)

        if copy > 0:
            return True

    except ValueError:
        return False

def get_factorial_value(integer_value):
    result=1
    if integer_value == 1:
        return result
    else :
        result = integer_value * get_factorial_value(integer_value-1)
    # ==================================
    return result

def main():
    user_input = 999
    # ===Modify codes below=============
    while(user_input != 0):
        user_input = input("Input a positive number : ")
        value = is_positive_number(user_input)
        if value == True:
            user_input = int(user_input)
            cost = get_factorial_value(user_input)
            print("%d\n" % cost)
        else :
            if user_input == '0':
                print("Thank you for using this program\n")
                break
            else:
                print("Input again, Please\n")
    else:
        print("Thank you for using this program\n")

#================================
if __name__ == "__main__":
    main()
