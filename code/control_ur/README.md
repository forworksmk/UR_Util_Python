## Usage
**[control_ur] Set values to move UR**
- `move_joints.py`
    - set joints value to move UR joints
    - api : `rtde_c.moveJ(q_path)`
        - input : (joint positions, speed, acceleration, blend)
            - q: joint positions [rad]
            - speed: joint speed of leading axis [rad/s]
            - acceleration: joint acceleration of leading axis [rad/s^2]
            - blend : blend radius (smoothly transition between two trajectories)
- `move_endeffector.py`
    - set end-effector position value to move UR joints
    - api : `rtde_c.moveL(p_path)`
        - input : (pose,speed,acceleration,blend)
            - pose: target pose [m]
            - speed: tool speed [m/s]
            - acceleration: tool acceleration [m/s^2]
            - blend : blend radius (smoothly transition between two trajectories)