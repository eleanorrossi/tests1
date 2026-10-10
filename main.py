from dataclasses import dataclass

@dataclass
class State:
  theta_rad: float
  omega_rad_per_sec: float



def main():
  state = State(theta = 0.0, omega = 1.0)
  print()

if __name__ == "__main__":
  main()
  






