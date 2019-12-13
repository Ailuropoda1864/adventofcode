day = 6

###############################
from read_input import *

input_string = get_input_string(day)

parsed_input = [tuple(map(int, line.split(', '))) for line in input_string.splitlines()]

# find the edges of the grid
max_x = max(parsed_input, key=lambda coords: coords[0])[0]
min_x = min(parsed_input, key=lambda coords: coords[0])[0]
max_y = max(parsed_input, key=lambda coords: coords[1])[1]
min_y = min(parsed_input, key=lambda coords: coords[1])[1]


class dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cal_dist(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)


input_coordinates = [dot(x, y) for x, y in parsed_input]

grid = [dot(x, y) for y in range(min_y, max_y+1)
        for x in range(min_x, max_x+1)]


# Part One
out_layer = [dot(min_x-1, y) for y in range(min_y-1, max_y+2)] + \
        [dot(max_x+1, y) for y in range(min_y-1, max_y+2)] + \
        [dot(x, min_y-1) for x in range(min_x-1, max_x+2)] + \
        [dot(x, max_y+1) for x in range(min_x - 1, max_x + 2)]
# in order: left, right, bottom, top edges


def cal_num_closest_loc(my_dots, grid):
    num_closest_loc = [0 for dot in my_dots]
    for dot1 in grid:
        distances = [dot1.cal_dist(dot2) for dot2 in my_dots]
        min_dist = min(distances)
        closest_coord_id = [id for id, dist in enumerate(distances) if dist == min_dist]
        if len(closest_coord_id) == 1:
            num_closest_loc[closest_coord_id[0]] += 1
    return num_closest_loc

nums1 = cal_num_closest_loc(input_coordinates, grid)
nums2 = cal_num_closest_loc(input_coordinates, out_layer)


# the number of closest locations for coordinates with finite areas would not change
# even as the grid expands
largest_area = max([num for id, num in enumerate(nums1) if nums2[id] == 0])
print(largest_area)


# Part Two
size = sum([1 for dot1 in grid
            if sum([dot1.cal_dist(dot2) for dot2 in input_coordinates]) < 10000])
print(size)

