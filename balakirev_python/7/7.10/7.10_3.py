def add_tag():
    def func(s):
        return f"<h1>{s}</h1>"

    return func


f = add_tag()
print(f(input()))
