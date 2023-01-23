def print_message(width, height):
    print(f"Периметр прямоугольника, равен {2 * width + 2 * height}")


width, height = map(int, input().split())
print_message(width, height)
