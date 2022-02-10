import random
import constants

from chalk import color_string


def wrap_line(line, text_color='cyan', background_color='black'):
    line = color_string(line, text_color, background_color)
    line = f"{line}{constants.END_OF_LINE}"
    return line


def repeat_char(char, length):
    s = ''.join([char for x in range(length)])
    return s


def repeat_line(line, n_lines):
    lines = ''.join([line for x in range(n_lines)])
    return lines


def make_padding_line(line_width, frame_y):
    line = f"{frame_y}{repeat_char(' ', line_width - 2)}{frame_y}"
    line = wrap_line(line)
    return line


def make_frame_horizontal_line(line_width, frame_x):
    line = f"{repeat_char(frame_x, line_width)}"
    line = wrap_line(line)
    return line


def make_text_line(line, padding, frame_y):
    pad = repeat_char(' ', padding)
    line = f"{frame_y}{pad}{line}{pad}{frame_y}"
    line = wrap_line(line)
    return line


def frame_zen(zen, frame_x, frame_y, horizontal_padding=4, vertical_padding=1):
    text_width = len(zen)
    frame_width = text_width + (horizontal_padding * 2) + 2
    frame_side_x = make_frame_horizontal_line(frame_width, frame_x)
    padding_line = make_padding_line(frame_width, frame_y)
    text_line = make_text_line(zen, horizontal_padding, frame_y)
    y_padding = repeat_line(padding_line, vertical_padding)
    frame = frame_side_x + y_padding + text_line + y_padding + frame_side_x
    return frame


def python_zen(frame_x_char="=", frame_y_char="|"):
    with open("zen.txt") as zen:
        commandments = [commandment for commandment in zen]
    nugget_of_wisdom = random.choice(commandments)
    stripped_nugget = nugget_of_wisdom.strip()
    framed_wisdom = frame_zen(stripped_nugget, frame_x_char, frame_y_char)
    return framed_wisdom


if __name__ == '__main__':
    result = python_zen()
    print(result)
