def check_password(string, chars="$%!?@#"):
    return False if len(string) < 8 else any(char in chars for char in string)


print(check_password('12345678!'))
