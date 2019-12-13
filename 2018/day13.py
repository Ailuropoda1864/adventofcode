day = 13

###############################
from read_input import *
from collections import deque

input_string = get_input_string(day)


class Cart:
    CARTS = {
        '^': 'up',
        'v': 'down',
        '<': 'left',
        '>': 'right'
    }

    CHANGE_DIRECTION_AT_CURVE = {
        ('/', 'up'): 'right',
        ('/', 'down'): 'left',
        ('/', 'left'): 'down',
        ('/', 'right'): 'up',
        ('\\', 'up'): 'left',
        ('\\', 'down'): 'right',
        ('\\', 'left'): 'up',
        ('\\', 'right'): 'down'
    }

    CHANGE_DIRECTION_AT_INTERSECTION = {
        ('left', 'up'): 'left',
        ('left', 'down'): 'right',
        ('left', 'left'): 'down',
        ('left', 'right'): 'up',
        ('right', 'up'): 'right',
        ('right', 'down'): 'left',
        ('right', 'left'): 'up',
        ('right', 'right'): 'down'
    }

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.direction = self.CARTS[symbol]
        self.turns = deque(['left', 'straight', 'right'])

    def __repr__(self):
        return '(({},{}), {})'.format(self.x, self.y, self.direction)

    def update_direction(self, symbol):
        if symbol == '+':
            if self.turns[0] != 'straight':
                self.direction = self.CHANGE_DIRECTION_AT_INTERSECTION[(self.turns[0], self.direction)]
            self.turns.rotate(-1)
        elif symbol in '/\\':
            self.direction = self.CHANGE_DIRECTION_AT_CURVE[(symbol, self.direction)]

    def move(self):
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1


class Track:
    def __init__(self):
        self.carts = []
        self.turns = {}

    def sort_carts(self):
        self.carts.sort(key=lambda cart: cart.x)
        self.carts.sort(key=lambda cart: cart.y)

    def map_cart_position_to_cart(self, x, y):
        return [cart for cart in self.carts if cart.x == x and cart.y == y]

    def get_cart_positions(self, exclude_idx=[]):
        return [(cart.x, cart.y) for idx, cart in enumerate(self.carts) if idx not in exclude_idx]

    def remove_crashed_carts(self):
        self.carts = [cart for cart in self.carts if cart.x is not None and cart.y is not None]


def parse_input(input_string):
    split_input = input_string.splitlines()

    track = Track()

    for y, line in enumerate(split_input):
        for x, char in enumerate(line):
            if char in '+/\\':
                track.turns[(x, y)] = char
            elif char in '^v<>':
                track.carts.append(Cart(x, y, char))

    return track


def part1():
    track = parse_input(input_string)

    while True:
        for idx, cart in enumerate(track.carts):
            # move cart to the next position
            cart.move()
            cart_position = (cart.x, cart.y)

            # check if there's a crash
            if cart_position in track.get_cart_positions(exclude_idx=[idx]):
                return cart_position

            # check if direction of the cart needs to be changed
            if cart_position in track.turns.keys():
                turn_symbol = track.turns[cart_position]
                cart.update_direction(turn_symbol)

        track.sort_carts()


def part2():
    track = parse_input(input_string)

    while len(track.carts) > 1:
        for idx, cart in enumerate(track.carts):
            if cart.x is None and cart.y is None:
                continue

            else:
                # move cart to the next position
                cart.move()
                cart_position = (cart.x, cart.y)

                # if there's a crash
                if cart_position in track.get_cart_positions(exclude_idx=[idx]):
                    # set the position of any cart at the crash site to None
                    # (to mark for removal at the end of the tick)
                    for cart in track.map_cart_position_to_cart(*cart_position):
                        cart.x, cart.y = None, None
                    continue

                # check if direction of the cart needs to be changed
                if cart_position in track.turns.keys():
                    turn_symbol = track.turns[cart_position]
                    cart.update_direction(turn_symbol)

        # at the end of each tick
        track.remove_crashed_carts()
        track.sort_carts()

    return track.carts[0]

if __name__ == '__main__':
    print(part1())
    print(part2())
