def get_data_fig(*args, **kwargs):
    _vals = [sum(args)] + [kwargs[arg] for arg in ['type', 'color', 'closed', 'width'] if arg in kwargs]
    return tuple(_vals)


print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))
