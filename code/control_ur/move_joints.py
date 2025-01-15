# move UR joints example
# key point
# - input format (joint positions that includes acceleration, speed and blend for each position) <- from document
#   - q: joint positions
#   - speed: joint speed of leading axis [rad/s]
#   - acceleration: joint acceleration of leading axis [rad/s^2]
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

    vel = 0.5
    acc = 0.5
    blend = [0.0,0.15,0.0]
    q_1 = [-0.0008276144610803726, -1.288763241176941, 2.100346390401022, -0.8569260400584717, 1.5611083507537842, 0.06798052787780762, vel, acc, blend[0]]
    q_2 = [-0.00010854402651006012, -1.7139908275999964, 1.779182259236471, -0.09303029001269536, 1.6089975833892822, 0.032881975173950195, vel, acc, blend[1]]
    q_3 = [-9.00884475e-01, -1.60826506e+00,  2.19351061e+00, -5.85258489e-01, 1.16221126e+00, 4.98549025e-06, vel,acc, blend[2]]

    q_path = [q_1,q_2,q_3]
    rtde_c.moveJ(q_path)


    rtde_c.stopScript()


if __name__ == '__main__':
    main()
