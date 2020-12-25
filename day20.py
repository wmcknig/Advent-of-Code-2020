from sys import argv
from math import prod

"""
Advent of Code Day 20 Part 1
You are given a series of square tiles consisting of '.' and '#' characters.
Said tiles, if flipped and rotated correctly, can be put into a square array
such that all adjacent tiles have matching edges
Find the corner tiles and multiply their ids
Part 2
Produce an image by stripping the borders from the tiles and assembling
the matching tiles, then check for the presence of a pattern. Said pattern is
only detectable if the image is flipped or rotated a certain way. Find the
number of '#' characters in the complete image that are not part of the pattern
"""

"""
Checks to see if two tiles have matching edges
"""
def matching_edges(a, b):
    set_a = set(a)
    set_a.update(set(i[::-1] for i in a))
    set_b = set(b)
    set_b.update(set(i[::-1] for i in b))
    return set_a.intersection(set_b)

"""
Flips a tile
"""
def flip(tile):
    return tile[::-1]

"""
Rotates a tile 90 degrees clockwise
"""
def rotate(tile):
    return ["".join(row[i] for row in tile)[::-1] for i in range(len(tile))]

"""
Checks if the given edge matches an edge of the given tile and rotates/flips
it so that said edge matches the given edge
"""
def check_tile(edge, tile, side):
    matches = False
    #check the top to see if it matches
    for _ in range(4):
        if tile[0] == edge:
            matches = True
            break
        tile = rotate(tile)
    if not matches:
        #try the tile flipped
        tile = flip(tile)
        for _ in range(4):
            if tile[0] == edge:
                matches = True
                break
            tile = rotate(tile)
    if matches:
        if side == "top":
            return tile
        if side == "left":
            tile = rotate(tile)
            tile = rotate(tile)
            tile = rotate(tile)
            return tile
        if side == "right":
            tile = rotate(tile)
            return tile
        if side == "bottom":
            tile = rotate(tile)
            tile = rotate(tile)
            return tile
    #failed to find a matching tile orientation
    return False

"""
Given a tile, recursively checks its connected tiles and adds them to an
assembled mapping of tile ids to their oriented tiles and above, below, left,
and right tile ids.
Assumes that each matching tile for a tile uniquely matches to one edge of
the tile.
Assumes tile is already in layout
"""
def complete_image(tiles, matches, tile, layout):
    for tile_id in matches[tile]:
        #check that the tile isn't already matched
        if tile_id in layout[tile].values():
            continue
        if tile_id in layout:
            matching_tile = layout[tile_id]["tile"]
        else:
            matching_tile = tiles[tile_id]
        #check above
        result = check_tile(layout[tile]["tile"][0][::-1], matching_tile,
                                        "bottom")
        if result is not False:
            layout[tile]["top"] = tile_id
            if tile_id in layout:
                layout[tile_id]["bottom"] = tile
            else:
                layout[tile_id] = {"tile": result, "bottom": tile}
            complete_image(tiles, matches, tile_id, layout)
            continue
        #check below 
        result = check_tile(layout[tile]["tile"][-1], matching_tile, "top")
        if result is not False:
            layout[tile]["bottom"] = tile_id
            if tile_id in layout:
                layout[tile_id]["top"] = tile
            else:
                layout[tile_id] = {"tile": result, "top": tile}
            complete_image(tiles, matches, tile_id, layout)
            continue
        #check left
        result = check_tile("".join(i[0] for i in layout[tile]["tile"]),
                                matching_tile, "right")
        if result is not False:
            layout[tile]["left"] = tile_id
            if tile_id in layout:
                layout[tile_id]["right"] = tile
            else:
                layout[tile_id] = {"tile": result, "right": tile}
            complete_image(tiles, matches, tile_id, layout)
            continue
        #check right
        result = check_tile("".join(i[-1] for i in layout[tile]["tile"][::-1]),
                                matching_tile, "left")
        if result is not False:
            layout[tile]["right"] = tile_id
            if tile_id in layout:
                layout[tile_id]["left"] = tile
            else:
                layout[tile_id] = {"tile": result, "left": tile}
            complete_image(tiles, matches, tile_id, layout)
            continue

"""
Given a layout, trims the edges from each tile and composes them into a large
image
"""
def render_image(layout):
    image = []
    #find the topleftmost tile (it is assumed there is one and only one)
    row_start = list(filter(lambda x: "top" not in layout[x]
                                and "left" not in layout[x], layout))[0]
    #for each row of tiles, iterate across the string rows
    while row_start is not None:
        for subrow in range(1, len(layout[row_start]["tile"]) - 1):
            current = row_start
            string = ""
            while current is not None:
                string += layout[current]["tile"][subrow][1:-1]
                current = layout[current].get("right")
            image.append(string)
        row_start = layout[row_start].get("bottom")
    return image

"""
Checks the image for the presence of a subimage. Spaces in the subimage
mean corresponding values in the regular image are irrelevant. Returns a
count of how many times the subimage is found
"""
def mask_image(image, subimage):
    length = len(subimage[0])
    height = len(subimage)
    count = 0
    for y in range(len(image) - height + 1):
        for x in range(len(image[0]) - length + 1):
            pixels = []
            for row in range(height):
                pixels += zip(image[y + row][x:], subimage[row])
            detected = True
            for (i, j) in pixels:
                if j == ' ':
                    continue
                if i != j:
                    detected = False
                    break
            if detected:
                count += 1
    return count

if __name__ == "__main__":
    f = open(argv[1], 'r')
    tiles = [[j.strip() for j in i.split("\n")]
                for i in f.read().strip().split("\n\n")]
    f.close()
    edges = {}
    complete_tiles = {}
    for tile in tiles:
        tile_id = int(tile[0].strip(":").split()[1])
        complete_tiles[tile_id] = tile[1:]
        top = tile[1]
        bottom = tile[-1]
        left = "".join(i[0] for i in tile[1:])
        right = "".join(i[-1] for i in tile[1:])
        edges[tile_id] = (top, bottom, left, right)
    #find each possible match among the edges
    matches = {i: [] for i in edges}
    for tile in edges:
        for other in edges:
            if tile != other and \
                    len(matching_edges(edges[tile], edges[other])) != 0:
                matches[tile].append(other)
    corners = list(filter(lambda x: len(matches[x]) == 2, matches))
    #assemble the tiles
    layout = {corners[0]: {"tile": complete_tiles[corners[0]]}}
    complete_image(complete_tiles, matches, corners[0], layout)
    image = render_image(layout)
    subimage = []
    subimage.append("                  # ")
    subimage.append("#    ##    ##    ###")
    subimage.append(" #  #  #  #  #  #   ")
    pound_count = sum(map(lambda x: x.count('#'), subimage))
    for _ in range(4):
        count = mask_image(image, subimage)
        if count > 0:
            break
        image = rotate(image)
    if count == 0:
        image = flip(image)
        for _ in range(4):
            count = mask_image(image, subimage)
            if count > 0:
                break
            image = rotate(image)
    print(sum(map(lambda x: x.count('#'), image)) - count * pound_count)
