# control gripper example
# key point
# - To ensure precise operation, check whether the gripper's action is fully completed.

import time
import sys
sys.path.append("../../package")
from gripper.rg_gripper import RG

rg = RG(gripper='rg2', ip="192.168.0.114", port="502")

if __name__ == '__main__':
    # fully opened
    rg.open_gripper(force=400)
    while True:
        time.sleep(0.5)
        if not rg.get_status()[0]:
            break

    # fully closed
    rg.close_gripper(force=400)
    while True:
        time.sleep(0.5)
        if not rg.get_status()[0]:
            break

    # move to middle point (max width : 1600)
    rg.move_gripper(550,force=400)
    while True:
        time.sleep(0.5)
        if not rg.get_status()[0]:
            break

    rg.close_connection()