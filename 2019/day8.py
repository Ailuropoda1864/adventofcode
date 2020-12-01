day = 8

###############################
from read_input import *

input_string = get_input_string(day).strip()


# Part One
def find_layer_w_fewest_0(image_str, layer_len):
    image_len = len(image_str)
    assert image_len % layer_len == 0

    min_0_count = float('inf')
    for layer_start in range(0, image_len, layer_len):
        count = image_str.count('0', layer_start, layer_start + layer_len)
        if min_0_count > count:
            min_0_count = count
            target_layer = layer_start
    return target_layer


def part1(image_str, width, height):
    layer_len = width * height
    layer = find_layer_w_fewest_0(input_string, layer_len)
    return input_string.count('1', layer, layer + layer_len) * image_str.count('2', layer, layer + layer_len)


print(part1(input_string, 25, 6))


# Part Two
def decode(image_str, layer_len):
    image = ['2' for _ in range(layer_len)]
    for idx, pixel in enumerate(image_str):
        layer_idx = idx % layer_len
        if image[layer_idx] == '2':
            image[layer_idx] = pixel
    return image


def visualize(image, width, height):
    convert = {'0': ' ', '1': '#'}
    converted_image = [convert[pixel] for pixel in image]
    for i in range(0, width * height, width):
        print(''.join(converted_image[i: i + width]))


def part2(image_str, width, height):
    layer_len = width * height
    image = decode(image_str, layer_len)
    visualize(image, width, height)


part2(input_string, 25, 6)

