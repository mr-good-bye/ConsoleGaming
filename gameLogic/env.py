from loguru import logger
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class Map:
	def __init__(self, pos=None, bitmap=None):
		"""
		Class of map, implementing its bitmap and store links to @images@
		:param pos:    tuple (x, y)
		:param bitmap: existing bitmap  -> list[y][x]
		"""
		if bitmap:
			logger.trace("Creating from bitmap")
			self.bitmap = bitmap
			self.y = len(self.bitmap)
			self.x = max([len(i) for i in self.bitmap])
			return
		self.bitmap = [[' ' for _ in range(self.x)] for _ in range(self.y)]  # bitmap[y][x]
		self.x = pos[0]
		self.y = pos[1]
		logger.debug(f" Created map with x={self.x}, y={self.y}")

	def show(self):
		"""
		Print bitmap in console
		:return: None
		"""
		cls()
		for raw in self.bitmap:
			print(*raw, sep='')
		logger.debug("Printed bitmap")

	def get(self, pos=None):
		"""
		Getter of bitmap
		:param pos: -optional- tuple (x, y)
		:return: if no x or y -> bitmap[][] else bitmap[y][x]->char
		"""
		if pos:
			return self.bitmap[pos[1]][pos[0]]
		else:
			return self.bitmap

	def set(self, pos, char):
		"""
		Sets character at given position
		:param pos:    tuple (x, y)
		:param char:
		:return: None
		"""
		if len(char) != 1:
			raise ValueError("Must be exactly one character")
		self.bitmap[pos[1]][pos[0]] = char

	def overlap(self, pos, bitmap):
		"""
		overwrites map bitmap with given bitmap starting from given position
		:param pos:    tuple (x, y)
		:param bitmap: Must be list inside a list of chars
		:return: None
		"""
		posX, posY = len(bitmap[0]), len(bitmap)
		x, y = pos
		if x+posX >= self.x or y+posY >= self.y:
			logger.critical("Given wrong image")
			raise IndexError("given bitmap out of borders of map")
		logger.debug("Overlapping ran")
		curX, curY = pos
		for row in bitmap:
			for char in row:
				self.bitmap[curY][curX] = char
				curX += 1
			curY += 1
			curX = pos[0]


class Player:
	def __init__(self, lev, pos=(1, 1), char='@'):
		"""
		Creates instance of Player
		:param lev: Map of player
		:param pos: Start position of player 1,1 by default
		:param char: Player character (One char)
		"""
		if len(char) != 1:
			raise ValueError("Must be exactly one character")
		self.x = pos[0]
		self.y = pos[1]
		self.char = char
		self.map = lev
		logger.debug("Created player")

	def move(self, goto):
		"""
		Moves player
		:param goto: up, left, right, down
		:return: None
		"""
		if goto == 'up':
			self.y -= 1
			if self.map.get((self.x, self.y)) != ' ':
				self.y += 1
			else:
				self.map.set((self.x, self.y+1), ' ')
		elif goto == 'down':
			self.y += 1
			if self.map.get((self.x, self.y)) != ' ':
				self.y -= 1
			else:
				self.map.set((self.x, self.y-1), ' ')
		elif goto == 'left':
			self.x -= 1
			if self.map.get((self.x, self.y)) != ' ':
				self.x += 1
			else:
				self.map.set((self.x+1, self.y), ' ')
		elif goto == 'right':
			self.x += 1
			if self.map.get((self.x, self.y)) != ' ':
				self.x -= 1
			else:
				self.map.set((self.x-1, self.y), ' ')
		self.map.set((self.x, self.y), self.char)

