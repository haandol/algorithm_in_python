# coding: utf-8


def hanoi(height, from_pole, mid_pole, to_pole):
    if height >= 1:
        hanoi(height-1, from_pole, to_pole, mid_pole)
        move_pole(from_pole, to_pole)
        hanoi(height-1, mid_pole, from_pole, to_pole)


def move_pole(from_pole, to_pole):
    print('moving disk from {} to {}'.format(from_pole, to_pole))


if '__main__' == __name__:
    hanoi(3, 'A', 'B', 'C')
