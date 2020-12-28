#runs only on python 2.7
#python 3+ has an issue with the NEMA header comparison found on line 10 in the parseGPS function

#Example of GGA message format
#sdata[   0     1        2    3     4     5 6  7  8    9   9  10  11 12  13]
#      $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M  ,, *47
#
#     GGA          Global Positioning System Fix Data
#     123519       Fix taken at 12:35:19 UTC
#     4807.038,N   Latitude 48 deg 07.038' N
#     01131.000,E  Longitude 11 deg 31.000' E
#     1            Fix quality: 0 = invalid
#                               1 = GPS fix (SPS)
#                               2 = DGPS fix
#                               3 = PPS fix
#                               4 = Real Time Kinematic
#                               5 = Float RTK
#                               6 = estimated (dead reckoning) (2.3 feature)
#                               7 = Manual input mode
#                               8 = Simulation mode
#     08           Number of satellites being tracked
#     0.9          Horizontal dilution of position
#     545.4,M      Altitude, Meters, above mean sea level
#     46.9,M       Height of geoid (mean sea level) above WGS84
#                      ellipsoid
#     (empty field) time in seconds since last DGPS update
#     (empty field) DGPS station ID number
#     *47          the checksum data, always begins with *
import serial
import time
 
port = "/dev/serial0"
 
def parseGPS(data):
#    print "raw:", data #prints raw data
    
    if data[0:6] == '$GPGGA':
        sdata = data.split(",")
        print "---Parsing GPGGA---"           
        time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        if sdata[2] != '':
            lat = decode(sdata[2]) #latitude
        else:
            lat = "0"
        dirLat = sdata[3]      #latitude direction N/S
        if sdata[4] != '':
            lon = decode(sdata[4]) #longitute
        else:
            lon = "0"
        dirLon = sdata[5]      #longitude direction E/W
        
        fix = sdata[6]       #number of satellites being tracked
        satcnt = sdata[7]    #True course
        horzdil = sdata[8] # = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6]#date
        alti = sdata[9]
        fname = 'GPS_TESTING'
        saveGGAData (fix,satcnt,horzdil,alti,fname)
        
        print ("fix: %s, sat.Cnt.: %s, horiz. dilution: %s, altitude(M) %s" % (fix,satcnt,horzdil,alti))
 
    if data[0:6] == '$GPRMC':
        sdata = data.split(",")
        if sdata[2] == 'V':
            print "no satellite data available"
            text = "no satellite data available"
            saveNoConnect(text, "GPS_TESTING")
            return
        print "---Parsing GPRMC---"
        time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        lat = decode(sdata[3]) #latitude
        dirLat = sdata[4]      #latitude direction N/S
        lon = decode(sdata[5]) #longitute
        dirLon = sdata[6]      #longitude direction E/W
        speed = sdata[7]       #Speed in knots
        trCourse = sdata[8]    #True course
        date = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6]#date
        fname = 'GPS_TESTING'
        saveRMCData (time, lat, dirLat, lon, dirLon, speed, trCourse, date, fname)
        print ("time: %s, latitude: %s(%s), longitude: %s(%s), speed: %s, True Course: %s, Date: %s" %  (time,lat,dirLat,lon,dirLon,speed,trCourse,date))
 
def decode(coord):
    #Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    print coord
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"

def saveRMCData(time, lat, dirLat, lon, dirLon, speed, trCourse, date, fname):
    #save cleaned GPS-RMC data to a text file for later analysis
    #append the file format to the file name string 
    fname = fname + ".txt"
    try:
        print "Opening File"
        #see if this file exists so that we can "append" data to the end of the file
        file = open(fname, "a")
    except:
        print "Creating File"
        file = open(fname, "w+")
    
    data = "time : %s, latitude : %s(%s), longitude : %s(%s), speed : %s, True Course : %s, Date : %s \n" %  (time,lat,dirLat,lon,dirLon,speed,trCourse,date)
    print "saving data" 
    file.write(data)
    print "closing file"
    file.close()
    
def saveGGAData(fix,satcnt,horzdil,alti, fname):
    #save cleaned GPS-GGA data to a text file for later analysis
    #append the file format to the file name string 
    fname = fname + ".txt"
    try:
        print "Opening File"
        #see if this file exists so that we can "append" data to the end of the file
        file = open(fname, "a")
    except:
        print "Creating File"
        file = open(fname, "w+")
    
    data = "fix: %s, sat.Cnt.: %s, horiz. dilution: %s, altitude: %s M \n" % (fix,satcnt,horzdil,alti)
    print "saving data" 
    file.write(data)
    print "closing file"
    file.close()

def saveNoConnect(text, fname):
    #save "No connection" Text to text file for later analysis
    #append the file format to the file name string 
    fname = fname + ".txt"
    try:
        print "Opening File"
        #see if this file exists so that we can "append" data to the end of the file
        file = open(fname, "a")
    except:
        print "Creating File"
        file = open(fname, "w+")
    print "saving data" 
    file.write(text)
    print "closing file"
    file.close()
 
print "Receiving GPS data"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
   data = ser.readline()
   parseGPS(data)
   #time.sleep(3)

 
