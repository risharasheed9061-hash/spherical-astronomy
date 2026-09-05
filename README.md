# Spherical Astronomy Calculator

## Introduction

This project implements classical spherical astronomy formulas for computing when celestial objects rise and set, converting between coordinate systems, and estimating sidereal time. It is based on the derivation and worked problems from the *"Dynamics of Celestial Bodies"* project (Risha Abdul Rasheed, supervised by Dr. Chrispin Karthick, IIA).

The core idea comes from spherical trigonometry applied to the rotation between the equatorial and horizontal reference frames:

```
cos h = -tan(delta) * tan(phi)
```

where `h` is the hour angle at rising/setting, `delta` is the object's declination, and `phi` is the observer's latitude.

## Overview

The calculator provides the following capabilities:

- **Rise/set hour angle** — compute the hour angle at which an object rises or sets for a given latitude and declination.
- **Rise/set sidereal time** — convert that hour angle into local sidereal time using the object's right ascension.
- **Altitude/Azimuth conversion** — convert hour angle + declination into horizontal coordinates (altitude and azimuth) for an observer at a given latitude.
- **Zonal to local solar time** — convert standard/zonal clock time to local mean solar time based on longitude.
- **Sidereal time estimation** — estimate local sidereal time from local solar time and days elapsed since the vernal equinox.

All angles are handled in degrees for latitude/declination/azimuth/altitude, and decimal hours for right ascension and time, with helper functions provided to convert to/from `H:M:S` and `D° M′` formats.

## Usage

```python
from calculator import (
    hms_to_hours,
    rise_set_sidereal_time,
    altitude_azimuth,
    zonal_to_local_solar_time,
    estimate_sidereal_time,
    hours_to_hm_str,
)

# Example: rise/set sidereal time for an object
ra = hms_to_hours(14, 15.7)      # Right ascension in decimal hours
dec = 19 + 11 / 60               # Declination in degrees
lat = 42 + 19 / 60               # Observer latitude in degrees

theta_rise, theta_set = rise_set_sidereal_time(ra, dec, lat)

print(f"Rises at LST = {hours_to_hm_str(theta_rise)}")
print(f"Sets  at LST = {hours_to_hm_str(theta_set)}")
```

**Output:**

```
Rises at LST = 6h20m
Sets  at LST = 22h11m
```

```python
# Example: altitude/azimuth from hour angle and declination
alt, az = altitude_azimuth(hour_angle_deg=45.0, dec_deg=14.7, lat_deg=60.16)

print(f"Altitude : {alt:.1f}°")
print(f"Azimuth  : {az:.1f}°")
```

**Output:**

```
Altitude : 32.6°
Azimuth  : 108.3°
```

Run the module directly to see all four worked examples from the project (Arcturus rise/set in Boston, local solar time in Paris, estimated sidereal time in Paris, and the Moon's altitude/azimuth over Helsinki):

```bash
python calculator.py
```


---

## Testing

All four worked problems were run and verified to match the original calculations from the project report.
