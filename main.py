from dataclasses import dataclass

# Constants
INERTIA = 1.0
DT = 0.1

@dataclass
class SystemState:
    theta_rad: float
    omega_rad_per_sec: float

def state_derivation(state: SystemState, torque_nm: float) -> list[float]:
    # [theta_dot, omega_dot] -> [omega, torque / Inertia]
    omega_rad_per_sec = state.omega_rad_per_sec
    alpha_rad_per_sec2 = torque_nm / INERTIA
    return [omega_rad_per_sec, alpha_rad_per_sec2]

def euler_step(state: SystemState, torque_nm: float, dt: float) -> SystemState:
    # x_new = x + dx/dt * dt
    theta_dot, omega_dot = state_derivation(state, torque_nm)
    
    return SystemState(
        theta_rad=state.theta_rad + theta_dot * dt,
        omega_rad_per_sec=state.omega_rad_per_sec + omega_dot * dt
    )

def main():
    initial_theta_rad = 0.0
    initial_omega_rad_per_sec = 0.0
    
    # Initialize dataclass instance
    state = SystemState(initial_theta_rad, initial_omega_rad_per_sec)
    torque_nm = 1.0  # Changed to 1.0 so you can see the values change!
    
    # Reduced loop count for console printing safety, change back if needed
    for i in range(100):
        current_time = i * DT
        state = euler_step(state, torque_nm, DT)
        print(f"time: {current_time:.2f}s, angular position: {state.theta_rad:.4f} rad, angular velocity: {state.omega_rad_per_sec:.4f} rad/s")

if __name__ == "__main__":
    main()
