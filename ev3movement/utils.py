from math import pi


RADIUS = 3.183
BASE_LINE = 12


def compute_ticks(distance):
    """

    :param distance:
    :return:
    """
    return (360 * distance) / (2 * pi * RADIUS)


def compute_ticks_angle(angle):
    """

    :param angle:
    :return:
    """
    return (angle * BASE_LINE) / RADIUS

