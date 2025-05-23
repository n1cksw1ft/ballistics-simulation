import numpy as np

# --- Constants & Setup ---
m = 0.0081  # mass in kg (125 grain)
v0 = 940    # muzzle velocity in m/s
theta_deg = 35
theta = np.radians(theta_deg)

Cd = 0.35  #  drag coefficient for .308
d = 0.00782  # bullet diameter in meters
A = np.pi * (d / 2)**2  # cross-sectional area
rho = 1.225  # air density at sea level
g = 9.81  # gravity in m/s^2

# --- Initial Conditions ---
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)
v = np.array([vx, vy], dtype=float)
pos = np.array([0.0, 1.55], dtype=float)  # start at 1.55m height

# --- Simulation Parameters ---
dt = 0.01  # time step in seconds
penetration_energy_joules = 80

# --- Tracking ---
max_penetration_distance = 0.0
last_energy = 0.0
impact_distance = 0.0

prev_pos = pos.copy()
prev_v = v.copy()

# --- Simulation Loop ---
while True:
    speed = np.linalg.norm(v)
    if speed == 0:
        break

    # Drag and gravity
    drag_force = -0.5 * rho * Cd * A * speed * v
    drag_acc = drag_force / m
    gravity = np.array([0, -g])
    acc = drag_acc + gravity

    # Update motion
    v += acc * dt
    pos += v * dt

    # Track energy
    KE = 0.5 * m * speed**2
    if KE >= penetration_energy_joules:
        max_penetration_distance = pos[0]
        last_energy = KE

    # Check for ground impact
    if pos[1] < 0:
        # Interpolate impact distance
        dy = pos[1] - prev_pos[1]
        dx = pos[0] - prev_pos[0]
        t_ratio = -prev_pos[1] / dy
        impact_distance = prev_pos[0] + t_ratio * dx
        break

    # Save previous step
    prev_pos = pos.copy()
    prev_v = v.copy()

# --- Results ---
print(f"Max distance with ≥80 J energy: {max_penetration_distance:.2f} meters")
print(f"Final energy at that point: {last_energy:.2f} J")
print(f"Total distance until impact: {impact_distance:.2f} meters")