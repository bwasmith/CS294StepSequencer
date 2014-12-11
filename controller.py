import pygame
#meant to do all controlled actions for the application
class Controller():
	def __init__(self, model):
		self.model = model
		self.view = None


	#will be called from view's takeInput function
	#will make appropriate changes to the model
	def handleEvent():
		pass

	def switchView(self, view_type):
		print "switching to this view!", view_type
		self.model.current_view = view_type
		self.model.current_cursor = self.model.button_dict[view_type][0]

	def handleMenuEvent(self, event):
		buttons = self.model.button_dict["menu"]
		current = self.model.current_cursor
		if event.key == pygame.K_LEFT:
			self.model.current_cursor = self.shift_cursor(current, buttons, True)
		elif event.key == pygame.K_RIGHT:
			self.model.current_cursor = self.shift_cursor(current, buttons, False)
		elif event.key == pygame.K_RETURN:
			if self.model.current_cursor.switch == True:
				self.switchView("play")
			else:
				self.model.current_cursor.pressed = not self.model.current_cursor.pressed

	def handlePlayEvent(self, event):
		buttons = self.model.button_dict["play"]
		current = self.model.current_cursor
		if event.key == pygame.K_LEFT:
			self.model.current_cursor = self.shift_cursor(current, buttons, True)
		elif event.key == pygame.K_RIGHT:
			self.model.current_cursor = self.shift_cursor(current, buttons, False)
		elif event.key == pygame.K_RETURN:
			if self.model.current_cursor.switch == True:
				self.switchView("menu")
			else:
				self.model.current_cursor.pressed = not self.model.current_cursor.pressed




	def shift_cursor(self, current_cursor, all_buttons, left):
		index = all_buttons.index(current_cursor)
		if left:
			if index > 0:
				return all_buttons[index - 1]
			else:
				return all_buttons[len(all_buttons) - 1]
		else:
			if index < len(all_buttons)-1:
				return all_buttons[index + 1]
			else:
				return all_buttons[0]
