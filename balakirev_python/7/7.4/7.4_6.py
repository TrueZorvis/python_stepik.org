def get_html(string, tag='h1', up=True):
    tag = tag.upper() if up else tag.lower()
    return f"<{tag}>{string}</{tag}>"


str_in = input()
print(get_html(str_in, tag='div'))
print(get_html(str_in, tag='div', up=False))
