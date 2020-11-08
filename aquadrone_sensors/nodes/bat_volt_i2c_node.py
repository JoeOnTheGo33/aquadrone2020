#!/usr/bin/env python

import rospy
import sys
import smbus # pip

print(sys.version)

RESOLUTION = 18
R1 = [10e3, 47e3, 86.6e3, 127e3]
R2 = 28.7e3


from MCP342x import MCP342x # pip install MCP342x

print(MCP342x)


def create_pack(bus, addr)
    pack = []
    for j in range(4):
        adr_sensor = MCP342x(bus, addr, j, resolution=RESOLUTION, scale_factor= R2 / (R1[i]+R2) )
        pack.append(adr_sensor)
    return pack
    


rospy.init_node("bat_volt_sensor")


bus = smbus.SMBus(1)
cell_sensors = []
cell_volts = [0.0] * 8

cell_sensors.extend(create_pack(bus, 110))
cell_sensors.extend(create_pack(bus, 101))

print(cell_sensors)

for s in all_sensors():
    s.configure()


while not rospy.is_shutdown():
    for i in range(len(cell_sensors):
        cell_volts[i] = cell_sensor[i].convert_and_read()

    # TODO publish voltage
    
    rate.sleep()




