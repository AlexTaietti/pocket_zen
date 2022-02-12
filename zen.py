import random
import constants

from chalk import modify_string


def end_line(line):
    line = f"{line}{constants.END_OF_LINE}"
    return line


def wrap_line(line):
    line = f"|{line}|"
    return line


def repeat_string(string, length):
    s = ''.join([string for x in range(length)])
    return s


def make_frame_top_outer(frame_width):
    line = f"|\\{repeat_string('‾', frame_width-4)}/|"
    line = modify_string(line, 'cyan', 'black')
    line = end_line(line)
    return line


def make_frame_bottom_outer(frame_width):
    line = f"|/{repeat_string('_', frame_width-4)}\\|"
    line = modify_string(line, 'cyan', 'black')
    line = end_line(line)
    return line


def make_frame_top_inner(frame_width):
    line = f"| \\{repeat_string('_', frame_width-6)}/ |"
    line = modify_string(line, 'cyan', 'black')
    line = end_line(line)
    return line


def make_frame_bottom_inner(frame_width):
    line = f"| /{repeat_string('‾', frame_width-6)}\\ |"
    line = modify_string(line, 'cyan', 'black')
    line = end_line(line)
    return line


def make_frame_padding_line(frame_width):
    line = repeat_string(' ', frame_width - 8)
    line = f"|  |{line}|  |"
    line = modify_string(line, 'cyan', 'black')
    line = end_line(line)
    return line


def make_string_line(string):
    pad = repeat_string(' ', constants.HORIZONTAL_PADDING - 1)
    left_pad = f"|  |{pad}"
    right_pad = f"{pad}|  |"
    left_pad = modify_string(left_pad, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR)
    right_pad = modify_string(right_pad, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR)
    text = modify_string(string, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR, 'underline')
    line = f"{left_pad}{text}{right_pad}"
    line = end_line(line)
    return line


def frame_string(string):
    text_width = len(string)
    frame_inner_width = text_width + (constants.HORIZONTAL_PADDING * 2) + 2
    frame_width = frame_inner_width + (constants.FRAME_THICKNESS * 2) + 2
    y_pad = make_frame_padding_line(frame_width)
    ftt = make_frame_top_outer(frame_width)
    ft = make_frame_top_inner(frame_width)
    txt = make_string_line(string)
    fb = make_frame_bottom_inner(frame_width)
    fbb = make_frame_bottom_outer(frame_width)
    frame = f"{ftt}{ft}{y_pad}{txt}{y_pad}{fb}{fbb}"
    return frame


def python_zen():
    with open("zen.txt") as zen:
        commandments = [commandment for commandment in zen]
    nugget_of_wisdom = random.choice(commandments)
    stripped_nugget = nugget_of_wisdom.strip()
    framed_wisdom = frame_string(stripped_nugget)
    return framed_wisdom


if __name__ == '__main__':
    f = python_zen()
    print(f)
