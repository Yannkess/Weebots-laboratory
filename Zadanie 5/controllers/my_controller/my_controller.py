"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

TIME_STEP = 16

push= 0.02
hide= -0.02
front= 0.7
back = -0.7
center= hide
stage = 0
time = 0
avoidObstacleCounter = 0


l0_leg_pos= hide
l1_leg_pos= hide
l2_leg_pos= hide 
r0_leg_pos= hide
r1_leg_pos= hide
r2_leg_pos= hide


l0_motor_pos = center
l1_motor_pos = center
l2_motor_pos = center
r0_motor_pos = center
r1_motor_pos = center
r2_motor_pos = center

robot = Robot()


l0_motor = robot.getDevice('l0_motor')
l1_motor = robot.getDevice('l1_motor')
l2_motor = robot.getDevice('l2_motor')
r0_motor = robot.getDevice('r0_motor')
r1_motor = robot.getDevice('r1_motor')
r2_motor = robot.getDevice('r2_motor')

l0_leg = robot.getDevice('l0_leg')
l1_leg = robot.getDevice('l1_leg')
l2_leg = robot.getDevice('l2_leg')
r0_leg = robot.getDevice('r0_leg')
r1_leg = robot.getDevice('r1_leg')
r2_leg = robot.getDevice('r2_leg')

ds1 = robot.getDevice('ds1')
ds2 = robot.getDevice('ds2')

ds1.enable(TIME_STEP)
ds2.enable(TIME_STEP)

def rotate_right(stage):

    
    if stage == 0:
        
        l0l= hide
        l1l= hide
        l2l= hide
        r0l= hide
        r1l= hide
        r2l= hide

        l0m = center
        l1m = center
        l2m = center
        r0m = center
        r1m = center
        r2m = center

    elif stage == 1:
        l0l= hide
        l1l= push
        l2l= hide
        r0l= push
        r1l= hide
        r2l= push

        l0m = back
        l1m = front
        l2m = back
        r0m = front
        r1m = back
        r2m = front
    elif stage == 2:
        l0l= push
        l1l= push
        l2l= push
        r0l= push
        r1l= push
        r2l= push

        l0m = back
        l1m = front
        l2m = back
        r0m = front
        r1m = back
        r2m = front
    elif stage == 3:
        l0l= push
        l1l= hide
        l2l= push
        r0l= hide
        r1l= push
        r2l= hide

        l0m = back
        l1m = front
        l2m = back
        r0m = front
        r1m = back
        r2m = front
    elif stage == 4:
        l0l= push
        l1l= hide
        l2l= push
        r0l= hide
        r1l= push
        r2l= hide

        l0m = front
        l1m = back
        l2m = front
        r0m = back
        r1m = front
        r2m = back
    elif stage == 5:
        l0l= push
        l1l= push
        l2l= push
        r0l= push
        r1l= push
        r2l= push

        l0m = front
        l1m = back
        l2m = front
        r0m = back
        r1m = front
        r2m = back
    elif stage == 6:
        l0l= hide
        l1l= push
        l2l= hide
        r0l= push
        r1l= hide
        r2l= push

        l0m = front
        l1m = back
        l2m = front
        r0m = back
        r1m = front
        r2m = back

    return l0l,l1l,l2l,r0l,r1l,r2l,l0m,l1m,l2m,r0m,r1m,r2m

def move_forward(stage):

    
    if stage == 0:
        
        l0l= hide
        l1l= hide
        l2l= hide
        r0l= hide
        r1l= hide
        r2l= hide

        l0m = center
        l1m = center
        l2m = center
        r0m = center
        r1m = center
        r2m = center

    elif stage == 1:
        l0l= hide
        l1l= push
        l2l= hide
        r0l= push
        r1l= hide
        r2l= push

        l0m = back
        l1m = front
        l2m = back
        r0m = back
        r1m = front
        r2m = back
    elif stage == 2:
        l0l= push
        l1l= push
        l2l= push
        r0l= push
        r1l= push
        r2l= push

        l0m = back
        l1m = front
        l2m = back
        r0m = back
        r1m = front
        r2m = back
    elif stage == 3:
        l0l= push
        l1l= hide
        l2l= push
        r0l= hide
        r1l= push
        r2l= hide

        l0m = back
        l1m = front
        l2m = back
        r0m = back
        r1m = front
        r2m = back
    elif stage == 4:
        l0l= push
        l1l= hide
        l2l= push
        r0l= hide
        r1l= push
        r2l= hide

        l0m = front
        l1m = back
        l2m = front
        r0m = front
        r1m = back
        r2m = front
    elif stage == 5:
        l0l= push
        l1l= push
        l2l= push
        r0l= push
        r1l= push
        r2l= push

        l0m = front
        l1m = back
        l2m = front
        r0m = front
        r1m = back
        r2m = front
    elif stage == 6:
        l0l= hide
        l1l= push
        l2l= hide
        r0l= push
        r1l= hide
        r2l= push

        l0m = front
        l1m = back
        l2m = front
        r0m = front
        r1m = back
        r2m = front

    return l0l,l1l,l2l,r0l,r1l,r2l,l0m,l1m,l2m,r0m,r1m,r2m
     

while robot.step(TIME_STEP) != -1:


    ds1Value = ds1.getValue()
    ds2Value = ds2.getValue()


    if time == 0:
        stage = 0
    if time >=6:
        if stage == 6:
            stage = 1
            time = 1
        else:
            stage += 1
            time = 1

    time += 1

    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        l0_leg_pos,l1_leg_pos,l2_leg_pos,r0_leg_pos,r1_leg_pos,r2_leg_pos,l0_motor_pos,l1_motor_pos,l2_motor_pos,r0_motor_pos,r1_motor_pos,r2_motor_pos = rotate_right(stage)
    else:  
        if ds1Value < 950 or ds2Value < 950:
            avoidObstacleCounter = 77
        l0_leg_pos,l1_leg_pos,l2_leg_pos,r0_leg_pos,r1_leg_pos,r2_leg_pos,l0_motor_pos,l1_motor_pos,l2_motor_pos,r0_motor_pos,r1_motor_pos,r2_motor_pos = move_forward(stage)



    l0_leg.setPosition(l0_leg_pos)
    l0_motor.setPosition(l0_motor_pos)

    l1_leg.setPosition(l1_leg_pos)
    l1_motor.setPosition(l1_motor_pos)

    l2_leg.setPosition(l2_leg_pos)
    l2_motor.setPosition(l2_motor_pos)

    r0_leg.setPosition(r0_leg_pos)
    r0_motor.setPosition(r0_motor_pos)

    r1_leg.setPosition(r1_leg_pos)
    r1_motor.setPosition(r1_motor_pos)

    r2_leg.setPosition(r2_leg_pos)
    r2_motor.setPosition(r2_motor_pos)


