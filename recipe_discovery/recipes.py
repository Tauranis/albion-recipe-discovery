RECIPIES = {
    # Animals
    "T7_FARM_PIG_GROWN": None,
    "T5_FARM_GOOSE_GROWN": None,
    "T3_FARM_CHICKEN_GROWN": None,
    # Raw Food
    "T7_MEAT": [("T7_FARM_PIG_GROWN", 0.05)],
    "T7_CORN": None,
    "T7_FISH_FRESHWATER_STEPPE_RARE": None,
    "T5_MEAT": [("T5_FARM_GOOSE_GROWN", 0.05)],
    "T5_CABBAGE": None,
    "T5_EGG": None,
    "T5_FISH_FRESHWATER_STEPPE_RARE": None,
    "T3_MEAT": [("T3_FARM_CHICKEN_GROWN", 0.05)],
    "T3_WHEAT": None,
    "T3_EGG": None,
    "T3_FISH_FRESHWATER_STEPPE_RARE": None,
    # Herbs
    "T3_COMFREY": None,
    "T4_BURDOCK": None,
    "T5_TEASEL": None,
    "T7_MULLEIN": None,
    # Food
    "T7_MEAL_OMELETTE": [("T7_CORN", 36), ("T7_MEAT", 72), ("T5_EGG", 18)],
    "T7_MEAL_OMELETTE_FISH": [
        ("T7_FISH_FRESHWATER_STEPPE_RARE", 1),
        ("T7_CORN", 6),
        ("T7_MULLEIN", 6),
        ("T7_MEAT", 6),
    ],
    "T5_MEAL_OMELETTE": [("T5_CABBAGE", 12), ("T5_MEAT", 24), ("T5_EGG", 6)],
    "T5_MEAL_OMELETTE_FISH": [
        ("T5_FISH_FRESHWATER_STEPPE_RARE", 1),
        ("T5_CABBAGE", 2),
        ("T5_TEASEL", 2),
        ("T5_EGG", 2),
    ],
    "T3_MEAL_OMELETTE": [("T3_WHEAT", 4), ("T3_MEAT", 8), ("T3_EGG", 2)],
    "T3_MEAL_OMELETTE_FISH": [
        ("T3_FISH_FRESHWATER_STEPPE_RARE", 1),
        ("T3_COMFREY", 1),
        ("T3_EGG", 1),
    ],
    # Potion
    "T5_POTION_REVIVE": [("T5_TEASEL", 24), ("T4_BURDOCK", 12), ("T5_EGG", 6)],
    "T3_POTION_REVIVE": [("T3_COMFREY", 8)],
    "T4_POTION_COOLDOWN": [("T4_BURDOCK", 8), ("T3_COMFREY", 4)],
    # Metal armor
    "T6_ARMOR_PLATE_SET1": [("T6_METALBAR", 16)],
    "T6_ARMOR_PLATE_SET2": [("T6_METALBAR", 16)],
    "T6_ARMOR_PLATE_SET3": [("T6_METALBAR", 16)],
    "T5_ARMOR_PLATE_SET1": [("T5_METALBAR", 16)],
    "T5_ARMOR_PLATE_SET2": [("T5_METALBAR", 16)],
    "T5_ARMOR_PLATE_SET3": [("T5_METALBAR", 16)],
    "T4_ARMOR_PLATE_SET1": [("T4_METALBAR", 16)],
    "T4_ARMOR_PLATE_SET2": [("T4_METALBAR", 16)],
    "T4_ARMOR_PLATE_SET3": [("T4_METALBAR", 16)],
    # Metal Helmet
    "T6_HEAD_PLATE_SET1": [("T6_METALBAR", 8)],
    "T6_HEAD_PLATE_SET2": [("T6_METALBAR", 8)],
    "T6_HEAD_PLATE_SET3": [("T6_METALBAR", 8)],
    "T5_HEAD_PLATE_SET1": [("T5_METALBAR", 8)],
    "T5_HEAD_PLATE_SET2": [("T5_METALBAR", 8)],
    "T5_HEAD_PLATE_SET3": [("T5_METALBAR", 8)],
    "T4_HEAD_PLATE_SET1": [("T4_METALBAR", 8)],
    "T4_HEAD_PLATE_SET2": [("T4_METALBAR", 8)],
    "T4_HEAD_PLATE_SET3": [("T4_METALBAR", 8)],
    # Metal Shoes
    "T8_SHOES_PLATE_SET1": [("T8_METALBAR", 8)],
    "T8_SHOES_PLATE_SET2": [("T8_METALBAR", 8)],
    "T8_SHOES_PLATE_SET3": [("T8_METALBAR", 8)],
    "T7_SHOES_PLATE_SET1": [("T7_METALBAR", 8)],
    "T7_SHOES_PLATE_SET2": [("T7_METALBAR", 8)],
    "T7_SHOES_PLATE_SET3": [("T7_METALBAR", 8)],
    "T6_SHOES_PLATE_SET1": [("T6_METALBAR", 8)],
    "T6_SHOES_PLATE_SET2": [("T6_METALBAR", 8)],
    "T6_SHOES_PLATE_SET3": [("T6_METALBAR", 8)],
    "T5_SHOES_PLATE_SET1": [("T5_METALBAR", 8)],
    "T5_SHOES_PLATE_SET2": [("T5_METALBAR", 8)],
    "T5_SHOES_PLATE_SET3": [("T5_METALBAR", 8)],
    "T4_SHOES_PLATE_SET1": [("T4_METALBAR", 8)],
    "T4_SHOES_PLATE_SET2": [("T4_METALBAR", 8)],
    "T4_SHOES_PLATE_SET3": [("T4_METALBAR", 8)],
    # Crossbow
    "T5_MAIN_1HCROSSBOW": [("T5_PLANKS", 16), ("T5_METALBAR", 8)],
    "T4_MAIN_1HCROSSBOW": [("T4_PLANKS", 16), ("T4_METALBAR", 8)],
    "T5_2H_CROSSBOW": [("T5_PLANKS", 20), ("T5_METALBAR", 12)],
    "T4_2H_CROSSBOW": [("T4_PLANKS", 20), ("T4_METALBAR", 12)],
    "T5_2H_CROSSBOWLARGE": [("T5_PLANKS", 20), ("T5_METALBAR", 12)],
    "T4_2H_CROSSBOWLARGE": [("T4_PLANKS", 20), ("T4_METALBAR", 12)],
    # Sword
    # Gathering Gear
    "T4_HEAD_GATHERER_FIBER": [("T4_CLOTH", 8)],
    "T4_ARMOR_GATHERER_FIBER": [("T4_CLOTH", 8)],
    "T4_BACKPACK_GATHERER_FIBER": [("T4_CLOTH", 4), ("T4_LEATHER", 4)],
    "T4_SHOES_GATHERER_FIBER": [("T4_CLOTH", 8)],
    "T4_ARMOR_GATHERER_HIDE": [("T4_LEATHER", 8)],
    "T4_BACKPACK_GATHERER_HIDE": [("T4_CLOTH", 4), ("T4_LEATHER", 4)],
    "T4_HEAD_GATHERER_HIDE": [("T4_LEATHER", 8)],
    "T4_SHOES_GATHERER_HIDE": [("T4_LEATHER", 8)],
    "T8_2H_TOOL_PICK": [("T8_PLANKS", 6), ("T8_METALBAR", 2)],
    "T7_2H_TOOL_PICK": [("T7_PLANKS", 6), ("T7_METALBAR", 2)],
    "T6_2H_TOOL_PICK": [("T6_PLANKS", 6), ("T6_METALBAR", 2)],
    "T5_2H_TOOL_PICK": [("T5_PLANKS", 6), ("T5_METALBAR", 2)],
    "T4_2H_TOOL_PICK": [("T4_PLANKS", 6), ("T4_METALBAR", 2)],
    "T3_2H_TOOL_PICK": [("T3_PLANKS", 6), ("T3_METALBAR", 2)],
    "T2_2H_TOOL_PICK": [("T2_PLANKS", 6), ("T2_METALBAR", 2)],
    "T8_ARMOR_GATHERER_ORE": [("T8_METALBAR", 8)],
    "T8_BACKPACK_GATHERER_ORE": [("T8_CLOTH", 4), ("T8_LEATHER", 4)],
    "T8_HEAD_GATHERER_ORE": [("T8_METALBAR", 8)],
    "T8_SHOES_GATHERER_ORE": [("T8_METALBAR", 8)],
    "T7_ARMOR_GATHERER_ORE": [("T7_METALBAR", 8)],
    "T7_BACKPACK_GATHERER_ORE": [("T7_CLOTH", 4), ("T7_LEATHER", 4)],
    "T7_HEAD_GATHERER_ORE": [("T7_METALBAR", 8)],
    "T7_SHOES_GATHERER_ORE": [("T7_METALBAR", 8)],
    "T6_ARMOR_GATHERER_ORE": [("T6_METALBAR", 8)],
    "T6_BACKPACK_GATHERER_ORE": [("T6_CLOTH", 4), ("T6_LEATHER", 4)],
    "T6_HEAD_GATHERER_ORE": [("T6_METALBAR", 8)],
    "T6_SHOES_GATHERER_ORE": [("T6_METALBAR", 8)],
    "T5_ARMOR_GATHERER_ORE": [("T5_METALBAR", 8)],
    "T5_BACKPACK_GATHERER_ORE": [("T5_CLOTH", 4), ("T5_LEATHER", 4)],
    "T5_HEAD_GATHERER_ORE": [("T5_METALBAR", 8)],
    "T5_SHOES_GATHERER_ORE": [("T5_METALBAR", 8)],
    "T4_ARMOR_GATHERER_ORE": [("T4_METALBAR", 8)],
    "T4_BACKPACK_GATHERER_ORE": [("T4_CLOTH", 4), ("T4_LEATHER", 4)],
    "T4_HEAD_GATHERER_ORE": [("T4_METALBAR", 8)],
    "T4_SHOES_GATHERER_ORE": [("T4_METALBAR", 8)],
    "T4_ARMOR_GATHERER_ROCK": [("T4_METALBAR", 8)],
    "T4_BACKPACK_GATHERER_ROCK": [("T4_CLOTH", 4), ("T4_LEATHER", 4)],
    "T4_HEAD_GATHERER_ROCK": [("T4_METALBAR", 8)],
    "T4_SHOES_GATHERER_ROCK": [("T4_METALBAR", 8)],
    "T4_ARMOR_GATHERER_WOOD": [("T4_LEATHER", 8)],
    "T4_BACKPACK_GATHERER_WOOD": [("T4_CLOTH", 4), ("T4_LEATHER", 4)],
    "T4_HEAD_GATHERER_WOOD": [("T4_LEATHER", 8)],
    "T4_SHOES_GATHERER_WOOD": [("T4_LEATHER", 8)],
    # Furniture
    "T7_FURNITUREITEM_TABLE": [("T7_PLANKS", 30), ("T7_CLOTH", 30)],
    "T6_FURNITUREITEM_TABLE": [("T6_PLANKS", 30), ("T6_CLOTH", 30)],
    "T5_FURNITUREITEM_TABLE": [("T5_PLANKS", 30), ("T5_CLOTH", 30)],
    "T4_FURNITUREITEM_TABLE": [("T4_PLANKS", 30), ("T4_CLOTH", 30)],
    "T3_FURNITUREITEM_TABLE": [("T3_PLANKS", 30), ("T3_CLOTH", 30)],
    "T2_FURNITUREITEM_TABLE": [("T2_PLANKS", 30), ("T2_CLOTH", 30)],
    "T5_FURNITUREITEM_CHEST": [("T5_PLANKS", 20), ("T5_METALBAR", 10)],
    "T4_FURNITUREITEM_CHEST": [("T4_PLANKS", 20), ("T4_METALBAR", 10)],
    "T3_FURNITUREITEM_CHEST": [("T3_PLANKS", 20), ("T3_METALBAR", 10)],
    "T2_FURNITUREITEM_CHEST": [("T2_PLANKS", 20), ("T2_METALBAR", 10)],
    "T7_FURNITUREITEM_BED": [("T7_PLANKS", 10), ("T7_CLOTH", 20)],
    "T6_FURNITUREITEM_BED": [("T6_PLANKS", 10), ("T6_CLOTH", 20)],
    "T5_FURNITUREITEM_BED": [("T5_PLANKS", 10), ("T5_CLOTH", 20)],
    "T4_FURNITUREITEM_BED": [("T4_PLANKS", 10), ("T4_CLOTH", 20)],
    "T3_FURNITUREITEM_BED": [("T3_PLANKS", 10), ("T3_CLOTH", 20)],
    "T2_FURNITUREITEM_BED": [("T2_PLANKS", 10), ("T2_CLOTH", 20)],
    # Metal Bars
    "T8_METALBAR": [("T8_ORE", 5), ("T7_METALBAR", 1)],
    "T7_METALBAR": [("T7_ORE", 5), ("T6_METALBAR", 1)],
    "T6_METALBAR": [("T6_ORE", 4), ("T5_METALBAR", 1)],
    "T5_METALBAR": [("T5_ORE", 3), ("T4_METALBAR", 1)],
    "T4_METALBAR": [("T4_ORE", 2), ("T3_METALBAR", 1)],
    "T3_METALBAR": [("T3_ORE", 2), ("T2_METALBAR", 1)],
    "T2_METALBAR": [("T2_ORE", 1)],
    # Ore
    "T8_ORE": None,
    "T7_ORE": None,
    "T6_ORE": None,
    "T5_ORE": None,
    "T4_ORE": None,
    "T3_ORE": None,
    "T2_ORE": None,
    # Planks
    "T8_PLANKS": [("T8_WOOD", 5), ("T7_PLANKS", 1)],
    "T7_PLANKS": [("T7_WOOD", 5), ("T6_PLANKS", 1)],
    "T6_PLANKS": [("T6_WOOD", 4), ("T5_PLANKS", 1)],
    "T5_PLANKS": [("T5_WOOD", 3), ("T4_PLANKS", 1)],
    "T4_PLANKS": [("T4_WOOD", 2), ("T3_PLANKS", 1)],
    "T3_PLANKS": [("T3_WOOD", 2), ("T2_PLANKS", 1)],
    "T2_PLANKS": [("T2_WOOD", 1)],
    # Wood
    "T8_WOOD": None,
    "T7_WOOD": None,
    "T6_WOOD": None,
    "T5_WOOD": None,
    "T4_WOOD": None,
    "T3_WOOD": None,
    "T2_WOOD": None,
    # CLOTH
    "T8_CLOTH": [("T8_FIBER", 5), ("T7_CLOTH", 1)],
    "T7_CLOTH": [("T7_FIBER", 5), ("T6_CLOTH", 1)],
    "T6_CLOTH": [("T6_FIBER", 4), ("T5_CLOTH", 1)],
    "T5_CLOTH": [("T5_FIBER", 3), ("T4_CLOTH", 1)],
    "T4_CLOTH": [("T4_FIBER", 2), ("T3_CLOTH", 1)],
    "T3_CLOTH": [("T3_FIBER", 2), ("T2_CLOTH", 1)],
    "T2_CLOTH": [("T2_FIBER", 1)],
    # FIBER
    "T8_FIBER": None,
    "T7_FIBER": None,
    "T6_FIBER": None,
    "T5_FIBER": None,
    "T4_FIBER": None,
    "T3_FIBER": None,
    "T2_FIBER": None,
    # LEATHER
    "T8_LEATHER": [("T8_HIDE", 5), ("T7_LEATHER", 1)],
    "T7_LEATHER": [("T7_HIDE", 5), ("T6_LEATHER", 1)],
    "T6_LEATHER": [("T6_HIDE", 4), ("T5_LEATHER", 1)],
    "T5_LEATHER": [("T5_HIDE", 3), ("T4_LEATHER", 1)],
    "T4_LEATHER": [("T4_HIDE", 2), ("T3_LEATHER", 1)],
    "T3_LEATHER": [("T3_HIDE", 2), ("T2_LEATHER", 1)],
    "T2_LEATHER": [("T2_HIDE", 1)],
    # HIDE
    "T8_HIDE": None,
    "T7_HIDE": None,
    "T6_HIDE": None,
    "T5_HIDE": None,
    "T4_HIDE": None,
    "T3_HIDE": None,
    "T2_HIDE": None,
    # STONEBLOCK
    "T8_STONEBLOCK": [("T8_ROCK", 5), ("T7_STONEBLOCK", 1)],
    "T7_STONEBLOCK": [("T7_ROCK", 5), ("T6_STONEBLOCK", 1)],
    "T6_STONEBLOCK": [("T6_ROCK", 4), ("T5_STONEBLOCK", 1)],
    "T5_STONEBLOCK": [("T5_ROCK", 3), ("T4_STONEBLOCK", 1)],
    "T4_STONEBLOCK": [("T4_ROCK", 2), ("T3_STONEBLOCK", 1)],
    "T3_STONEBLOCK": [("T3_ROCK", 2), ("T2_STONEBLOCK", 1)],
    "T2_STONEBLOCK": [("T2_ROCK", 1)],
    # ROCK
    "T8_ROCK": None,
    "T7_ROCK": None,
    "T6_ROCK": None,
    "T5_ROCK": None,
    "T4_ROCK": None,
    "T3_ROCK": None,
    "T2_ROCK": None,
    "T1_ROCK": None,
}
