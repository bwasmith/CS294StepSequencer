X_SIZE = 1200
Y_SIZE = 640
import random
import pygame
#class to store the internal state of the current game board
#meant to hold all state for current application
NUMBER_BEATS = 16
class Model():
	def __init__(self):
		self.current_view = "menu"
		self.view_dict = {}
		self.button_dict = {}
		self.sounds_keys = []

		self.current_pressed = []

		
		#initialize to first menu button
		self.current_cursor = None

		self.play_mark = 0

		self.screen = None

		self.sequences = {}



	def initialize_screen(self):
		pygame.init()
		screen = pygame.display.set_mode((X_SIZE,Y_SIZE))
		self.screen = screen
##MENU
	#initialize all pieces of internal representation for Menu Items
	def initialize_menu_data(self):
		sound_buttons = self.initializeSoundButtons(5)
		all_menu_buttons = [self.createSwitchButton()]
		all_menu_buttons += sound_buttons

		self.add_view_buttons("menu", all_menu_buttons)
		self.current_cursor = self.button_dict[self.current_view][0]


	def initializeSoundButtons(self, num):
		x_spacing = X_SIZE/(num+2)
		button_start = x_spacing
		square_size = x_spacing*2/3
		y = 500

		ls = []
		for i in range(0,num):
			b = Button()
			b.x = button_start
			b.y = y
			b.size = square_size
			button_start += x_spacing
			ls.append(b)
			if i < len(self.sound_keys):
				b.sound = self.sound_keys[i]
			
		return ls

	def initializeSoundService(self, s):
		self.sound_keys = s.sound_dict.keys()


##PLAY
	def initialize_play_data(self):
		play_stream = self.initializePlayStream(3,8)

		all_play_buttons = [self.createSwitchButton()]
		# all_play_buttons += play_buttons

		self.add_view_buttons("play", all_play_buttons)

	def initializePlayButtons(self, num):
		return 

	def initializePlayStream(self, num1, num2):

		return 


#GENERAL FUNCTION
	def add_view_buttons(self, view_type, buttons):
		self.button_dict[view_type] = buttons

	#to add views to the space
	def setView(self, view_type, view):
		self.view_dict[view_type] = view

	def getCurrentView(self):
		return self.view_dict[self.current_view]

	def clearCursor(self):
		self.current_cursor = None

	def getSoundButtons(self):
		return self.sound_buttons

	def createSwitchButton(self):
		b = Button()
		b.x = 15
		b.y = 15
		b.size = 40
		b.switch = True
		return b

	def createButton(self):
		return Button()

	def initializeSequences(self):
		num_pressed = len(self.current_pressed)
		
		for button in self.button_dict["play"]:
			sequence = []
			for i in range(0, NUMBER_BEATS):
				button.sequence_booleans[0] = 0

class Button():
	def __init__(self):
		self.color = (random.randint(10,255), random.randint(10,255),random.randint(10,255))
		self.x = None
		self.y = None
		self.size = None
		self.sound = None
		self.pressed = False
		self.switch = False
		self.sequence_booleans = [0]* NUMBER_BEATS



