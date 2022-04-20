# write your code here
memory = 0.0
result = 0.0
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_ = {
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
}


def calculator():
    operations = ('+', '-', '*', '/')
    global result
    while True:
        print(msg_0)
        x, oper, y = input().split()
        is_x_number, x = validate_numbers(x)
        if is_x_number is False:
            print(x)
            continue
        is_y_number, y = validate_numbers(y)
        if is_y_number is False:
            print(y)
            continue
        if oper not in operations:
            print(msg_2)
            continue
        check(x, oper, y)
        if oper == '+':  # dict?
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
        print(result)
        accept_answer_msg_4(result)


def accept_answer_msg_4(v):
    print(msg_4)
    answer = input()
    if answer == 'y':
        if is_one_digit(v) is True:
            store_result()
        elif is_one_digit(v) is False:
            global memory
            memory = v
            return memory, accept_answer_msg_5()
    elif answer == 'n':
        accept_answer_msg_5()
    else:
        return accept_answer_msg_4(v)


def accept_answer_msg_5():
    print(msg_5)
    answer = input()
    if answer == 'y':
        calculator()
    elif answer == 'n':
        exit()
    else:
        return accept_answer_msg_5()


def validate_numbers(v):
    if v == 'M':
        v = memory
    elif isfloat(v) is False:
        return False, msg_1
    return True, float(v)


def isfloat(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer() is True:
        return True
    else:
        return False


def check(x, operation, y):
    msg = ""
    if is_one_digit(x) is True and is_one_digit(y) is True:
        msg = msg + msg_6
    if (x == 1 or y == 1) and operation == '*':
        msg = msg + msg_7
    if (x == 0 or y == 0) and (operation == '*' or operation == '-' or operation == '+'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def store_result():
    msg_index = 10
    global result, memory
    while is_one_digit(result) is not False:
        print(msg_[msg_index])
        answer_2 = input()
        if answer_2 == 'y' and msg_index < 12:
            msg_index += 1
        elif answer_2 == 'n':
            accept_answer_msg_5()
        else:
            memory = result
            accept_answer_msg_5()


calculator()
