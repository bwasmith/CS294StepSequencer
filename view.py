import pygame

X_SIZE = 1200
Y_SIZE = 640
NUMBER_BEATS = 16

#mean to display the current state (from model) of the applicationw
class View():
	def __init__(self):
		self.model = None
		pass

	#abstract method which all View Subclasses will implement
	def display(self):
		self.model.screen.fill((0,100,0))
		pygame.display.flip()
		pass

	#will take the input from the main, and will send event to the controller
	def takeInput(self,event):
		self.controller.handleEvent(event)

	def displayCurrentCursor(self):
		button = self.model.current_cursor
		pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["yellow"], (button.x-10,button.y-10,button.size+20,button.size+20),8)

class Menu_View(View):
	def __init__(self, model,controller):
		self.model = model
		self.text = ""
		self.controller = controller
	
	#when input is give, it is passed on to particular view, then passed forward to appropriate control handler
	def takeInput(self,event):
		print "handling menu event"
		self.controller.handleMenuEvent(event)

	def display(self):
		self.model.screen.fill((50,0,50))

		self.displayCurrentCursor()
		self.displayMenuButton()

		pygame.display.flip()


		#if its pressed, place a pressed button
			#if not, regular button
		#go to the model, get the current cursor position
		#place the correct thing around cursor position
	def displayMenuButton(self):
		for button in self.model.button_dict["menu"]:
			if button.switch:
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["orange"],(button.x, button.y, button.size, button.size))
			elif (button.pressed):
				pygame.draw.rect(self.model.screen, button.color,(button.x, button.y, button.size, button.size))
			else:
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["red"],(button.x, button.y, button.size, button.size))

class Play_View(View):
	def __init__(self, model,controller):
		self.model = model
		self.text = ""
		self.controller = controller

	def takeInput(self, event):
		print "handling play event"
		self.controller.handlePlayEvent(event)

	def display(self):
		self.model.screen.fill((0,0,0))
		self.displayCurrentCursor()
		self.displayPlayButtons()
		self.displayPlayMarkers()

		pygame.display.flip()




	#will display the switch button
	#as well as current menu buttons
	def displayPlayButtons(self):
		num_buttons = len(self.model.current_pressed)
		y_start = 200
		index = 0
		for button in self.model.button_dict["play"]:
			if button.switch:
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["orange"],(button.x, button.y, button.size, button.size))
			else:
				pygame.draw.rect(self.model.screen, button.color,(button.x, button.y, button.size, button.size))
				index += 1
		
	def displayPlayMarkers(self):
		location = self.model.play_mark
		x_start = 250
		x_difference = (X_SIZE - x_start)/(NUMBER_BEATS+1)
		pygame.draw.circle(self.model.screen, pygame.color.THECOLORS["pink"],(x_start + location * x_difference, 100), 10)




		for i in range(0,NUMBER_BEATS):
			x_offset = x_start + i * x_difference
			pygame.draw.line(self.model.screen, pygame.color.THECOLORS["darkseagreen4"],(x_offset, 115), (x_start + i * x_difference,Y_SIZE),3)
			for button in self.model.button_dict["play"]:
				if button.switch:
					continue
				if button.sequence_booleans[i]:
					pygame.draw.circle(self.model.screen, button.color,(x_offset, button.y), 8)
		#need to display all the current markers at this period in time 
		#iterate through each button
			#for each button, iterate over the sequence booleans, print a small circle of button color if True









