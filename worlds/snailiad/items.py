from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class SnailiadItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    in_game_id: int
    item_group: str = ""


item_base_id = 609342400

item_table: Dict[str, SnailiadItemData] = {
    "Pea Shooter": SnailiadItemData(ItemClassification.progression, 1, 0, 0, "Weapon"),  # todo Progression or Not
    "Boomerang": SnailiadItemData(ItemClassification.progression, 1, 1, 1, "Weapon"),
    "Super Secret Boomerang": SnailiadItemData(ItemClassification.progression, 0, 2, 11, "Weapon"),  # not generated but kept here for parity
    "Rainbow Wave": SnailiadItemData(ItemClassification.progression, 1, 3, 2, "Weapon"),
    "Debug Rainbow Wave": SnailiadItemData(ItemClassification.progression, 0, 4, 12, "Weapon"),  # not generated but kept here for parity
    "Progressive Weapon": SnailiadItemData(ItemClassification.progression, 0, 5, 100000, "Weapon"),  # todo confirm with epsilon what IDs the progressibve items are

    "Rapid Fire": SnailiadItemData(ItemClassification.progression, 1, 6, 6, "Modifier"),
    "Backfire": SnailiadItemData(ItemClassification.progression, 0, 7, 6, "Modifier"),
    "Devastator": SnailiadItemData(ItemClassification.progression, 1, 8, 3, "Modifier"),
    "Progressive Modifier": SnailiadItemData(ItemClassification.progression, 0, 9, 200000, "Modifier"),

    "Ice Snail": SnailiadItemData(ItemClassification.progression, 1, 10, 7, "Shell"),
    "Gravity Shell": SnailiadItemData(ItemClassification.progression, 1, 11, 8, "Shell"),
    "Magnetic Foot": SnailiadItemData(ItemClassification.progression, 0, 12, 8, "Shell"),
    "Corkscrew Jump": SnailiadItemData(ItemClassification.progression, 0, 13, 8, "Shell"),
    "Angel Hop": SnailiadItemData(ItemClassification.progression, 0, 14, 8, "Shell"),
    "Full Metal Snail": SnailiadItemData(ItemClassification.progression, 1, 15, 9, "Shell"),
    "Progressive Shell": SnailiadItemData(ItemClassification.progression, 0, 16, 300000, "Shell"),

    "Gravity Shock": SnailiadItemData(ItemClassification.progression, 1, 17, 10, "Ability"),
    "High Jump": SnailiadItemData(ItemClassification.progression, 1, 18, 4, "Ability"),
    "Wall Grab": SnailiadItemData(ItemClassification.progression, 0, 19, 4, "Ability"),
    "Shell Shield": SnailiadItemData(ItemClassification.progression, 1, 20, 5, "Ability"),
    "Shellmet": SnailiadItemData(ItemClassification.progression, 0, 21, 5, "Ability"),

    "Helix Fragment": SnailiadItemData(ItemClassification.filler, 30, 22, 24, ""),
    "Nothing": SnailiadItemData(ItemClassification.filler, 0, 23, 400000, ""),  # created in __init__
    "Heart Container": SnailiadItemData(ItemClassification.filler, 0, 24, 13, ""),  # created in __init__

    "Gravity Lock": SnailiadItemData(ItemClassification.trap, 0, 25, 500000, "Trap"),
    "Weapon Lock": SnailiadItemData(ItemClassification.trap, 0, 26, 600000, "Trap"),
    "Lullaby Trap": SnailiadItemData(ItemClassification.trap, 0, 27, 700000, "Trap"),
    "Spider Trap": SnailiadItemData(ItemClassification.trap, 0, 28, 800000,  "Trap"),
}

slot_data_item_names = []

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_group: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

extra_groups: Dict[str, Set[str]] = {
    "Flight": {"Angel Hop", "Corkscrew Jump", "Magnetic Foot", "Gravity Shell"},
    "Jump": {"High Jump", "Wall Grab"},
    "Shield": {"Shell Shield", "Shellmet"},
    "Rapid": {"Rapid Fire", "Backfire"},
}  # if item groups are requested to be added, they can be added here

item_name_group.update(extra_groups)
