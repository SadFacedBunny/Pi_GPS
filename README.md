# Pi_GPS
This is a project i completed for school. I was able to use a raspberry pi 3b and a gps adapter with the Blox NEO-6M chip, to log my gps data. With additional help from python and the library plotly, i was able to then map my coordinates that i previously logged. 


I originally wanted to use this project to analyse my MPG during my daily drive but, i am not that far yet. This is the minimal form of the project can only plot the coordinates onto and interactive map 

useful tutorial:
https://www.electronicwings.com/raspberry-pi/gps-module-interfacing-with-raspberry-pi

Message format documentation:
https://www.trimble.com/OEM_ReceiverHelp/V4.44/en/NMEA-0183messages_MessageOverview.html

```
Example of GGA message format
sdata[   0     1        2    3     4     5 6  7  8    9   9  10  11 12  13]
      $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M  ,, *47

     GGA          Global Positioning System Fix Data
     123519       Fix taken at 12:35:19 UTC
     4807.038,N   Latitude 48 deg 07.038' N
     01131.000,E  Longitude 11 deg 31.000' E
     1            Fix quality: 0 = invalid
                               1 = GPS fix (SPS)
                               2 = DGPS fix
                               3 = PPS fix
                               4 = Real Time Kinematic
                               5 = Float RTK
                               6 = estimated (dead reckoning) (2.3 feature)
                               7 = Manual input mode
                               8 = Simulation mode
     08           Number of satellites being tracked
     0.9          Horizontal dilution of position
     545.4,M      Altitude, Meters, above mean sea level
     46.9,M       Height of geoid (mean sea level) above WGS84
                      ellipsoid
     (empty field) time in seconds since last DGPS update
     (empty field) DGPS station ID number
     *47          the checksum data, always begins with *
```
