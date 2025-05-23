# .308 Ballistics Simulation – Applied Maths Project

This Python project simulates how far a .308 Winchester spitzer bullet can travel before it drops below the lethal energy threshold (80 joules). It includes gravity, air resistance, firing angle, and firing height.

This was created for a 5th year Applied Maths project.

## What It Does

- Calculates how far the bullet travels
- Includes drag and gravity
- Stops when the bullet hits the ground or becomes non-lethal (<80 J)
- Prints the distance and impact energy at that point

## Requirements

- Python 3.x
- numpy

To install numpy, run:pip install numpy

## How to Run

Download or clone this repo.

Then run the simulation:

python ballistics_sim.py

## Files

- `ballistics_sim.py` – the main simulation
- `requirements.txt` – Python packages needed
- `README.md` – this file

## Notes

- Firing height is set to 1.55 meters
- Drag coefficient, air density, and angle can be changed at the top of the script


