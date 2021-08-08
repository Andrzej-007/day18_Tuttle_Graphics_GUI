
import colorgram

extract_colour = colorgram.extract('image_hirst.jpg', 20)

# colors = colorgram.extract('image_hirst.jpg', 3)
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[1]
# red_2 = rgb.r
# print(rgb)
# print(red)
# print(red_2)

colect_colours = []
colected_rgb = []

for i in range(20):
    colour = extract_colour[i]
    colour_rgb = colour.rgb
    colected_rgb.append(tuple(colour_rgb))    # <--  here we have to methods
    new_colour = (colour_rgb[0], colour_rgb[1], colour_rgb[2])  # <--  here we have to methods
    colect_colours.append(new_colour)

print(f'{colect_colours}\n')
print(len(colect_colours))
print(f'\n colected_rgb {colected_rgb}')

    # r = i.rgb.r  # or r = i.rgb[0]
    # g = i.rgb.g
    # b = i.rgb.b
    # new_colours = (r, g, b)
    # colect_colours.append(new_colours)

# print(colect_colours)




