from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class AM2RItemData(NamedTuple):
    classification: ItemClassification
    game_id: int
    quantity_in_item_pool: int
    item_group: str = ""


item_base_id = 8678000

item_table: Dict[str, AM2RItemData] = {
    "Missile":                  AM2RItemData(ItemClassification.filler, 15, 0),
    "Missile Launcher":         AM2RItemData(ItemClassification.progression, 300, 0),

    "Super Missile":            AM2RItemData(ItemClassification.filler, 16, 0),
    "Super Missile Launcher":   AM2RItemData(ItemClassification.progression, 300, 0),

    "Power Bomb":               AM2RItemData(ItemClassification.filler, 18, 0),
    "Power Bomb Launcher":      AM2RItemData(ItemClassification.progression, 300, 0),

    "Energy Tank":              AM2RItemData(ItemClassification.filler, 17, 0),

    "Morph Ball":               AM2RItemData(ItemClassification.progression, 300, 0),
    "Power Grip":               AM2RItemData(ItemClassification.progression, 300, 0),
    "Bombs":                    AM2RItemData(ItemClassification.progression, 0, 1),
    "Spider Ball":              AM2RItemData(ItemClassification.progression, 2, 1),
    "Hi Jump":                  AM2RItemData(ItemClassification.progression, 4, 1),
    "Spring Ball":              AM2RItemData(ItemClassification.progression, 3, 1),

    "Space Jump":               AM2RItemData(ItemClassification.progression, 6, 1),
    "Speed Booster":            AM2RItemData(ItemClassification.progression, 7, 1),
    "Screw Attack":             AM2RItemData(ItemClassification.progression, 8, 1),

    "Varia Suit":               AM2RItemData(ItemClassification.progression, 5, 1),
    "Gravity Suit":             AM2RItemData(ItemClassification.progression, 9, 1),

    "Arm Cannon":               AM2RItemData(ItemClassification.progression, 300, 0),
    "Charge Beam":              AM2RItemData(ItemClassification.progression, 10, 1),
    "Wave Beam":                AM2RItemData(ItemClassification.useful, 12, 1),
    "Spazer":                   AM2RItemData(ItemClassification.useful, 13, 1),
    "Plasma Beam":              AM2RItemData(ItemClassification.useful, 14, 1),
    "Ice Beam":                 AM2RItemData(ItemClassification.progression, 11, 1),

    "Flood Trap":               AM2RItemData(ItemClassification.trap, 21, 0),
    "Big Toss Trap":            AM2RItemData(ItemClassification.trap, 22, 0),
    "Short Beam":               AM2RItemData(ItemClassification.trap, 23, 0),
    "EMP Trap":                 AM2RItemData(ItemClassification.trap, 24, 0),
    "OHKO Trap":                AM2RItemData(ItemClassification.trap, 25, 0),
    "Touhou Trap":              AM2RItemData(ItemClassification.trap, 26, 0),

    "Metroid":                  AM2RItemData(ItemClassification.progression_skip_balancing, 19, 0)

}

item_name_to_id: Dict[str, int] = {name: item_base_id + data.game_id for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

trap_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.trap]
