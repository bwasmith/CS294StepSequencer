import pygame
#meant to do all controlled actions for the application
X_SIZE = 1200
Y_SIZE = 640
NUMBER_BEATS = 16

class Controller():
	def __init__(self, model, sound_service):
		self.model = model
		self.view = None
		self.sound_service = sound_service


	#will be called from view's takeInput function
	#will make appropriate changes to the model
	def handleEvent():
		pass

	#for switching to menu, just switches to that view
	#for play, need to update the current pressed buttons
	def switchView(self, view_type):
		print "switching to this view!", view_type
		self.model.current_view = view_type
		self.model.current_cursor = self.model.button_dict[view_type][0]
		if view_type == "play":
			#need to set the play buttons = to the current pressed buttons
			menu_button = self.model.button_dict["play"].pop(0)
			if not menu_button.switch:
				print "there was an error!"
			play_b = [menu_button]
			play_b += self.createPlayButtons()
			self.model.button_dict["play"] = play_b
			self.model.initializeSequences()

	def createPlayButtons(self):
		new_play_list = []
		pressed = self.model.current_pressed
		num_pressed = len(pressed)
		if num_pressed == 0:
			return []

		y_start = 150
		y_difference = (Y_SIZE - y_start)/(num_pressed)
		index = 0
		for button in pressed:
			new_play_button = self.model.createButton()
			new_play_button.x = 100
			new_play_button.y = y_start + index*y_difference
			new_play_button.color = button.color
			new_play_button.size = button.size*2/3
			new_play_button.sound = button.sound
			index += 1

			new_play_list.append(new_play_button)
		return new_play_list


	def iteratePlay(self):
		#playing logic
		#for each current pressed, if its play mark index is a 1, then add to a list
		sound_list = []
		for button in self.model.button_dict["play"]:
			if button.switch:
				continue
			if button.sequence_booleans[self.model.play_mark]:
				sound_list.append(button.sound)
		print sound_list
		self.sound_service.playSounds(sound_list)
		#play the whole list
		self.model.play_mark += 1
		if self.model.play_mark > (NUMBER_BEATS - 1):
			self.model.play_mark = 0

		


	def handleMenuEvent(self, event):
		buttons = self.model.button_dict["menu"]
		current = self.model.current_cursor
		if event.key == pygame.K_LEFT:
			self.model.current_cursor = self.shift_cursor(current, buttons, True)
		elif event.key == pygame.K_RIGHT:
			self.model.current_cursor = self.shift_cursor(current, buttons, False)
		elif event.key == pygame.K_RETURN:
			if current.switch == True:
				self.switchView("play")
			else:
				self.pressMenuButton()
		elif event.key == pygame.K_UP:
			if not current.switch:
				if current.sound == None:
					print "error!"
					return
				self.sound_service.playSounds([current.sound])
		elif event.key == pygame.K_0:
			self.sound_service.playSound()
		elif event.key == pygame.K_9:
			self.sound_service.playOtherSound()
		elif event.key == pygame.K_8:
			self.sound_service.playOtherSound()
			self.sound_service.playSound()
		elif event.key == pygame.K_7:
			self.sound_service.playSound()
			self.sound_service.playOtherSound()
		elif event.key == pygame.K_6:
			self.sound_service.playSounds(["808-clap.wav","elrdrum.wav"])




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
				self.pressPlayButton()

	def pressMenuButton(self):
		#current cursor should be pressed
		pressed_buttons = self.model.current_pressed
		cursor = self.model.current_cursor

		if not cursor.pressed:
			cursor.pressed = True
			pressed_buttons.append(cursor)
		else:
			cursor.pressed = False
			pressed_buttons.pop(pressed_buttons.index(cursor))

		if len(pressed_buttons) > 3:
			popped = pressed_buttons.pop(0)
			popped.pressed = False

		if pressed_buttons != self.model.current_pressed:
			print "ERROR WITH REFERENCE PASS"

	#needs to add a step to the step sequencer
	#the current index is being stored in the model
	#will get it and change the current cursor's sequence_booleans
	def pressPlayButton(self):
		current_index = self.model.play_mark
		self.model.current_cursor.sequence_booleans[current_index] = not self.model.current_cursor.sequence_booleans[current_index]



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

