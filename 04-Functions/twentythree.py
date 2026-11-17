def f(password):
    check_string = ""
    for i in password:
        if i not in check_string:
            check_string = check_string + i
    return len(password) >= 6 and len(password) == len(check_string)
    