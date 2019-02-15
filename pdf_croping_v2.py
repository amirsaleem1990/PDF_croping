
import os
import img2pdf
from PIL import Image
file_name = input("Enter your PDF file name without .pdf\n")
def to_png(file_name):
	try:
		os.removedirs('newFolderForPictures/')
	except:
		pass
	os.mkdir("newFolderForPictures")
	os.chdir("newFolderForPictures/")
	os.system("pdftoppm ../" +  file_name + ".pdf outputname -png -rx 600 -ry 600")
to_png(file_name)


ls = os.listdir()
try:
	os.removedirs('cropped_files')
	os.mkdir("cropped_files")
except:
	os.mkdir("cropped_files")
def crop(file_name):
	original = Image.open(file_name)
	cropped_example = original.crop((370, 400, 3200, 5100))
	# first argument : left me kahan sy shuru karna h
	# second arugment: upper me kahan sy start karna h
	# third argument: right me kahan tak jana h
	# fourth argument: bottom me kahan tak jana h
	os.chdir("cropped_files/")
	cropped_example.save(file_name.split('-')[1].replace(".png", "")+'_cropped.jpg')
	os.chdir("../")

for i in sorted(ls):
	if i.endswith(".png"):	
		crop(i)


	


def croped_images_to_pdf():
	os.chdir("cropped_files/")
	ls = sorted(os.listdir())
	with open("name.pdf","wb") as f:
	    f.write(img2pdf.convert(ls[:-1]))
	os.system('gio open name.pdf')
croped_images_to_pdf()
# To convert PDF to Image you can use pdftoppm to convert a PDF to a PNG:
# pdftoppm input.pdf outputname -png

# This will output each page in the PDF using the format outputname-01.png, with 01 being the index of the page.


#Converting a single page of the PDF
#pdftoppm input.pdf outputname -png -f {page} -singlefile
#Change {page} to the page number. It's indexed at 1, so -f 1 would be the first page.



#Specifying the converted image's resolution
#The default resolution for this command is 150 DPI. Increasing it will result in both a larger file size and more detail.
#To increase the resolution of the converted PDF, add the options -rx {resolution} and -ry {resolution}. For example:
#pdftoppm input.pdf outputname -png -rx 300 -ry 300
