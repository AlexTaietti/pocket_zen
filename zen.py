import random

from frame import frame_string


def python_zen():
    with open("zen.txt") as zen:
        tips = [tip.strip() for tip in zen]
    nugget_of_wisdom = random.choice(tips)
    framed_wisdom = frame_string(nugget_of_wisdom)
    return framed_wisdom


if __name__ == '__main__':
    framed_zen = python_zen()
    print(framed_zen)
