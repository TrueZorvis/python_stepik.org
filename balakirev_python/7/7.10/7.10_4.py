def add_tag(tag):
    def func(s):
        return f"<{tag}>{s}</{tag}>"

    return func


f = add_tag(input())
print(f(input()))
