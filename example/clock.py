#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011-07-28 14:31:13  pkrawczak@gmail.com



import gui, time, pygame
from math import sin, cos, radians

class Clock(pygame.Surface):

	size = (200, 200)

	def __init__(self):
		pygame.Surface.__init__(self, self.size)
		
		self.hand_color = (255, 200, 0)
		self.dots_color = (255, 100, 0)
		self.background_color = (100, 0, 0)
		#self.background_image = pygame.image.load("back.png")
		self.pos = (0, 0)
		self.hand_length = 100
		
	def blit_on(self, surface):
		self.fill(self.background_color)
		if not self.background_image == None: self.blit(self.background_image, (0,0))
		self.blit_hands()
		self.blit_dots()
		surface.blit(self, self.pos)
	
	def blit_dots(self):
		# standard coords of 12:00:00
		x = 0
		y = self.hand_length - 10
		for i in xrange(1, 13):
			angle = i * 30
			point = self.screen_point(self.rotated((x,y), angle))
			pygame.draw.circle(self, self.dots_color, point, 4)
		for i in xrange(1, 61):
			angle = i * 6
			point = self.screen_point(self.rotated((x,y), angle))
			self.set_at(point, self.dots_color)
	
	def blit_hands(self):
		now = time.localtime()
		# standard coords of 12:00:00
		x = 0
		y = self.hand_length
		
		second = now.tm_sec
		minute = now.tm_min + second / 60.
		hour = now.tm_hour + minute / 60.
		
		if hour > 12: hour = hour - 12
		hour_angle = hour * 30
		hour_point = self.screen_point(self.rotated((x, y - 40), hour_angle))
		pygame.draw.aaline(self, self.hand_color, self.screen_point((0, 0)), hour_point, 1)
			
		minute_angle = minute * 6
		minute_point = self.screen_point(self.rotated((x, y - 20), minute_angle))
		pygame.draw.aaline(self, self.hand_color, self.screen_point((0, 0)), minute_point, 1)
		
		second_angle = second * 6
		second_point = self.screen_point(self.rotated((x, y), second_angle))
		pygame.draw.aaline(self, self.hand_color, self.screen_point((0, 0)), second_point, 1)
		
	def rotated(self, point, angle):
		x, y = point
		angle = radians(-angle)
		rotated_x = int(x * cos(angle) - y * sin(angle))
		rotated_y = int(x * sin(angle) + y * cos(angle))
		return (rotated_x, rotated_y)
		
	def screen_point(self, point):
		x, y = point
		x_p = x + self.size[0] / 2
		y_p = -y + self.size[1] / 2
		return (x_p, y_p)
		
	
class ClockGUI(gui.GUI):

	size = (200, 200)
	
	def __init__(self):
		gui.GUI.__init__(self, self.size)
		pygame.display.set_caption("clock")
		pygame.mouse.set_visible(True)
		
		clock = Clock()
		self.components.append(clock)
		
		
if __name__ == "__main__":
	cg = ClockGUI()
	cg.start()
	
	
	
	
