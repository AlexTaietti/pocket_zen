# constant strings
FOREGROUND = 'fore'
BACKGROUND = 'back'

BLACK = 'black'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
WHITE = 'white'

BOLD = 'bold'
UNDERLINE = 'underline'
REVERSE = 'reverse'

# ansi characters
ANSI_START = '\u001b['
ANSI_END = 'm'
RESET_CHARACTER = '0'


# color codes
COLORS = {
    BLACK: 0,
    RED: 1,
    GREEN: 2,
    YELLOW: 3,
    BLUE: 4,
    MAGENTA: 5,
    CYAN: 6,
    WHITE: 7
}

# layers
LAYERS = {
    FOREGROUND: 3,
    BACKGROUND: 4
}


# text styles
TEXT_STYLES = {
    BOLD: 1,
    UNDERLINE: 4,
    REVERSE: 7
}

# general
END_OF_LINE = '\r\n'

# frame characters
FRAME_INNER_X_CHAR = '='
FRAME_Y_CHAR = '|'
FRAME_OUTER_TOP_CHAR = '‾'
FRAME_OUTER_BOTTOM_CHAR = '_'
FRAME_ASKEW_RIGHT = '/'
FRAME_ASKEW_LEFT = '\\'

DEFAULT_TEXT_COLOR = CYAN
DEFAULT_BACKGROUND_COLOR = BLACK

HORIZONTAL_PADDING = 4
VERTICAL_PADDING = 1
