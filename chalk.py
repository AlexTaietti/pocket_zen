from ansi_sequences import apply_modifier, get_foreground_color, get_background_color, get_text_style_code


def modify_string(string, text_color=None, background=None, text_style=None):
    if text_color:
        color_code = get_foreground_color(text_color)
        string = apply_modifier(string, color_code)
    if background:
        background_color_code = get_background_color(background)
        string = apply_modifier(string, background_color_code)
    if text_style:
        style_code = get_text_style_code(text_style)
        string = apply_modifier(string, style_code)
    return string
