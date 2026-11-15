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
- `tilt_test.py`: compares sunlight on flat ground, a south roof (30°) and a north roof (30°) for Darmstadt on 21 December 2026 (clear sky; edit the date in the script to test other days)

## First results (clear-sky model, no clouds)
Daily sunlight in kWh/m² for Darmstadt:

| Surface | 21 June | 21 December |
|---|---|---|
| Flat ground | 7.54 | 0.98 |
| South roof, 30° tilt | 7.56 | 2.17 |
| North roof, 30° tilt | 5.99 | 0.31 |

Findings: in summer, tilt hardly changes the daily total, while in winter a south roof receives about 2.2 times more than flat ground. A north roof loses almost everything in winter. Real values will be lower because of clouds, and this will be checked with PVGIS weather data.

## Author
Pavithra G, M.Sc. Electrical Engineering, Power Engineering (Hochschule Darmstadt)
