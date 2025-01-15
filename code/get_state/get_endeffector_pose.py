# get endeffector pos

import rtde_control
import rtde_receive
import numpy as np

def main(args=None):
    # init RTDE
    rtde_r = rtde_receive.RTDEReceiveInterface("192.168.0.100")
    rtde_c = rtde_control.RTDEControlInterface("192.168.0.100")

    current_TCPPose = np.array(rtde_r.getActualTCPPose()).copy()
    print(current_TCPPose)
    rtde_c.stopScript()

if __name__ == '__main__':
    main()