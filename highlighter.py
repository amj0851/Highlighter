import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import glob

def main():
	#create a list of all xml files in this folder
	files = glob.glob('*.xml')
	
	for xml_file in files:
		#account for broken xml files
		try:
			tree = ET.parse(xml_file)
		except:
			print("Error parsing, skipping file: "+ xml_file +" ")
			continue
		
		#grab matching png file
		png_file = xml_file[:-4]+'.png'

		#setup for finding leaf components
		root = tree.getroot()
		leafs = []

		#Recursively search through the tree for components with no children
		def recursive(root):
			root_len = len(root)
			if (root_len<1):
				#found a leaf component
				leafs.append(root)
				return
			for x in range(root_len):
				temp = root[x]
				recursive(temp)

		recursive(root)

		#draw a box around the bounds of each leaf components
		try:
			image = Image.open(png_file)
		except:
			print("Couldn't find matching png, skipping file: "+xml_file)
			continue
		draw = ImageDraw.Draw(image)
		for x in leafs:
			
			#Get the bounds of the component
			bounds = x.get('bounds')

			#clean it up
			bounds = bounds.replace('[', '')
			bounds = bounds.replace(']', ' ')
			bounds = bounds.replace(',', ' ')
			barr = bounds.split()
			
			#parse out coordinates	
			x1 = int(barr[0])
			x2 = int(barr[2])
			y1 = int(barr[1])
			y2 = int(barr[3])

			draw.rectangle((x1, y1, x2, y2), width = 5, outline = "yellow")
			

		#save the final image
		image.save(png_file[:-4]+"_result.png")

	#show successful completion
	print("Results saved to folder")


main()


	