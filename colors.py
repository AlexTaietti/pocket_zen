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


def get_color_code(color):
    return COLORS[color]


# layers
LAYERS = {
    'fore': 3,
    'back': 4
}


def get_layer_code(layer):
    return LAYERS[layer]


# more color data accessors and utils
def get_layer_color_code(color, layer):
    color = get_color_code(color)
    layer = get_layer_code(layer)
    return f'{layer}{color}'


def get_colors():
    return COLORS.items()


def get_layers():
    return LAYERS.items()
