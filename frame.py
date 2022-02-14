import shutil
import textwrap

from chalk import modify_string
from formatting_utils import repeat_string, end_line, get_random_color

# default colors
DEFAULT_BACKGROUND_COLOR = 'black'
DEFAULT_TEXT_COLOR = get_random_color(exclude=DEFAULT_BACKGROUND_COLOR)

# frame size
HORIZONTAL_PADDING = 6
FRAME_THICKNESS = 2
FRAME_PIECES_WIDTH = (HORIZONTAL_PADDING * 2) + (FRAME_THICKNESS * 2) + 4


def decorate_wrap_line(line):
    line = modify_string(line, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR)
    line = end_line(line)
    return line


def make_frame_top_outer_line(frame_width):
    line = f"|\\{repeat_string('‾', frame_width-4)}/|"
    line = decorate_wrap_line(line)
    return line


def make_frame_bottom_outer_line(frame_width):
    line = f"|/{repeat_string('_', frame_width-4)}\\|"
    line = decorate_wrap_line(line)
    return line


def make_frame_top_inner_line(frame_width):
    line = f"| \\{repeat_string('_', frame_width-6)}/ |"
    line = decorate_wrap_line(line)
    return line


def make_frame_empty_line(frame_width):
    line = repeat_string(' ', frame_width - 8)
    line = f"|  |{line}|  |"
    line = decorate_wrap_line(line)
    return line


def make_frame_bottom_inner_line(frame_width):
    line = f"| /{repeat_string('‾', frame_width-6)}\\ |"
    line = decorate_wrap_line(line)
    return line


def normalize_chunk_width(chunk, chunk_width):
    chunk = chunk.strip()
    if len(chunk) < chunk_width:
        spaces_count = chunk_width - len(chunk)
        spaces = repeat_string(' ', spaces_count)
        text = modify_string(chunk, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, 'underline')
        padding = modify_string(spaces, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR)
        chunk = f"{text}{padding}"
        return chunk
    chunk = modify_string(chunk, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, 'underline')
    return chunk


def make_text_horizontal_padding():
    padding = repeat_string(' ', HORIZONTAL_PADDING)
    left_padding = f"|  |{padding}"
    right_padding = f"{padding}|  |"
    left_padding = modify_string(left_padding, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR)
    right_padding = modify_string(right_padding, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR)
    right_padding = end_line(right_padding)
    return left_padding, right_padding


def fit_text_to_terminal(string, terminal_width):
    text_width = terminal_width - FRAME_PIECES_WIDTH
    chunks = textwrap.wrap(string, text_width)
    longest_chunk = max(chunks, key=len)
    final_text_width = len(longest_chunk)
    padding_left, padding_right = make_text_horizontal_padding()
    chunks = [normalize_chunk_width(chunk, final_text_width) for chunk in chunks]
    strings = [f"{padding_left}{chunk}{padding_right}" for chunk in chunks]
    pretty_text = ''.join(strings)
    return pretty_text, final_text_width


def build_frame_top(frame_width):
    frame_outer_top = make_frame_top_outer_line(frame_width)
    frame_inner_top = make_frame_top_inner_line(frame_width)
    frame_top = f"{frame_outer_top}{frame_inner_top}"
    return frame_top


def build_frame_bottom(frame_width):
    frame_inner_bottom = make_frame_bottom_inner_line(frame_width)
    frame_outer_bottom = make_frame_bottom_outer_line(frame_width)
    frame_bottom = f"{frame_inner_bottom}{frame_outer_bottom}"
    return frame_bottom


def build_single_line(string):
    string = modify_string(string, DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, 'underline')
    padding_left, padding_right = make_text_horizontal_padding()
    text = f"{padding_left}{string}{padding_right}"
    return text


def frame_string(string):
    text_width = len(string)
    frame_width = text_width + FRAME_PIECES_WIDTH
    terminal_width = shutil.get_terminal_size().columns
    if frame_width > terminal_width:
        text, text_width = fit_text_to_terminal(string, terminal_width)
        frame_width = text_width + FRAME_PIECES_WIDTH
    else:
        text = build_single_line(string)
    vertical_padding = make_frame_empty_line(frame_width)
    frame_top = build_frame_top(frame_width)
    frame_bottom = build_frame_bottom(frame_width)
    frame = f"{frame_top}{vertical_padding}{text}{vertical_padding}{frame_bottom}"
    return frame
