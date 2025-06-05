def raster_create():
    return [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
    ]


def raster_put_at(raster, character, x, y):
    raster[x][y] = character
    return raster


def raster_print(raster):
    for row in raster:
        line = ''
        for space in row:
            if space is None:
                line += ' '
            else:
                line += space.rjust(2)
        print(line)


def raster_put_rect_at(raster, char, x, y, width, height):
    for i in range(height):
        for j in range(width):
            raster[x + i][y + j] = char
    return char


raster = raster_create()


raster_put_rect_at(raster, '*', 0, 0, 10, 10)
raster_put_rect_at(raster, '+', 1, 1, 8, 8)
raster_put_rect_at(raster, 'o', 2, 2, 6, 6)
raster_put_rect_at(raster, '-', 3, 3, 4, 4)
raster_put_rect_at(raster, 'x', 4, 4, 2, 2)


raster_print(raster)
