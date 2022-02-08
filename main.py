import random


def python_zen():
    with open("zen.txt") as zen:
        commandments = [commandment for commandment in zen]
    nugget_of_wisdom = random.choice(commandments)
    print(nugget_of_wisdom)


if __name__ == '__main__':
    python_zen()
