from designer import *
from dataclasses import dataclass
# Put imports at the top of the file
from random import randint

@dataclass
class World:
    copter: DesignerObject
    copter_speed: int
    drops: list[DesignerObject]
    fires: list[DesignerObject]


# Set initial speed of the copter
COPTER_SPEED = 5
# Set the speed of the water drops
WATER_DROP_SPEED = 5


def create_world() -> World:
    """ Create the world """
    return World(create_copter(), COPTER_SPEED, [], [])


def create_copter() -> DesignerObject:
    """ Create the copter """
    copter = emoji("helicopter")
    copter.y = get_height() * (1 / 3)
    copter.flip_x = True
    return copter


def move_copter(world: World):
    """ Move the copter horizontally"""
    world.copter.x += ___


def head_left(world: World):
    """ Make the copter start moving left """
    world.copter_speed = -COPTER_SPEED
    world.copter.flip_x = False


def head_right(world: World):
    """ Make the copter start moving right """
    world.copter_speed = COPTER_SPEED
    world.copter.flip_x = True


def bounce_copter(world: World):
    """ Handle the copter bouncing off a wall """
    if world.copter.x > get_width():
        head_left(world)
    elif world.copter.x < 0:
        head_right(world)


def flip_copter(world: World, key: str):
    """ Change the direction that the copter is moving """
    if key == "left":
        ___
    elif key == "right":
        ___


def create_water_drop() -> DesignerObject:
    """ Create a water drop"""
    return circle("blue", ___)


def drop_water(world: World, key: str):
    """ Drop water from directly below the copter when space is pressed. """
    if key == 'space':
        new_drop = create_water_drop()
        move_below(___, world.___)
        world.___.append(___)


def move_below(bottom: DesignerObject, top: DesignerObject):
    """ Move the bottom object to be below the top object """
    bottom.y = ___.y + ___.height/2
    bottom.x = ___.x

def make_water_fall(world: World):
    """ Move all the water drops down """
    for ___ in ___:
        drop.y += WATER_DROP_SPEED


def destroy_waters_on_landing(world: World):
    """ Destroy any water drops that have landed on the ground """
    kept = []
    for drop in world.drops:
        if ___:
            ___.append(___)
        else:
            destroy(___)
    world.drops = kept

def create_fire() -> DesignerObject:
    """ Create a small fire randomly on the screen """
    fire = emoji('🔥')
    fire.scale_x = .1
    fire.scale_y = .1
    fire.anchor = 'midbottom'
    fire.x = randint(___, ___)
    fire.y = get_height()
    return fire

def make_fires(world: World):
    """ Create a new fire at random times, if there aren't enough fires """
    not_too_many_fires = len(___) < ___
    random_chance = randint(___, ___) == ___
    if not_too_many_fires and random_chance:
        world.fires.append(create_fire())


when("starting", create_world)
when("updating", move_copter)
when("updating", bounce_copter)
when("updating", make_water_fall)
when("updating", destroy_waters_on_landing)
when("updating", make_fires)
when("___", flip_copter)
when('typing', drop_water)

start()

