from colors import get_colors, get_layer_color_code

# ansi sequence characters
ANSI_START = '\u001b['
ANSI_END = 'm'
RESET_CHARACTER = '0'

# text style codes
BOLD_CODE = '1'
UNDERLINE_CODE = '4'
REVERSED_CODE = '7'


# turn codes into actual ansi sequences
def wrap_modifier(modifier_code):
    decorator_code = f'{ANSI_START}{modifier_code}{ANSI_END}'
    return decorator_code


# reset decoration sequence
RESET = wrap_modifier(RESET_CHARACTER)

# font style sequences
BOLD = wrap_modifier(BOLD_CODE)
UNDERLINE = wrap_modifier(UNDERLINE_CODE)
REVERSED = wrap_modifier(REVERSED_CODE)


# make a list of wrapped ansi sequences ready to be prepended to any unicode string
def make_color_sequences_for_layer(layer):
    color_name_to_ansi = dict()
    colors = get_colors()
    for color_name, color_code in colors:
        layer_color_code = get_layer_color_code(color_name, layer)
        color_name_to_ansi[color_name] = wrap_modifier(layer_color_code)
    return color_name_to_ansi


FG_COLOR_SEQUENCES = make_color_sequences_for_layer('fore')
BG_COLOR_SEQUENCES = make_color_sequences_for_layer('back')


def get_foreground_color(color):
    return FG_COLOR_SEQUENCES[color]


def get_background_color(color):
    return BG_COLOR_SEQUENCES[color]


def apply_modifier(string, modifier):
    pretty_string = f'{modifier}{string}{RESET}'
    return pretty_string


def add_modifier(modified_string, modifier):
    new_modified_string = f'{modifier}{modified_string}'
    return new_modified_string


def color_string(string, text_color, background=None):
    color_code = get_foreground_color(text_color)
    pretty_string = apply_modifier(string, color_code)
    if background:
        background_color_code = get_background_color(background)
        pretty_string = add_modifier(pretty_string, background_color_code)
    return pretty_string


if __name__ == '__main__':
    s = color_string('=============', 'black', background='blue')
    print(s)

