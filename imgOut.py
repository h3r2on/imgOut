#!/usr/bin/python
import sqlite3 as sqlite
import os
import optparse


# Create cmdline parser
parser = optparse.OptionParser()

parser.add_option('-d', '--database',
	dest="database",
	default=False,
	help='select the sqlite database to use')

parser.add_option('-o', '--outputdir',
	dest="imagedir",
	default="images")

(options, args) = parser.parse_args()

# Create a new in-memory DB and a cursor
#
con = sqlite.connect(options.database)
cur = con.cursor()
outputdir = options.imagedir
if not os.path.isdir(outputdir):
	os.makedirs(outputdir)

# expecting table images
# expecting at least three columns
# id (int), data(BLOB), filename(string)
for image in cur.execute("select * from images"):


	with open(outputdir + '/' + image[2], "wb") as output_file:
		output_file.write(image[1])

cur.close()
con.close()