"""
Spherical Astronomy Calculator
================================
Implements the classical rising/setting equation and coordinate
conversions derived from spherical trigonometry (rotation between
the equatorial and horizontal reference frames):

    cos h = -tan(delta) * tan(phi)

where:
    h     = hour angle at rising/setting
    delta = declination of the object
    phi   = observer's latitude

Also includes:
    - hour angle -> altitude/azimuth conversion
    - sidereal time <-> local solar time conversion
    - rise/set sidereal time calculation

Based on the derivation and worked problems from:
"Dynamics of Celestial Bodies" project (Risha Abdul Rasheed,
supervised by Dr. Chrispin Karthick, IIA).
"""

import math


# ---------- helpers ----------

def hms_to_hours(h, m, s=0):
    """Convert hours/minutes/seconds to decimal hours."""
    return h + m / 60 + s / 3600


def deg_to_dms_str(deg):
    """Convert decimal degrees to a 'D° M′' string."""
    sign = "-" if deg < 0 else ""
    deg = abs(deg)
    d = int(deg)
    m = (deg - d) * 60
    return f"{sign}{d}\u00b0{m:.1f}\u2032"


def hours_to_hm_str(hours):
    """Convert decimal hours to 'Hh Mm' string, wrapping into 0-24h."""
    hours = hours % 24
    h = int(hours)
    m = (hours - h) * 60
    return f"{h}h{round(m):02d}m"


# ---------- core formulas ----------

def hour_angle_at_rise_set(dec_deg, lat_deg):
    """
    Hour angle (in degrees) at which an object of declination dec_deg
    rises/sets, for an observer at latitude lat_deg.

    cos h = -tan(delta) * tan(phi)

    Returns h in degrees (0-180). The object rises at h = -h, sets at h = +h.
    Raises ValueError if the object is circumpolar or never rises.
    """
    delta = math.radians(dec_deg)
    phi = math.radians(lat_deg)
    cos_h = -math.tan(delta) * math.tan(phi)

    if cos_h > 1 or cos_h < -1:
        raise ValueError(
            "Object is circumpolar or never rises at this latitude "
            "(|cos h| > 1)."
        )

    h_rad = math.acos(cos_h)
    return math.degrees(h_rad)


def rise_set_sidereal_time(ra_hours, dec_deg, lat_deg):
    """
    Local sidereal time (in decimal hours) at which an object rises
    and sets.

    Theta = alpha +/- h   (h converted from degrees to hours)
    """
    h_deg = hour_angle_at_rise_set(dec_deg, lat_deg)
    h_hours = h_deg / 15.0

    theta_rise = (ra_hours - h_hours) % 24
    theta_set = (ra_hours + h_hours) % 24

    return theta_rise, theta_set


def altitude_azimuth(hour_angle_deg, dec_deg, lat_deg):
    """
    Convert hour angle + declination to altitude and azimuth
    for an observer at a given latitude.

    sin(a)        = sin(delta)sin(phi) + cos(delta)cos(h)cos(phi)
    sin(A)cos(a)  = sin(h)cos(delta)
    cos(A)cos(a)  = cos(h)cos(delta)sin(phi) - sin(delta)cos(phi)
    """
    h = math.radians(hour_angle_deg)
    delta = math.radians(dec_deg)
    phi = math.radians(lat_deg)

    sin_a = math.sin(delta) * math.sin(phi) + math.cos(delta) * math.cos(h) * math.cos(phi)
    a = math.asin(sin_a)

    sinA_cosa = math.sin(h) * math.cos(delta)
    cosA_cosa = math.cos(h) * math.cos(delta) * math.sin(phi) - math.sin(delta) * math.cos(phi)

    A = math.atan2(sinA_cosa, cosA_cosa)

    altitude_deg = math.degrees(a)
    azimuth_deg = math.degrees(A) % 360

    return altitude_deg, azimuth_deg


def zonal_to_local_solar_time(zonal_time_hours, longitude_deg, standard_meridian_deg):
    """
    Convert zonal (standard) time to local mean solar time.
    Every 15 degrees of longitude = 1 hour, 1 degree = 4 minutes.
    """
    diff_deg = standard_meridian_deg - longitude_deg
    diff_hours = diff_deg / 15.0
    return zonal_time_hours - diff_hours


def estimate_sidereal_time(local_solar_time_hours, day_of_year_from_equinox):
    """
    Estimate sidereal time from local solar time and days elapsed
    since the vernal equinox (~21 March).

    Theta ~= T + 12h + n * 4min
    """
    n = day_of_year_from_equinox
    theta = local_solar_time_hours + 12 + (n * 4) / 60.0
    return theta % 24


# ---------- worked examples (from the project) ----------

if __name__ == "__main__":
    print("=" * 60)
    print("Problem 1: Arcturus rise/set sidereal time in Boston")
    print("=" * 60)
    ra = hms_to_hours(14, 15.7)
    dec = 19 + 11 / 60
    lat = 42 + 19 / 60
    theta_rise, theta_set = rise_set_sidereal_time(ra, dec, lat)
    print(f"RA = {ra:.4f}h, Dec = {deg_to_dms_str(dec)}, Lat = {deg_to_dms_str(lat)}")
    print(f"Rises at LST = {hours_to_hm_str(theta_rise)}")
    print(f"Sets  at LST = {hours_to_hm_str(theta_set)}")

    print()
    print("=" * 60)
    print("Problem 2: Local solar time in Paris at 12:00 official time")
    print("=" * 60)
    local_time = zonal_to_local_solar_time(12.0, longitude_deg=2, standard_meridian_deg=15)
    print(f"Mean local solar time = {hours_to_hm_str(local_time)}")
    print("(True solar time varies by the Equation of Time, roughly")
    print(" 10:54-11:24 across the year)")

    print()
    print("=" * 60)
    print("Problem 3: Estimated sidereal time, Paris, 15 April 22:00 (zonal clock time)")
    print("=" * 60)
    solar_time = zonal_to_local_solar_time(22.0, longitude_deg=2, standard_meridian_deg=15)
    theta = estimate_sidereal_time(solar_time, day_of_year_from_equinox=25)
    print(f"Local solar time = {hours_to_hm_str(solar_time)}")
    print(f"Estimated sidereal time = {hours_to_hm_str(theta)}")

    print()
    print("=" * 60)
    print("Problem 4: Altitude/Azimuth of the Moon over Helsinki")
    print("=" * 60)
    ra_moon = hms_to_hours(2, 55, 7)
    dec_moon = 14 + 42 / 60
    lst = hms_to_hours(6, 19, 26)
    lat_helsinki = 60.16
    h_deg = (lst - ra_moon) * 15  # hour angle in degrees
    alt, az = altitude_azimuth(h_deg, dec_moon, lat_helsinki)
    print(f"Hour angle = {h_deg:.2f} deg")
    print(f"Altitude = {alt:.1f} deg")
    print(f"Azimuth  = {az:.1f} deg")
