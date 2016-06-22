#!/usr/bin/env python
import os
import sys
import sqlite3
import simplejson as json
import click
from sh import exiftool
from sh import convert
from pprint import pprint


class Image(object):
    path = None
    metadata = None
    people = None
    regions = None
    width = None
    Height = None

    def get_metadata(self):
        if self.path is not None:
            et_out = exiftool('-struct', '-g', '-J', self.path)
            self.metadata = json.loads(et_out.encode("utf-8", "strict"))[0]
            self.map_metadata()
            self.get_people()

    def map_metadata(self):
        try:
            self.width = self.metadata['XMP']['RegionInfo']['AppliedToDimensions']['W']
            self.height = self.metadata['XMP']['RegionInfo']['AppliedToDimensions']['H']
        except:
            pass

    def get_people(self):
        try:
            pprint(self.metadata['XMP']['RegionInfo'])
            self.regions = self.metadata['XMP']['RegionInfo']['RegionList']
            self.people = list(map(lambda x: x['Name'], self.regions))
        except KeyError:
            pass

    def __str__(self):
        people_string = ', '.join(self.people) if self.people is not None else 'No one'
        return '{people} found in {path}'.format(people=people_string, path=self.path)

    def __init__(self, path):
        self.path = path
        self.get_metadata()


@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path):
    this_image = Image(path)
    print(this_image)
    pprint(this_image.regions)

if __name__ == "__main__":
    main()