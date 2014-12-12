import pygame

X_SIZE = 1000
Y_SIZE = 640
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
		y_difference = (Y_SIZE-200)/(num_buttons-1)
		index = 0
		for button in self.model.button_dict["play"]:
			if button.switch:
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["orange"],(button.x, button.y, button.size, button.size))
			else:
				pygame.draw.rect(self.model.screen, button.color,(100, y_start + index * y_difference, button.size, button.size))
				index += 1
		


	def displayPlayMarkers(self):
		location = self.model.play_mark
		pygame.draw.circle(self.model.screen, pygame.color.THECOLORS["pink"],(300 + location*self.model.play_difference, 100), 10)
		for i in range(0,8):
			pygame.draw.line(self.model.screen, pygame.color.THECOLORS["pink"],(300 + i*self.model.play_difference, 115), (300+i*self.model.play_difference,Y_SIZE),2)
