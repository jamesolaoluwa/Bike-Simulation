# Bike Simulation

Welcome to My Bike Simulation, a Python program that simulates the operation of a motorcycle. This simulation allows you to start, stop, change gears, accelerate, and even engage nitro boost!

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Features

- **Start**: Start the bike to begin your ride.
- **Change Gear**: Switch between "neutral," "low gear," and "high gear" for different riding conditions.
- **Accelerate**: Accelerate the bike's speed and optionally engage nitro for a speed boost.
- **Engage Nitro**: Activate the nitro boost to experience thrilling acceleration.
- **Disengage Nitro**: Safely disengage nitro when you want to return to normal speed.
- **Stop**: Bring the bike to a stop at the end of your ride.

## Getting Started

To use this Bike Simulation, follow these steps:

1. Make sure you have Python installed on your computer. If not, you can download it from the [Python website](https://www.python.org/downloads/).

2. Download the `bikesimulation.py` file from this repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where `bikesimulation.py` is located.

4. Run the simulation by executing the following command:

   ```bash
   python bikesimulation.py
   ```

## Usage

Once you run the simulation, you can interact with the motorcycle using the following commands:

- `start`: Start the motorcycle.
- `change_gear`: Switch between "neutral," "low gear," and "high gear."
- `accelerate`: Accelerate the motorcycle and optionally engage nitro boost.
- `engage_nitro`: Activate the nitro boost.
- `disengage_nitro`: Safely disengage nitro.
- `stop`: Stop the motorcycle.

Here's an example of how to use the simulation:

```python
bike = BikeSimulation('Aprilla', 'CB1', 'Red', 2009, 250)

bike.start()
bike.change_gear()
bike.accelerate()
bike.engage_nitro()
bike.accelerate()
bike.disengage_nitro()
bike.accelerate()
bike.stop()
```
