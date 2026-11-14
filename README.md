# PV and battery system design for a German household

Simulation project in Python (pvlib, pandas, matplotlib).
Status: work in progress, started November 2026.

## Goal
Size a rooftop PV system and a home battery for a typical 4-person household in Darmstadt, Germany, and simulate one year hour by hour to find self-consumption, autarky and payback time.

## Plan
1. Sunlight on a tilted roof (clear sky, then real weather data from PVGIS)
2. PV power per hour, including temperature and inverter losses
3. Household load profile
4. Battery charge and discharge rules
5. Yearly results: self-consumption, autarky, grid import and export
6. Costs and payback

## Current files
- `hello_pv.py`: first script, prints clear-sky irradiance (GHI, DNI, DHI) for Darmstadt on 21 June 2026

## Author
Pavithra G, M.Sc. Electrical Engineering, Power Engineering (Hochschule Darmstadt)
