### imgOut
Utility to export images out of sqlite databases

### Usage

imgOut.py accepts 2 parameters to select the database and output directory, the output directory is optional and will default to images. If the directory does not exist the script will attempt to create it.

you can use -h or --help for details.

##assumptions 
The script assumes that your Table is called images and that it has three columns id, imgData, filename. if your table differs you'll need to modify the script to match your setup.

## Example

`$ python imgOut.py -d myimages.db -o images`

the above example will select the myimages database and output the images into the images directory in the same directory as the script.