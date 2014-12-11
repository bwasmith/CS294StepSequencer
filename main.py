import pygame
import view, controller, model



m = model.Model()
m.initialize_screen()

c = controller.Controller(m)

menu_v = view.Menu_View(m,c)
menu_v.display()
m.setView("menu",menu_v)


play_v = view.Play_View(m,c)
m.setView("play", play_v)

c.switchView("menu")

#initial view
v = m.getCurrentView()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
        	v.takeInput(event)
        	v = m.getCurrentView()
        	print m.current_view, "current view"
        	v.display()

pygame.quit()
