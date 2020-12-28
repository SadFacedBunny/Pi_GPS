##jdaniels
##12.27.2020

##this will parse my gps logs so that they can be visualized

fname = "GPS_DRIVE2"
fname = fname + ".txt"

        

with open(fname) as LogFile:

    ##try to open or create a parsed file
    fname = fname[:-4] + "_parsed.csv"
    try:
        #see if this file exists so that we can "append" data to the end of the file
        file = open(fname, "a")
        print("Opening File")
        file.write("drive_name,lat,lon,speed\n")
    except:
        print("Creating File")
        file = open(fname, "w+")
        

    ##for each line in logfile
    for line in LogFile:

        if  line == "no satellite data available " or line == "no fix on satellite ":
            pass
        elif line[:4] == "time":
            ##time : 13:30:01, latitude : 49 deg 43.78108 min(N), longitude : 012 deg 08.34999 min(E), speed : 54.733, True Course : 130.86, Date : 27/12/20 
            ##01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
            ##          1         2         3         4         5         6         7         8         9         0         1         2         3
            ##      drive_name          Lat                                 Long                            speed

            ##Decimal Degrees = degrees + (minutes/60) + (seconds/3600)
            latDD = int(line[28:30]) + ((float(line[35:43])/60))
            
            lonDD = int(line[64:67]) + ((float(line[72:80])/60))
            
            data =  fname[:-11] + "," + str(latDD) + "," + str(lonDD) + "," +  line[97:102]
            file.write(data + "\n")
        
        elif line[:2] == "fix":
            ##fix: 1, sat.Cnt.: 04, horiz. dilution: 6.54, altitude: 381.8 M
            ##01234567890123456789012345678901234567890123456789012345678901
            ##          1         2         3       4         5           6    
            data = 0
            pass

    file.close()
        
