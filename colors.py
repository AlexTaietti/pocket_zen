# color codes
COLORS = {
    'black': 0,
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7
}

LAYERS = {
    'fore': 3,
    'back': 4
}


def _get_color_code(color, layer):
    color = COLORS[color]
    layer = LAYERS[layer]
    return f'{layer}{color}'


def get_foreground_color(color):
    color_code = _get_color_code(color, 'fore')
    return color_code


def get_background_color(color):
    color_code = _get_color_code(color, 'back')
    return color_code
