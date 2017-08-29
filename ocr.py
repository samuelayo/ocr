from PIL import Image
from wand.image import Image as wandimage
import pyocr
import pyocr.builders
import io
import os.path
import sys

imagepath = ''
if len(sys.argv) > 1:
	    imagepath = sys.argv[1]    
else:
    print("please specify an input file. image or pdf format only")
    exit()

def ocr_image(imagepath):
	tool = pyocr.get_available_tools()[0]
	text = ''
	pdf_list = []
	
	try:
	    im = Image.open(imagepath)
	    if im is not None:
	    	text = tool.image_to_string(
				        im,
				        lang='eng',
				        builder=pyocr.builders.TextBuilder()
				    )
	except:
		try:
			
			if os.path.isfile(imagepath): 
				im = wandimage(filename=imagepath, resolution=300)
			else:
				#print("input file not a valid image or pdf")
				exit()
			if im is not None:
				im.convert('jpeg')
				for img in im.sequence:
				    img_page = wandimage(image=img)
				    pdf_list.append(img_page.make_blob('jpeg'))
				for img in pdf_list: 
				    txt = tool.image_to_string(
				        Image.open(io.BytesIO(img)),
				        lang='eng',
				        builder=pyocr.builders.TextBuilder()
				    )
				    text = text + txt
			    
		except:
		    print("input file not a valid image or pdf")
		    exit()
	return text

if __name__ == '__main__':
	result = ocr_image(imagepath)
	print(result)
