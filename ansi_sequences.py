import constants

# color codes
COLORS = {
    constants.BLACK: 0,
    constants.RED: 1,
    constants.GREEN: 2,
    constants.YELLOW: 3,
    constants.BLUE: 4,
    constants.MAGENTA: 5,
    constants.CYAN: 6,
    constants.WHITE: 7
}

# layers
LAYERS = {
    constants.FOREGROUND: 3,
    constants.BACKGROUND: 4
}


# turn codes into actual ansi sequences
def wrap_modifier(modifier_code):
    decorator_code = f'{constants.ANSI_START}{modifier_code}{constants.ANSI_END}'
    return decorator_code


# reset decoration sequence
RESET = wrap_modifier(constants.RESET_CHARACTER)

# font style sequences
BOLD = wrap_modifier(constants.BOLD_CODE)
UNDERLINE = wrap_modifier(constants.UNDERLINE_CODE)
REVERSED = wrap_modifier(constants.REVERSED_CODE)


def get_color_code(color):
    return COLORS[color]


def get_layer_code(layer):
    return LAYERS[layer]


# more color data accessors and utils
def get_layer_color_code(color, layer):
    color = get_color_code(color)
    layer = get_layer_code(layer)
    return f'{layer}{color}'


def get_colors():
    return COLORS.items()


def get_color_names():
    return COLORS.keys()


def get_layers():
    return LAYERS.items()


def get_layer_names():
    return LAYERS.keys()


def apply_modifier(string, modifier):
    pretty_string = f'{modifier}{string}'
    return pretty_string


def reset_modifiers(string):
    new_modified_string = f'{string}{RESET}'
    return new_modified_string


# make a list of wrapped ansi sequences ready to be prepended to any unicode string
def make_color_sequences_for_layer(layer):
    color_name_to_ansi = dict()
    color_names = get_color_names()
    for color_name in color_names:
        layer_color_code = get_layer_color_code(color_name, layer)
        color_name_to_ansi[color_name] = wrap_modifier(layer_color_code)
    return color_name_to_ansi


FG_COLOR_SEQUENCES = make_color_sequences_for_layer(constants.FOREGROUND)
BG_COLOR_SEQUENCES = make_color_sequences_for_layer(constants.BACKGROUND)


def get_foreground_color(color):
    return FG_COLOR_SEQUENCES[color]


def get_background_color(color):
    return BG_COLOR_SEQUENCES[color]


