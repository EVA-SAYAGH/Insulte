colors = {
    'red': '\x1b[1;31m',
    'green': '\x1b[1;32m',
    'yellow': '\x1b[1;33m',
    'blue': '\x1b[1;34m',
}

def print_with_color(message, color):
    """
    This function is called when we want to print with a requested color
    """
    if color in colors:
        print(colors[color] + message + '\x1b[0m')
    else:
        print(message)
