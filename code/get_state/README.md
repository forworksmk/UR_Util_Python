## Usage
**[get_state] Read values from the UR**
- `get_joint_pos.py`
    - read positions of the joints from the UR
    - api : `rtde_r.getActualQ()`
        - output : (q1, q2, q3, q4, q5, q6) [rad]
- `get_endeffector_pose.py`
    - read xyz positions(cartesian coordinates) and xyz rotations of the end-effector from the UR
    - api : `rtde_r.getActualTCPPose()`
        - output : (x,y,z,rx,ry,rz)
            - x, y, z : [meter]
            - rx, ry, rz : [rad]