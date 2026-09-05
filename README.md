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
Rises at LST : 6h11m
Sets at LST  : 22h20m
# Example 2: Calculate Altitude and Azimuth of a target object
lst = hms_to_hours(6, 19, 26)
ra_target = hms_to_hours(2, 55, 7)
dec_target = 14 + 42 / 60
lat_observer = 60.16

h_deg = (lst - ra_target) * 15  # Hour angle in degrees
alt, az = altitude_azimuth(h_deg, dec_target, lat_observer)

print(f"Altitude : {alt:.1f}°")
print(f"Azimuth  : {az:.1f}°")
Altitude : 32.7°
Azimuth  : 232.0°
