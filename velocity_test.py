from dynamixel_sdk import *

DEVICENAME = '/dev/ttyACM0'
BAUDRATE = 1000000
PROTOCOL_VERSION = 2.0

DXL_ID = 1

ADDR_TORQUE_ENABLE = 64
ADDR_OPERATING_MODE = 11
ADDR_GOAL_VELOCITY = 104

TORQUE_DISABLE = 0
TORQUE_ENABLE = 1
VELOCITY_MODE = 1

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

if not portHandler.openPort():
    print("Failed open port")
    quit()

if not portHandler.setBaudRate(BAUDRATE):
    print("Failed baudrate")
    quit()

print("Connected")

# 1 disable torque
packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_TORQUE_ENABLE,
    TORQUE_DISABLE
)

print("Torque disabled")

# 2 set velocity mode
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_OPERATING_MODE,
    VELOCITY_MODE
)

print("Mode:", dxl_comm_result, dxl_error)

# 3 enable torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)

print("Torque:", dxl_comm_result, dxl_error)

# 4 set velocity
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
    portHandler,
    DXL_ID,
    ADDR_GOAL_VELOCITY,
    100
)

print("Velocity:", dxl_comm_result, dxl_error)
