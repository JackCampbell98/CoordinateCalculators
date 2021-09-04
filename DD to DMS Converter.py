degree_sign = u'\N{DEGREE SIGN}'

lat_dd = ("data_needed")
long_dd = ("data_needed")

#dd user input
while lat_dd != float():
    lat_dd = float(input("Enter latitude in decimal degrees format: "))
    if (lat_dd > 90) or (lat_dd < -90): 
        print("Input is outside range. Please enter a valid latitude...") 
        continue
    else: 
        break

while long_dd != float():
    long_dd = float(input("Enter longitude in decimal degrees format: "))
    if (long_dd > 180) or (long_dd < -180): 
        print("Input is outside range. Please enter a valid longitude...") 
        continue
    else: 
        break

#store degrees from dd
lat_deg = (int(lat_dd))
long_deg = (int(long_dd))

#calculate minutes float component
float_lat_min = (lat_dd - lat_deg) * 60
float_long_min = (long_dd - long_deg) * 60

lat_min = int(float_lat_min)
long_min = int(float_long_min)

#calculate seconds float component
float_lat_sec = (float_lat_min - lat_min) * 60
float_long_sec = (float_long_min - long_min) *60

lat_sec = round(float_lat_sec, 5) 
long_sec = round(float_long_sec, 5)

#print to terminal
print("Latitude in DMS: " + str(lat_deg) + str(degree_sign) + " " + str(lat_min) + "' " + str(lat_sec) + '"')
print("Longitude in DMS: " + str(long_deg) + str(degree_sign) + " " + str(long_min) + "' " + str(long_sec) + '"') 

input('Press ENTER to exit')