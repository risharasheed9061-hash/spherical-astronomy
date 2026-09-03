# Derivation of the Rising and Setting Equation

## Setup
A point P on a unit sphere is described by two angles: theta and psi.
Rotating the coordinate frame around the x-axis by angle chi gives a
second frame (x', y', z').

## Coordinate relations
z = sin(theta)
x = cos(theta) * cos(psi)
y = cos(theta) * sin(psi)

## After rotation
x' = x
y' = y*cos(chi) + z*sin(chi)
z' = z*cos(chi) - y*sin(chi)

## Substituting in
cos(theta)*cos(psi) = cos(theta')*cos(psi')
cos(theta')*sin(psi') = cos(theta)*sin(psi)*cos(chi) + sin(theta)*sin(chi)
sin(theta') = sin(theta)*cos(chi) - cos(theta)*sin(psi)*sin(chi)

## Applying to the horizon/equatorial systems
chi = 90° - phi (phi = observer's latitude)
theta = a (altitude), theta' = delta (declination)
psi = 90° - A (azimuth), psi' = 90° - h (hour angle)

## Result
sin(a) = sin(delta)*sin(phi) + cos(delta)*cos(h)*cos(phi)

Setting altitude a = 0 (the moment of rising/setting):

cos(h) = -tan(delta) * tan(phi)

This is the rising/setting equation used in calculator.py.
