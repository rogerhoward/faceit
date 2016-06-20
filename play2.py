#!/usr/bin/env python
import os
import sys
import sqlite3
from pprint import pprint


base_input_path ='/Users/rogerhoward/Desktop/faces/samples'
base_output_path = '/Users/rogerhoward/Desktop/faces/cropped'


class reg(object):
    values = {}

    def crop_values(self):
        top_left_x = int(self.fileWidth * self.tl_x)
        top_left_y = int(self.fileHeight * self.tl_y)
        width = int((self.tr_x - self.tl_x) * self.fileWidth)
        height = int((self.bl_y - self.tl_y) * self.fileHeight)

        return (top_left_x, top_left_y, width, height)

    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row):
            setattr(self, attr, val)
            self.values[attr] = val


# database_path = '/Volumes/speedo/faces.sqlite'
# database_path = 'catalog/catalog.lrcat'
database_path = '/Users/rogerhoward/Desktop/sample_catalog.lrcat'

query = "select Image, Faces.bl_x, Faces.bl_y, Faces.br_x, Faces.br_y, Faces.tl_x, Faces.tl_y, Faces.tr_x, Faces.tr_y, Faces.imageOrientation,  Image.fileWidth, Image.fileHeight, \
File.baseName || '.jpg' as Filename \
from AgLibraryFace AS Faces \
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face \
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local \
inner join Adobe_images AS Image ON Faces.image = Image.id_local \
inner join AgLibraryFile AS File on Image.rootFile = File.id_local \
where Keyword.name = 'Arthur Thomas Parker' and Faces.imageOrientation = 'AB' \
ORDER BY image"

if __name__ == "__main__":
    conn = sqlite3.connect(database_path)
    row_count = 0
    cursor = conn.execute(query)
    for row in cursor:
        r = reg(cursor, row)
        crop = r.crop_values()

        if crop[3] > 0:
            aspect_ratio = (crop[2] * 1.0) / (crop[3] * 1.0)
            if True:
                template = 'convert {input} -crop {w}x{h}+{tlx}+{tly} {output}'
                input_path = '{}/{}'.format(base_input_path, r.Filename)
                output_path = '{}/{}'.format(base_output_path, r.Filename)
                data = {'input': input_path, 'output': output_path, 'w': crop[2], 'h':crop[3], 'tlx': crop[0], 'tly': crop[1]}
                command = template.format(**data)
                print(command)