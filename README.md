# bampfa-scripts
scripts for bampfa digital preservation and digital asset management


# pcdExtrator.py

This is a script to normalize Kodak PhotoCD image files that have an unusual
but documented history: 

First the files were created on a proprietary Kodak PhotoCD. Second, the files were read on a CD-ROM drive on a Macintosh running Mac OS9.x. The Mac operating system did some funny stuff to the files:
* the .PCD file was wrapped as a QuickTime Image File (QTIF)
* the QTIF resource was then wrapped as a PICT resource, which was readable
by Mac OS9

This script uses [`deark`](https://github.com/jsummers/deark) to read the PICT, then the QTIF, then it uses [`imagemagick`](http://www.imagemagick.org/) to convert the original PCD file to PNG, then again from PNG to TIFF. This is necessary because of some
unusual colorspace issues with PCD, which can't be converted as-is to TIFF.

Both these programs need to be available on your Python path (e.g. `/usr/local/bin`)
Put the script into the folder w the image files, then run `python3 pcdExtractor.py`

See [this blog post](https://mcampos-quinn.github.io/2018/12/20/pcd-normalization.html) about the process of converting these files. 
