from ansi_sequences import apply_modifier, reset_modifiers, get_foreground_color, get_background_color


def color_string(string, text_color, background=None):
    color_code = get_foreground_color(text_color)
    pretty_string = apply_modifier(string, color_code)
    if background:
        background_color_code = get_background_color(background)
        pretty_string = apply_modifier(pretty_string, background_color_code)
    pretty_string = reset_modifiers(pretty_string)
    return pretty_string


if __name__ == '__main__':
    s = color_string('=============', 'black', background='blue')
    print(s)
