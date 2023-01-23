from string import ascii_lowercase, ascii_uppercase, digits


def verify_email(email: str):
    symbols = ascii_lowercase + ascii_uppercase + digits + '_@.'
    correct = True
    if email.count('@') != 1 or email.count('.') != 1:
        correct = False

    for char in email:
        if char not in symbols:
            correct = False
            break

    print("ДА" if correct else "НЕТ")


email_in = input()
verify_email(email_in)
