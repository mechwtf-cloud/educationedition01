def build_house():
    width = 8
    length = 10
    height = 9

    start = player.position()

    # ===== ZÁKLAD =====
    blocks.fill(
        Block.STONE,
        start,
        positions.add(start, world(width - 1, 0, length - 1)),
        FillOperation.REPLACE
    )

    # ===== PODLAHA =====
    blocks.fill(
        Block.PLANKS_SPRUCE,
        positions.add(start, world(0, 1, 0)),
        positions.add(start, world(width - 1, 1, length - 1)),
        FillOperation.REPLACE
    )

    # ===== STENY =====
    for y in range(2, height):
        for x in range(width):
            for z in range(length):
                if x == 0 or x == width - 1 or z == 0 or z == length - 1:
                    blocks.place(
                        Block.STRIPPED_DARK_OAK_WOOD,
                        positions.add(start, world(x, y, z))
                    )

    # ===== VYPRÁZDNI VNÚTRO =====
    blocks.fill(
        Block.AIR,
        positions.add(start, world(1, 2, 1)),
        positions.add(start, world(width - 2, height - 1, length - 2)),
        FillOperation.REPLACE
    )

    # ===== OKNÁ (veľké) =====
    for y in range(3, 6):
        for x in range(2, width - 2):
            blocks.place(
                Block.GLASS_PANE,
                positions.add(start, world(x, y, 0))
            )
            blocks.place(
                Block.GLASS_PANE,
                positions.add(start, world(x, y, length - 1))
            )

    # ===== BOČNÉ OKNÁ =====
    for y in range(3, 6):
        blocks.place(Block.GLASS_PANE, positions.add(start, world(0, y, 4)))
        blocks.place(Block.GLASS_PANE, positions.add(start, world(width - 1, y, 4)))

    # ===== DVERA =====
    blocks.place(Block.DARK_OAK_DOOR, positions.add(start, world(3, 2, 0)))

    # ===== STRECHA (presah + šikmá) =====
    for i in range(4):
        blocks.fill(
            Block.SPRUCE_WOOD_SLAB,
            positions.add(start, world(-1 + i, height + i, -1)),
            positions.add(start, world(width - i, height + i, length)),
            FillOperation.REPLACE
        )

player.on_chat("dom", build_house)



samovrazda
