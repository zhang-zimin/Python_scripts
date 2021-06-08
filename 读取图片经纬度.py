import exifread
import os

path = r'E:\OneDrive - HHU\西霞院\照片'
文件列表 = []
a= os.listdir(path)
for i in a:
    path = rf'E:\OneDrive - HHU\西霞院\照片\{i}'
    文件列表.append(path)
for path in 文件列表:
    try:
        with open(path, 'rb') as f:
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
            print(lat,lon)
    except KeyError:
        print('照片不含GPS信息,检查照片是否为原图')
