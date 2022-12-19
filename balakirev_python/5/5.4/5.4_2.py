phone = input()

# +7(xxx)xxx-xx-xx

flag_correct = True

numbers = phone[3:6] + phone[7:10] + phone[11:13] + phone[14:16]

for p in numbers:
    if p not in '0123456789':
        flag_correct = False
        break

if len(phone) > 16 or phone[0:3] != '+7(' or phone[6] != ')' or phone[10] != '-' or phone[13] != '-':
    flag_correct = False

print('ДА' if flag_correct else 'НЕТ')
