def build_house():
    width = 7
    length = 10
    height = 4

    start = player.position()

    for i in range(3):
        offset = positions.add(start, world(i * (width + 6), 0, 0))


        for x in range(width):
            for z in range(length):
                for y in range(height):
                    if x == 0 or x == width - 1 or z == 0 or z == length - 1:
                        blocks.place(
                            Block.STRIPPED_DARK_OAK_WOOD,
                            positions.add(offset, world(x, y, z))
                        )


        blocks.fill(
            Block.AIR,
            positions.add(offset, world(1, 1, 1)),
            positions.add(offset, world(width - 2, height - 1, length - 2)),
            FillOperation.REPLACE
        )


        for x in range(width):
            for z in range(length):
                blocks.place(
                    Block.PLANKS_DARK_OAK,
                    positions.add(offset, world(x, -1, z))
                )

        blocks.place(Block.OAK_DOOR, positions.add(offset, world(2, 0, 0)))

        
        for x in range(width):
            for z in range(length):
                blocks.place(
                    Block.SMOOTH_STONE_SLAB,
                    positions.add(offset, world(x, height, z))
                )


player.on_chat("dom", build_house)
