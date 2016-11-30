class CarSprite(pygame.sprite.Sprite):
    def __init__(self, image, position, minSpeed):
	pygame.sprite.Sprite.__init__(self)
	self.src_image = pygame.image.load(image)
	self.position = position
    def update():
	self.position[0] -= rand.randint(minSpeed, 64)
