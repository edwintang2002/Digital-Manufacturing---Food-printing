G21 ; units to millimeters
;G28 ; Home
M106 S255;
G90 ; Use absolute positioning

T0 ; Select tool 0 for the first and second layers

; Drip Line
G01 X0 Y0 Z5.9 F150 ; Move to start height
G01 X10 Y10 Z5.9 F150 ; Move to drip line 
G01 X50 Y10 E0.3 F100 ; Extrude drip line

; First Layer
G01 X60 Y60 F150; Move to triangle start location
G01 X60 Y60 E0 F100 ; Move to start
G01 X80 Y60 E0.5 F100 ; Line 1
G01 X70 Y74.6 E0.5 F100 ; Line 2 
G01 X60 Y60 E0.5 F100 ; Line 3 

; Second Layer 
G01 Z7 F150 ; Move up
G01 X60.52 Y60 E0 F100 ; Move to start after rotation
G01 X79.52 Y60.52 E0.5 F100 ; Line 1 
G01 X69.89 Y74.06 E0.5 F100 ; Line 2 
G01 X60.52 Y60 E0.5 F100 ; Line 3 

T1 ; Switch to tool 1 for the third layer
G92 X79.52

; Third Layer 
G01 Z9 F150 ; Move up 
G01 X61.04 Y60 E0 F100 ; Move to start after rot
G01 X79.04 Y61.04 E0.5 F100 ; Line 1
G01 X69.78 Y73.52 E0.5 F100 ; Line 2
G01 X61.04 Y60 E0.5 F100 ; Line 3


G01 Z30 E-1.5 F300 ; Move up and retract filament
G01 X10 Y10 ; Move to park position
M84
M106 S0
