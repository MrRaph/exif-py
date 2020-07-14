"""
Makernote (proprietary) tag definitions for Panasonic.

https://exiftool.org/TagNames/Panasonic.html
"""

TAGS = {
    0x0001: ('ImageQuality', {
        1: 'TIFF',
        2: 'High',
        3: 'Normal',
        6: 'Very High',
        7: 'RAW',
        9: 'Motion Picture',
        11: 'Full HD Movie',
        12: '4k Movie',
    }),
    0x0002: ('FirmwareVersion',),
    0x0003: ('WhiteBalance',{
        1: 'Auto',
        2: 'Daylight',
        3: 'Cloudy',
        4: 'Incandescent',
        5: 'Manual',
        8: 'Flash',
        10: 'Black & White',
        11: 'Manual 2',
        12: 'Shade',
        13: 'Kelvin',
        14: 'Manual 3',
        15: 'Manual 4',
        19: 'Auto (cool)',
    }),
    0x0007: ('FocusMode',{
        1: 'Auto',
        2: 'Manual',
        4: 'Auto, Focus button',
        5: 'Auto, Conitnuous',
        6: 'AF-S',
        7: 'AF-C',
        8: 'AF-F',
    }),
    0x0028: ('ColorEffect',{
        1: 'Off',
        2: 'Warm',
        3: 'Cool',
        4: 'Black & White',
        5: 'Sepia',
        6: 'Happy',
        8: 'Vivid',
    }),
    0x0051: ('LensType',),
    0x00ac: ('MonochromeFilterEffect', {
        0: 'Off',
        1: 'Yellow',
        2: 'Orange',
        3: 'Red',
        4: 'Green',
    }),
}
