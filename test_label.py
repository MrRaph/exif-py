from exifread import process_file, exif_log, __version__
from fractions import Fraction
# Open image file for reading (binary mode)
f = open('P1700081.jpeg', 'rb')

# Return Exif tags
tags = process_file(f)
Model, LensType, Speed, ISO = '', '', '', ''
for tag in tags.keys():
    if tag in ('MakerNote LensType'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        LensType = tags[tag]
    if tag in ('Image Model'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        Model = tags[tag]
    if tag in ('EXIF ISOSpeedRatings'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        ISO = tags[tag]
    if tag in ('EXIF ExposureTime'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        Speed = tags[tag]
    if tag in ('EXIF ExposureTime'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        Speed = tags[tag]
    if tag in ('EXIF FocalLength'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        Focal = tags[tag]
    if tag in ('EXIF FNumber'):
        print("Key: %s, value %s" % (tag, tags[tag]))
        FNumber = tags[tag]
        FNumber = float(Fraction(str(FNumber)))

print("Pris avec Lumix %s (%s), Focal : %s mm, Ouverture : %s, Speed : %s seconde(s), ISO : %s" % (Model, LensType, Focal, FNumber, Speed, ISO))