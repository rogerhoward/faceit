#!/usr/bin/env python
import os
import sys
import sqlite3
from pprint import pprint

class reg(object):
    values = {}

    def crop_values(self):
        top_left_x = int(self.fileWidth * self.tl_x)
        top_left_y = int(self.fileHeight * self.tl_y)
        crop_horizontal = int(self.fileWidth * self.tr_x) - top_left_x
        crop_vertical = int(self.fileHeight * self.bl_x) -top_left_y

        return (top_left_x, top_left_y, crop_horizontal, crop_vertical)

    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row) :
            setattr(self, attr, val)
            self.values[attr] = val



# database_path = '/Volumes/speedo/faces.sqlite'
database_path = '/Volumes/speedo/catalog/catalog.lrcat'

query = "select Folder.pathFromRoot, File.baseName, File.extension, Img.fileWidth, Img.fileHeight, Hist.*, Faces.*, Keyword.name \
from  Adobe_libraryImageFaceProcessHistory AS Hist \
inner join Adobe_images AS Img ON Hist.image = Img.id_local \
inner join AgLibraryFile AS File on  Img.rootFile = File.id_local \
inner join AgLibraryFolder AS Folder on File.folder = Folder.id_local \
inner join AgLibraryFace AS Faces on Hist.image = Faces.image \
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face \
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local"
# where Keyword.name = 'Arthur Thomas Parker' LIMIT 100"

if __name__ == "__main__":
    conn = sqlite3.connect(database_path)
    # c = conn.cursor()
    row_count = 0
    cursor = conn.execute(query)
    for row in cursor:
        r = reg(cursor, row)
        row_count += 1
        pprint(r.values)
        crop = r.crop_values()
        pprint(crop)

        if crop[3] > 0:
            aspect_ratio = crop[2] / crop[3]
            if aspect_ratio < 1.33 and aspect_ratio > 0.75:
                print('good size')

                template = 'convert {input} -crop {w}x{h}+{tlx}+{tly} {output}'

                input_path = '/Volumes/Projects/faces/arthur/{}.jpg'.format(r.baseName)
                output_path = '/Volumes/Projects/faces/arthur/_crops/{}.jpg'.format(r.baseName)

                data = {'input': input_path, 'output': output_path, 'w': crop[2], 'h':crop[3], 'tlx': crop[0], 'tly': crop[1]}
                command = template.format(**data)
                print(command)
    # print row_count