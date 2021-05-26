import exifread

with open(r'C:\Users\123\Pictures\IMG_20210521_110141.jpg', 'rb') as f:
    exif_dict = exifread.process_file(f)
    
    lon_ref = exif_dict["GPS GPSLongitudeRef"].printable
    lon = exif_dict["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
    if lon_ref != "E":
        lon = lon * (-1)
        
    lat_ref = exif_dict["GPS GPSLatitudeRef"].printable
    lat = exif_dict["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
    if lat_ref != "N":
        lat = lat * (-1)
print('照片的经纬度：', (lat, lon))
