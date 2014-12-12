import pygame
import view, controller, model, sound_service

s = sound_service.SoundService()

m = model.Model()
m.initialize_screen()
m.initializeSoundService(s)
m.initialize_menu_data()
m.initialize_play_data()

c = controller.Controller(m,s)

menu_v = view.Menu_View(m,c)
menu_v.display()
m.setView("menu",menu_v)


play_v = view.Play_View(m,c)
m.setView("play", play_v)

c.switchView("menu")

#initial view
v = m.getCurrentView()

running = True

clock = pygame.time.Clock()
time = 0
while running:
    if time > 500:
        time = 0
        if m.current_view == "play":
            c.iteratePlay()
            v.display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
        	v.takeInput(event)
        	v = m.getCurrentView()
        	print m.current_view, "current view"
        	v.display()
    time += clock.tick(1000)
    print time

s.release()

pygame.quit()
