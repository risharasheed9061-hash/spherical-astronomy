# spherical-astronomy

This project derives the classical equation for when stars rise and set (from spherical trigonometry), and includes a Python calculator that computes rise/set times, altitude, and azimuth for celestial objects.

Based on coursework for "Dynamics of Celestial Bodies," supervised by Dr. Chrispin Karthick, Indian Institute of Astrophysics.

## Usage

You can import and use the core astronomical functions directly in Python:

```python
from calculator import hms_to_hours, rise_set_sidereal_time, altitude_azimuth, hours_to_hm_str

# Example 1: Compute rise and set sidereal times for Arcturus in Boston
ra = hms_to_hours(14, 15.7)
dec = 19 + 11 / 60
lat = 42 + 19 / 60

theta_rise, theta_set = rise_set_sidereal_time(ra, dec, lat)

print(f"Rises at LST : {hours_to_hm_str(theta_rise)}")
print(f"Sets at LST  : {hours_to_hm_str(theta_set)}")
```
