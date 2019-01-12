#!/usr/bin/env python3
'''
This is a script to normalize Kodak PhotoCD image files that have an unusual
but documented history: 

First the files were created on a proprietary Kodak PhotoCD. 
Second the files were read on a CD-ROM drive on a Macintosh running Mac OS9.x
The Mac operating system did some funny stuff to the files:
- the .PCD file was wrapped as a QuickTime Image File (QTIF)
- the QTIF resource was then wrapped as a PICT resource, which was readable
  by Mac OS9

This script uses `deark` to read the PICT, then the QTIF, 
then it uses `imagemagick` to convert the original PCD file
to PNG, then again from PNG to TIFF. This is necessary because of some
unusual colorspace issues with PCD, which can't be converted as-is to TIFF.

Both these programs need to be available on your Python path (e.g. `/usr/local/bin`)
Put the script into the folder w the image files, then run `python3 pcdExtractor.py`
'''
import os
import subprocess

for base in os.listdir('.'):
	# assumes everything in the directory other than this file
	# is a PCD you want to extract.
	if not base.startswith('.'):
		if not base.endswith('py'):
			here = os.path.abspath('.')
			path = os.path.abspath(base)
			## INTERMEDIARY IMAGE PATHS
			qtifPath = path+'.000.qtif'	# this is extracted by `deark`
			pcdPath = path+'.000.pcd'	# then this is extracted by `deark`
			pngPath = path+'.png'		# this is output by `magick`
			tiffPath = path+'.tif'		# then so is this, it's the final output


			###
			### DEARK
			###

			# The first pass extracts the QTIF 
			deark1 = [
				'deark',
				'-o',base,
				path
			]
			subprocess.run(deark1)

			# The second pass extracts the underlying PCD
			deark2 = [
				'deark',
				'-o',base,
				qtifPath
			]
			subprocess.run(deark2)

			###
			### IMAGEMAGICK
			### 

			# The first pass converts the PCD to a PNG
			magick1 = [
				'magick',
				pcdPath+'[6]',
				pngPath
			]
			subprocess.run(magick1)

			# The second pass coverts the PNG to TIFF
			magick2 = [
				'magick',
				pngPath,
				tiffPath
			]
			subprocess.run(magick2)

			###
			### NOW CLEAN UP THE INTERMEDIATE FILES
			###
			for residual in (path,qtifPath,pcdPath,pngPath):
				os.remove(residual)

