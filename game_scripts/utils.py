import os
import pygame

# PATH OF THE IMAGES
BASE_IMG_PATH = 'game_assets/images/'

# LOAD IMAGES
def load_image(path):
	"""
	.convert():
		CONVERT THE INTERNAL REPRESENTATION OF AN IMAGE
		TO MAKE IT MORE EFFICIENT FOR RENDERING
	"""
	img = pygame.image.load(BASE_IMG_PATH + path).convert()

	# REFRESH SURFACE TO PREVENT RENDERING AN IMAGE ONTO ITSELF ON A PREVIOUS FRAME
	img.set_colorkey((0, 0, 0))
	return img

# RENDER MULTIPLE IMAGES IN THE SAME DIRECTORY
def load_images(path):
	# INITIALIZE AN EMPTY LIST
	images = []

	# os.listdir takes a path and gives you all the files in it
	for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
		images.append(load_image(path + '/' + img_name))
	
	# RETURN THE IMAGES AS A LIST
	return images

