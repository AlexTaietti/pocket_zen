import random

# ansi sequence characters
ANSI_ESCAPE = '\u001b['
END_MODIFIER = 'm'
RESET_CHARACTER = '0'

# text style codes
BOLD_CODE = '1'
UNDERLINE_CODE = '4'
REVERSED_CODE = '7'


def _wrap_modifier(modifier_code):
    decorator_code = f'{ANSI_ESCAPE}{modifier_code}{END_MODIFIER}'
    return decorator_code


# reset decoration modifier
RESET = _wrap_modifier(RESET_CHARACTER)

# color modifiers
FG_COLORS = tuple([_wrap_modifier(str(n)) for n in range(30, 37)])
BG_COLORS = tuple([_wrap_modifier(str(n)) for n in range(40, 47)])

# font style modifiers
BOLD = _wrap_modifier(BOLD_CODE)
UNDERLINE = _wrap_modifier(UNDERLINE_CODE)
REVERSED = _wrap_modifier(REVERSED_CODE)


def _apply_modifier(modifier, string):
    pretty_string = f'{modifier}{string}{RESET}'
    return pretty_string


def make_string_random_color(string, background=False):
    layer_color_codes = FG_COLORS if not background else BG_COLORS
    color = random.choice(layer_color_codes)
    colorful = _apply_modifier(color, string)
    return colorful


if __name__ == '__main__':
    s = make_string_random_color('ciao', background=True)
    print(s)

