def get_html(string, tag='h1'):
    return f"<{tag}>{string}</{tag}>"


str_in = input()
print(get_html(str_in))
print(get_html(str_in, tag='div'))
