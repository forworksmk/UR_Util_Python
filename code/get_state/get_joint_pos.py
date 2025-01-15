# get joints pos

import rtde_control
import rtde_receive
import numpy as np

def main(args=None):
    # init RTDE
    rtde_r = rtde_receive.RTDEReceiveInterface("192.168.0.100")
    rtde_c = rtde_control.RTDEControlInterface("192.168.0.100")

    current_q = np.array(rtde_r.getActualQ()).copy()
    print(current_q)
    rtde_c.stopScript()

if __name__ == '__main__':
    main()