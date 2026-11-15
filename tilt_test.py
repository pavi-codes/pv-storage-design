import pvlib
import pandas as pd

loc = pvlib.location.Location(49.87, 8.65, tz="Europe/Berlin",
                              altitude=150, name="Darmstadt")
times = pd.date_range("2026-12-21", periods=24, freq="h", tz=loc.tz)

solpos = loc.get_solarposition(times)   # where the sun is
cs = loc.get_clearsky(times)            # GHI, DNI, DHI


def poa(tilt, azimuth):
    """Sunlight on a tilted panel in W/m²."""
    result = pvlib.irradiance.get_total_irradiance(
        surface_tilt=tilt,
        surface_azimuth=azimuth,
        solar_zenith=solpos["apparent_zenith"],
        solar_azimuth=solpos["azimuth"],
        dni=cs["dni"], ghi=cs["ghi"], dhi=cs["dhi"])
    return result["poa_global"]


flat = cs["ghi"]
south = poa(30, 180)   # 180 = south
north = poa(30, 0)     # 0 = north

print("At 13:00, in W/m²")
print("  flat ground:", round(flat.iloc[13]))
print("  south roof :", round(south.iloc[13]))
print("  north roof :", round(north.iloc[13]))
print("Whole day, in kWh/m²")
print("  flat ground:", round(flat.sum() / 1000, 2))
print("  south roof :", round(south.sum() / 1000, 2))
print("  north roof :", round(north.sum() / 1000, 2))