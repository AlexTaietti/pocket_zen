import random

from ansi_sequences import COLORS

END_LINE = '\r\n'


def end_line(line):
    line = f"{line}{END_LINE}"
    return line


def repeat_string(string, length):
    string = ''.join([string for iteration in range(length)])
    return string


def get_random_color(exclude=None):
    color_names = list(COLORS.keys())
    if exclude:
        color_names.remove(exclude)
    color = random.choice(color_names)
    return color

