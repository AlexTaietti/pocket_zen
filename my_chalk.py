from colors import get_background_color, get_foreground_color

# ansi sequence characters
ANSI_ESCAPE = '\u001b['
END_CHARACTER = 'm'
RESET_CHARACTER = '0'

# text style codes
BOLD_CODE = '1'
UNDERLINE_CODE = '4'
REVERSED_CODE = '7'


# turn numbers into actual ansi sequences
def _wrap_modifier(modifier_code):
    decorator_code = f'{ANSI_ESCAPE}{modifier_code}{END_CHARACTER}'
    return decorator_code


# reset decoration sequence
RESET = _wrap_modifier(RESET_CHARACTER)

# font style sequences
BOLD = _wrap_modifier(BOLD_CODE)
UNDERLINE = _wrap_modifier(UNDERLINE_CODE)
REVERSED = _wrap_modifier(REVERSED_CODE)


def _apply_modifier(string, modifier):
    pretty_string = f'{modifier}{string}{RESET}'
    return pretty_string


def _add_modifier(modified_string, modifier):
    new_modified_string = f'{modifier}{modified_string}'
    return new_modified_string


def color_string(string, text_color, background=None):
    color_code = get_foreground_color(text_color)
    color_modifier = _wrap_modifier(color_code)
    pretty_string = _apply_modifier(string, color_modifier)
    if background:
        background_color_code = get_background_color(background)
        background_modifier = _wrap_modifier(background_color_code)
        pretty_string = _add_modifier(pretty_string, background_modifier)
    return pretty_string


if __name__ == '__main__':
    s = color_string('=============', 'black', background='blue')
    print(s)

