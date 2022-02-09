import random
from my_chalk import color_string


END_OF_LINE = '\r\n'


def repeat_char(char, length):
    s = ''.join([char for x in range(length)])
    return s


def repeat_line(line, n_lines):
    lines = ''.join([line for x in range(n_lines)])
    return lines


def make_padding_line(line_width):
    line = f"|{repeat_char(' ', line_width - 2)}|{END_OF_LINE}"
    return line


def make_frame_horizontal_line(line_width):
    line = f"{repeat_char('=', line_width)}{END_OF_LINE}"
    return line


def make_text_line(line, padding):
    pad = repeat_char(' ', padding)
    line = f"|{pad}{line}{pad}|{END_OF_LINE}"
    return line


def frame_zen(zen, horizontal_padding=4, vertical_padding=1):
    text_width = len(zen)
    frame_width = text_width + (horizontal_padding * 2) + 2
    frame_side_x = make_frame_horizontal_line(frame_width)
    padding_line = make_padding_line(frame_width)
    text_line = make_text_line(zen, horizontal_padding)
    y_padding = repeat_line(padding_line, vertical_padding)
    frame = frame_side_x + y_padding + text_line + y_padding + frame_side_x
    return frame


def python_zen():
    with open("zen.txt") as zen:
        commandments = [commandment for commandment in zen]
    nugget_of_wisdom = random.choice(commandments)
    stripped_nugget = nugget_of_wisdom.strip()
    framed_wisdom = frame_zen(stripped_nugget)
    colorful_wisdom = color_string(framed_wisdom, 'cyan')
    return colorful_wisdom


if __name__ == '__main__':
    result = python_zen()
    print(result)
