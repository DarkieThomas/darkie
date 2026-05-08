from dynamixel_sdk import *

DEVICENAME = '/dev/ttyACM0'
BAUDRATE = 1000000
PROTOCOL_VERSION = 2.0

DXL_ID = 1

ADDR_TORQUE_ENABLE = 64
ADDR_OPERATING_MODE = 11
ADDR_GOAL_VELOCITY = 104

TORQUE_ENABLE = 1
VELOCITY_MODE = 1

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

if portHandler.openPort():
    print("Port opened")
else:
    print("Failed to open port")
    quit()

if portHandler.setBaudRate(BAUDRATE):
    print("Baudrate set")
else:
    print("Failed baudrate")
    quit()

packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_TORQUE_ENABLE,
    0
)

packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_OPERATING_MODE,
    VELOCITY_MODE
)

packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)

packetHandler.write4ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_GOAL_VELOCITY,
    30
)

print("Motor spinning")
