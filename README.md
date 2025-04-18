# Geothermal Energy Binary Power Plant

This repository contains a MATLAB implementation and analysis of an Organic Rankine Cycle (ORC) for a 100kW geothermal binary power plant.

![Organic Rankine Cycle](images/orc_diagram.png)

## Project Overview

This project demonstrates the design and modeling of a binary cycle geothermal power plant using the Organic Rankine Cycle. The implementation focuses on:

- Thermodynamic analysis of the ORC system
- Modeling of key components (evaporator, turbine, condenser, feed pump)
- Performance evaluation and visualization
- Analysis of energy efficiency and optimization

This project was conducted as part of the "Renewable Energy" course in the Master in Green Energy Technology program at Østfold University College.

## Technical Details

The Organic Rankine Cycle is modeled with the following components:

1. **Evaporator/Boiler**: Transfers heat from geothermal brine to the working fluid
2. **Turbine**: Expands the high-pressure vapor to generate mechanical power
3. **Condenser**: Rejects heat and condenses the working fluid
4. **Feed Pump**: Pressurizes the working fluid for re-circulation

The model includes:
- Temperature-entropy (T-s) and enthalpy-entropy (h-s) diagrams
- Calculation of thermal efficiency
- Power output analysis
- Parametric studies for optimization

## Features

- MATLAB implementation of ideal Organic Rankine Cycle
- Visualization tools for thermodynamic cycles
- Performance analysis under various operating conditions
- Efficiency comparison with other renewable energy technologies

## Installation & Usage

### Prerequisites
- MATLAB (R2019b or later recommended)
- XSteam Fluid Property Library

### Running the Model
1. Clone this repository
2. Open MATLAB and navigate to the repository directory
3. Run the main script:
```matlab
orc_model
```

## Results

The model demonstrates:
- High availability (>98% and 7500 operating hours/year)
- Power generation of 100kW (electricity)
- Low environmental impact
- Thermodynamic efficiency analysis with temperature range of 35-450°C

## Advantages of Geothermal Binary Power Plants

- High degree of availability (>98%)
- Environmentally friendly with low CO2 emissions
- Weather-independent energy production
- Small ecological footprint
- Established technology for electricity production
- Low operating costs
- Potential for heat storage applications

## Future Work

Potential areas for further development:
- Analysis of geothermal production and re-injection wells
- Advanced thermodynamic models using Simulink
- Optimization of working fluid selection
- Economic analysis and feasibility studies
- Integration with other renewable energy systems