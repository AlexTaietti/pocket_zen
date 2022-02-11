import constants


# turn codes into actual ansi sequences
def wrap_modifier(modifier_code):
    decorator_code = f'{constants.ANSI_START}{modifier_code}{constants.ANSI_END}'
    return decorator_code


# reset decoration sequence
RESET = wrap_modifier(constants.RESET_CHARACTER)


# useful utility used to make strings beautiful
def apply_modifier(string, modifier):
    if string.endswith(RESET):
        string = f'{modifier}{string}'
    else:
        string = f'{modifier}{string}{RESET}'
    return string


# make a list of wrapped ansi text style sequences ready to be prepended to any unicode string
def make_text_style_sequences():
    text_style_to_ansi = dict()
    text_styles = constants.TEXT_STYLES.items()
    for style, code in text_styles:
        text_style_to_ansi[style] = wrap_modifier(code)
    return text_style_to_ansi


TEXT_STYLE_SEQUENCES = make_text_style_sequences()


# make 2 lists of wrapped ansi color sequences (foreground and background) ready to be prepended to any unicode string
def make_color_sequences_for_layer(layer):
    color_name_to_ansi = dict()
    color_names = constants.COLORS.keys()
    for color_name in color_names:
        layer_color_code = get_layer_color_code(color_name, layer)
        color_name_to_ansi[color_name] = wrap_modifier(layer_color_code)
    return color_name_to_ansi


def get_layer_color_code(color, layer):
    color = constants.COLORS[color]
    layer = constants.LAYERS[layer]
    return f'{layer}{color}'


FG_COLOR_SEQUENCES = make_color_sequences_for_layer(constants.FOREGROUND)
BG_COLOR_SEQUENCES = make_color_sequences_for_layer(constants.BACKGROUND)


# module's interface
def get_foreground_color(color):
    return FG_COLOR_SEQUENCES[color]


def get_background_color(color):
    return BG_COLOR_SEQUENCES[color]


def get_text_style_code(text_style):
    return TEXT_STYLE_SEQUENCES[text_style]
