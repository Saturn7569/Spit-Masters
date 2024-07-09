import pygame, os, json

BASE_IMG_PATH = "data/images/"

def load_sprite(path, colorkey=None):
    img = pygame.image.load(BASE_IMG_PATH + path)
    if colorkey != None: img.set_colorkey(colorkey)
    return img

def load_sprites(path, colorkeys=None):
    images = []
    for name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_sprite(path + "/" + name, colorkeys))
    return images

def load_json(path):
    fl = open(path, 'r')
    data = json.load(fl)
    fl.close()
    return data