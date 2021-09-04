degree_sign = u'\N{DEGREE SIGN}'

lat_dms = ("data_needed")
lat_deg = ("data_needed")
lat_min = ("data_needed")
lat_sec = ("data_needed")

long_dms = ("data_needed")
long_deg = ("data_needed")
long_min = ("data_needed")
long_sec = ("data_needed")

while lat_deg != float():
    lat_dms = input("Enter latitude in DMS format (DD MM SS.SSSSS): ")
    lat_deg, lat_min, lat_sec = lat_dms.split()
    if (float(lat_deg) > 90) or (float(lat_deg) < -90) or (float(lat_min) > 60) or (float(lat_sec) > 60):
        print("Input is outside range. Please enter a valid latitude...")
        continue
    else:
        break

while long_deg != float():
    long_dms = input("Enter longitude in DMS format (DD MM SS.SSSSS): ")
    long_deg, long_min, long_sec = long_dms.split()
    if (float(lat_deg) > 180) or (float(lat_deg) < -180) or (float(lat_min) > 60) or (float(lat_sec) > 60):
        print("Input is outside range. Please enter a valid longitude...")
        continue
    else:
        break


lat_dd = (float(lat_deg) + (float(lat_min) / 60) + (float(lat_sec) / 3600))
long_dd = (float(long_deg) + (float(long_min) / 60) + (float(long_sec) / 3600))

print("Latitude in DMS: " + str(lat_dd))
print("Longitude in DMS: " + str(long_dd))

input('Press ENTER to exit')