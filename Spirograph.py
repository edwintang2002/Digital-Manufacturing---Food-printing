import math as m
import csv


def main():
    R = 50  # R = radius of larger circle
    r = 30  # r = radius of circle traveling within larger circle
    d = 5  # d = distance from the center of the larger circle
    ext=0.15

    with(open('spiro.gcode', 'w')) as f:

        me = csv.writer(f)

        me.writerow(["G28"])  # home command
        me.writerow(["G1 Z6.2 E 0.05 F300"])  # pen up
        me.writerow(["G21"])  # Use mm
        me.writerow(["G90"])  # Use abs pos

        angle = 20
        theta = 0.3
        steps = 63
        i = 1
        for t in range(0, steps):  # loop to generate gcode
            angle += theta
            x = (R - r) * m.cos(angle) + d * m.cos(((R-r)/r)*angle)+80  # changes shape
            y = (R - r) * m.sin(angle) - d * m.sin(((R-r)/r)*angle)+80
            x = round(x, 1)  # so you don't crash the 3D printer
            y = round(y, 1)
            if i < 2:  # drop pen at start
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y)])
                me.writerow(["G1 Z6.2"])
                i = i + 1
            else:
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y) + " E" + str(ext)])
                i = i + 1


        me.writerow(["G1 Z8.2"])
        me.writerow(["T1"])
        me.writerow(["G92 X110.7"])
        for t in range(0, steps):  # loop to generate gcode
            angle += theta
            x = (R - r) * m.cos(angle) + d * m.cos(((R-r)/r)*angle)+80  # changes shape
            y = (R - r) * m.sin(angle) - d * m.sin(((R-r)/r)*angle)+80
            x = round(x, 1)  # so you don't crash the 3D printer
            y = round(y, 1)
            if i < 2:  # drop pen at start
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y)])
                me.writerow(["G1 Z6"])
                i = i + 1
            else:
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y) + " E" + str(ext)])
                i = i + 1

        me.writerow(["G1 Z10.2"])
        for t in range(0, steps):  # loop to generate gcode
            angle += theta
            x = (R - r) * m.cos(angle) + d * m.cos(((R-r)/r)*angle)+80  # changes shape
            y = (R - r) * m.sin(angle) - d * m.sin(((R-r)/r)*angle)+80
            x = round(x, 1)  # so you don't crash the 3D printer
            y = round(y, 1)
            if i < 2:  # drop pen at start
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y)])
                me.writerow(["G1 Z6"])
                i = i + 1
            else:
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y) + " E" + str(ext)])
                i = i + 1


        me.writerow(["G1 Z15"])
        me.writerow(["G28"])


main()
