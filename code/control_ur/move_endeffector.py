# move endeffector example
# key point
# - input format (tool poses that includes acceleration, speed and blend for each position) <- from document
#   - pose: target pose
#   - speed: tool speed [m/s]
#   - acceleration: tool acceleration [m/s^2]
#   - blend : blend radius (smoothly transition between two trajectories)
# - example
#   - rtde_c.moveL([x,y,z,rx,ry,rz, vel, acc, blend])
#   - rtde_c.moveL([x,y,z,rx,ry,rz], vel, acc, blend)

import rtde_control
import rtde_receive

def main(args=None):
    # init RTDE
    rtde_r = rtde_receive.RTDEReceiveInterface("192.168.0.100")
    rtde_c = rtde_control.RTDEControlInterface("192.168.0.100")

    vel = 0.25
    acc = 0.25
    blend = [0.0,0.2,0.0]
    p_1 = [-0.4914631078468379, -0.13492551489161278, 0.19083228093654026, 1.1377255981031682, -1.1964374573165788, -1.169625411023437, vel, acc, blend[0]]
    p_2 = [-0.43278167519201205, -0.1298241705490827, 0.4600776558304424, 1.1516785695530976, -1.2297141804292866, -1.227578682081981, vel, acc, blend[1]]
    p_3 = [-0.38553063458084413, 0.20675857572961903, 0.2705035439515677, 0.9428075894291785, -1.5607237131178935, -1.5591541559462414, vel,acc, blend[2]]

    p_path = [p_1,p_2,p_3]
    rtde_c.moveL(p_path)


    rtde_c.stopScript()


if __name__ == '__main__':
    main()