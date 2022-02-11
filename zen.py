import random
import constants

from chalk import modify_string


def end_line(line):
    line = f"{line}{constants.END_OF_LINE}"
    return line


def repeat_string(string, length):
    s = ''.join([string for x in range(length)])
    return s


def make_padding(line_width):
    line = f"{constants.FRAME_Y_CHAR}{repeat_string(' ', line_width - 2)}{constants.FRAME_Y_CHAR}"
    line = modify_string(line, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR)
    line = end_line(line)
    return line


def make_frame_horizontal_side(line_width):
    line = f"{repeat_string(constants.FRAME_INNER_X_CHAR, line_width)}"
    line = modify_string(line, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR)
    line = end_line(line)
    return line


def make_text_line(line, padding):
    pad = repeat_string(' ', padding)
    left_pad = f"{constants.FRAME_Y_CHAR}{pad}"
    right_pad = f"{pad}{constants.FRAME_Y_CHAR}"
    left_pad = modify_string(left_pad, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR)
    right_pad = modify_string(right_pad, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR)
    text = modify_string(line, constants.DEFAULT_TEXT_COLOR, constants.DEFAULT_BACKGROUND_COLOR, 'underline')
    line = f"{left_pad}{text}{right_pad}"
    line = end_line(line)
    return line


def frame_zen(zen):
    text_width = len(zen)
    frame_width = text_width + (constants.HORIZONTAL_PADDING * 2) + 2
    frame_side_x = make_frame_horizontal_side(frame_width)
    padding_line = make_padding(frame_width)
    text_line = make_text_line(zen, constants.HORIZONTAL_PADDING)
    y_padding = repeat_string(padding_line, constants.VERTICAL_PADDING)
    frame = frame_side_x + y_padding + text_line + y_padding + frame_side_x
    return frame


def python_zen():
    with open("zen.txt") as zen:
        commandments = [commandment for commandment in zen]
    nugget_of_wisdom = random.choice(commandments)
    stripped_nugget = nugget_of_wisdom.strip()
    framed_wisdom = frame_zen(stripped_nugget)
    return framed_wisdom


if __name__ == '__main__':
    result = python_zen()
    print(result)
