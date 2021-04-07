import serial
 
port = "/dev/serial0" #the rpisink uses ttyAMA0 AND serial0 for UART, it DOES NOT USE ttyS0
 
def parseGPS(data):
#    print "raw:", data #prints raw data
    if data[0:6] == "$GPRMC":
        sdata = data.split(",")
        if sdata[2] == 'V':
            print ("no satellite data available")
            return
        
        print ("---Parsing GPRMC---"),
        
        lat = decode(sdata[3]) #latitude
        dirLat = sdata[4]      #latitude direction N/S
        lon = decode(sdata[5]) #longitute
        dirLon = sdata[6]      #longitude direction E/W
        speed = sdata[7]       #Speed in knots
        
        print ("latitude : %s(%s), longitude : %s(%s), speed : %s," %  (lat,dirLat,lon,dirLon,speed))
 
def decode(coord):
    #Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"
 
 
print ("Receiving GPS data")
ser = serial.Serial(port, baudrate = 57600, timeout = 0.5)
while True:
   data = ser.readline()
   parseGPS(data)