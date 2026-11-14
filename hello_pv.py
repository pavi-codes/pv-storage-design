import pvlib
import pandas as pd

# Location: Darmstadt
loc = pvlib.location.Location(49.87, 8.65, tz="Europe/Berlin",
                              altitude=150, name="Darmstadt")

# 24 hourly time steps on 21 June 2026
times = pd.date_range("2026-06-21", periods=24, freq="h", tz=loc.tz)

# Clear-sky sunlight (no clouds), in W/m²
cs = loc.get_clearsky(times)
print(cs.loc["2026-06-21 12:00":"2026-06-21 14:00"].round(0))