import pygame

X_SIZE = 800
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
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["green"],(button.x, button.y, button.size, button.size))
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
		self.model.screen.fill((0,50,0))
		self.displayCurrentCursor()
		self.displayPlayButton()
		
		pygame.display.flip()



	def displayPlayButton(self):
		for button in self.model.button_dict["play"]:
			if button.switch:
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["orange"],(button.x, button.y, button.size, button.size))
			elif (button.pressed):
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["green"],(button.x, button.y, button.size, button.size))
			else:
				pygame.draw.rect(self.model.screen, pygame.color.THECOLORS["red"],(button.x, button.y, button.size, button.size))



