from string import ascii_lowercase, digits


def is_email(email):
    chars = ascii_lowercase + digits + '_@.'
    login = ascii_lowercase + digits + '_'
    domain = ascii_lowercase + '.'

    for ch in email:
        if ch not in chars:
            return False

    lst = email.split('@')
    if len(lst) > 2:
        return False

    for ch in lst[0]:
        if ch not in login:
            return False

    for ch in lst[1]:
        if ch not in domain:
            return False

    if lst[1].count('.') > 1:
        return False

    return True


lst = list(filter(is_email, input().lower().split()))
print(*lst)
