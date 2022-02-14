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

# layers
LAYERS = {
    'fore': 3,
    'back': 4
}


# text styles
TEXT_STYLES = {
    'bold': 1,
    'underline': 4,
    'reverse': 7
}

# ansi characters
ANSI_START = '\u001b['
ANSI_END = 'm'
RESET_CHARACTER = '0'


# turn codes into actual ansi sequences
def wrap_modifier(modifier_code):
    decorator_code = f'{ANSI_START}{modifier_code}{ANSI_END}'
    return decorator_code


# reset decoration sequence
RESET = wrap_modifier(RESET_CHARACTER)


# useful utility used to make strings beautiful
def apply_modifier(string: str, modifier):
    if string.startswith(ANSI_START) and string.endswith(RESET):
        string = f'{modifier}{string}'
    else:
        string = f'{modifier}{string}{RESET}'
    return string


# make a list of wrapped ansi text style sequences ready to be prepended to any unicode string
def make_text_style_sequences():
    text_style_to_ansi = dict()
    text_styles = TEXT_STYLES.items()
    for style, code in text_styles:
        text_style_to_ansi[style] = wrap_modifier(code)
    return text_style_to_ansi


TEXT_STYLE_SEQUENCES = make_text_style_sequences()


# make 2 lists of wrapped ansi color sequences (foreground and background) ready to be prepended to any unicode string
def make_color_sequences_for_layer(layer):
    color_name_to_ansi = dict()
    color_names = COLORS.keys()
    for color_name in color_names:
        layer_color_code = get_layer_color_code(color_name, layer)
        color_name_to_ansi[color_name] = wrap_modifier(layer_color_code)
    return color_name_to_ansi


def get_layer_color_code(color, layer):
    color = COLORS[color]
    layer = LAYERS[layer]
    return f'{layer}{color}'


FG_COLOR_SEQUENCES = make_color_sequences_for_layer('fore')
BG_COLOR_SEQUENCES = make_color_sequences_for_layer('back')


# module's interface
def get_foreground_color(color):
    return FG_COLOR_SEQUENCES[color]


def get_background_color(color):
    return BG_COLOR_SEQUENCES[color]


def get_text_style_code(text_style):
    return TEXT_STYLE_SEQUENCES[text_style]
