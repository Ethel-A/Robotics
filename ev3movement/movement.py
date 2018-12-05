import ev3dev.ev3 as ev3
from .utils import compute_ticks_angle, compute_ticks


def move_straight_line(distance, speed):

    if distance < 0:
        raise Exception('Distance cannot be a negative value. You provided {}'.format(distance))

    if speed < 0 or speed > 1000:
        raise Exception('The speed cannot be greater than 1000 or less that 0. You provided {}'.format(speed))

    left_motor = ev3.LargeMotor('outC')
    right_motor = ev3.LargeMotor('outB')

    left_motor.run_to_rel_pos(position_sp=compute_ticks(distance), speed_sp=speed)
    right_motor.run_to_rel_pos(position_sp=(compute_ticks(distance)), speed_sp=speed)

    left_motor.wait_while('running')
    right_motor.wait_while('running')


def turn_left_by_angle(angle, speed):

    if speed < 0 or speed > 1000:
        raise Exception('The speed cannot be greater than 1000 or less that 0')

    if angle > 360 or angle < 0:
        raise Exception('The angle provided must be between 0 and 360. You provided {}'.format(angle))

    left_motor = ev3.LargeMotor('outC')
    right_motor = ev3.LargeMotor('outB')

    left_motor.stop()
    right_motor.run_to_rel_pos(position_sp=compute_ticks_angle(angle), speed_sp=speed)

    right_motor.wait_while('running')


def turn_right_by_angle(angle, speed):

    if speed < 0 or speed > 1000:
        raise Exception('The speed cannot be greater than 1000 or less that 0')

    if angle > 360 or angle < 0:
        raise Exception('The angle provided must be between 0 and 360. You provided {}'.format(angle))

    left_motor = ev3.LargeMotor('outC')
    right_motor = ev3.LargeMotor('outB')

    left_motor.run_to_rel_pos(position_sp=compute_ticks_angle(angle), speed_sp=speed)
    right_motor.stop()

    right_motor.wait_while('running')


def spin_left_by_angle(angle, speed):

    if speed < 0 or speed > 1000:
        raise Exception('The speed cannot be greater than 1000 or less that 0.You provided {}'.format(speed))

    if angle > 360 or angle < 0:
        raise Exception('The angle provided must be between 0 and 360. You provided {}'.format(angle))

    left_motor = ev3.LargeMotor('outC')
    right_motor = ev3.LargeMotor('outB')

    left_motor.run_to_rel_pos(position_sp=-compute_ticks_angle(angle), speed_sp=speed)
    right_motor.run_to_rel_pos(position_sp=compute_ticks_angle(angle), speed_sp=speed)

    left_motor.wait_while('running')
    right_motor.wait_while('running')
