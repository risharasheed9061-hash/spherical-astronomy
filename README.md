# spherical-astronomy

This project derives the classical equation for when stars rise and set
(from spherical trigonometry), and includes a Python calculator that
computes rise/set times, altitude, and azimuth for celestial objects.

Based on coursework for "Dynamics of Celestial Bodies," supervised by
Dr. Chrispin Karthick, Indian Institute of Astrophysics.

## Usage

```python
from calculator import celestial_calculator

# Example: Compute rise/set time for target coordinates
result = celestial_calculator(latitude=12.9716, declination=15.32, ra=5.59)
print(result)
```

**Output:**
```text
Rise Time : 05:42:10 UTC
Set Time  : 18:15:22 UTC
Azimuth   : 78.4°
```
## Testing

All four worked problems were run and verified to match the original
calculations from the project report.
