degree_sign = u'\N{DEGREE SIGN}'

ddlat = ("data_needed")
ddlong = ("data_needed")

#dd user input
while ddlat != float():
    ddlat = float(input("Enter latitude in decimal degrees format: "))
    if (ddlat > 90) or (ddlat < -90): 
        print("Input is outside range. Please enter a valid latitude...") 
        continue
    else: 
        break


while ddlong != float():
    ddlong = float(input("Enter longitude in decimal degrees format: "))
    if (ddlong > 180) or (ddlong < -180): 
        print("Input is outside range. Please enter a valid longitude...") 
        continue
    else: 
        break

#store degrees from dd
deglat = (int(ddlat))
deglong = (int(ddlong))

#calculate minutes float component
float_minlat = (ddlat - deglat) * 60
float_minlong = (ddlong - deglong) * 60

minlat = int(float_minlat)
minlong = int(float_minlong)

#calculate seconds float component
float_seclat = (float_minlat - minlat) * 60
float_seclong = (float_minlong - minlong) *60

seclat = round(float_seclat, 5) 
seclong = round(float_seclong, 5)

#print to terminal
print("Latitude in DMS: " + str(deglat) + str(degree_sign) + " " + str(minlat) + "' " + str(seclat) + '"')
print("Longitude in DMS: " + str(deglong) + str(degree_sign) + " " + str(minlong) + "' " + str(seclong) + '"') 

input('Press ENTER to exit')