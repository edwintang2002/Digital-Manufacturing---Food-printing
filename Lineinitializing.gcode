G21 ; units to millimeters
G28 ; Home
G90 ; Use absolute positioning

T1 ; Select tool 0 for the first and second layers

; Drip Line
G01 X0 Y0 Z5 F150 ; Move to start height
G01 X10 Y10 Z5 F150 ; Move to drip line 
G01 X50 Y10 E0.5 F100 ; Extrude drip line

G01 X60 Y60 F150; Move to start location
G01 X60 Y80 E0.25 F100 ; Line 1 test
G01 X60 Y60 F150 ; move back

G01 X70 Y60 F200; Move to start location
G01 X70 Y80 E0.5 F150; line 2 test
G01 X70 Y60 F150; move back

G01 X80 Y60 F200; Move to start location
G01 X80 Y80 E1 F150; line 3 test
G01 X80 Y60 F150; move back 





G01 Z30 E-1.5 F300 ; Move up and retract filament
G01 X5 Y5 ; Move to park position

