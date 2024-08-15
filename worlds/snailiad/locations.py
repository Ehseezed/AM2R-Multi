from typing import Dict, Set, NamedTuple
from itertools import groupby


class SnailiadLocationData(NamedTuple):
    region: str
    location_group: str = "region"


location_based_id = 609342400  # todo actual base ID

location_table: Dict[str, SnailiadLocationData] = {
    "Leggy Snail\'s Tunnel":            SnailiadLocationData("Snail Town"),
    "Town Overtunnel":                  SnailiadLocationData("Snail Town"),
    "Super Secret Alcove":              SnailiadLocationData("Snail Town"),
    "Love Snail\'s Alcove":             SnailiadLocationData("Snail Town"),
    "Suspicious Tree":                  SnailiadLocationData("Snail Town"),
    "Anger Management Room":            SnailiadLocationData("Snail Town"),
    "Percentage Snail\'s Hidey Hole":   SnailiadLocationData("Snail Town"),
    "Digging Grounds":                  SnailiadLocationData("Snail Town"),
    "Cave Snail\'s Cave":               SnailiadLocationData("Snail Town"),
    "Fragment Cave":                    SnailiadLocationData("Snail Town"),
    #  Mare Carelia
    "Discombobulatory Alcove":          SnailiadLocationData("Mare Carelia"),
    "Seabed Caves":                     SnailiadLocationData("Mare Carelia"),
    "Fine Dining (Peashooter)":         SnailiadLocationData("Mare Carelia"),
    "Fine Dining (Fragment)":           SnailiadLocationData("Mare Carelia"),
    "The Maze Room":                    SnailiadLocationData("Mare Carelia"),
    "Monument of Greatness":            SnailiadLocationData("Mare Carelia"),
    "Heart of the Sea":                 SnailiadLocationData("Mare Carelia"),
    "Daily Helping of Calcium":         SnailiadLocationData("Mare Carelia"),
    "Dig, Snaily, Dig":                 SnailiadLocationData("Mare Carelia"),
    "Skywatcher\'s Loot":               SnailiadLocationData("Mare Carelia"),
    "Signature Croissants (Boomerang)": SnailiadLocationData("Mare Carelia"),
    "Signature Croissants (Heart)":     SnailiadLocationData("Mare Carelia"),
    # Spiralis Silere
    "Frost Shrine":                     SnailiadLocationData("Spiralis Silere"),
    "Sweater Required":                 SnailiadLocationData("Spiralis Silere"),
    "A Secret to Snowbody":             SnailiadLocationData("Spiralis Silere"),
    "Devil\'s Alcove":                  SnailiadLocationData("Spiralis Silere"),
    "Ice Climb":                        SnailiadLocationData("Spiralis Silere"),
    "The Labyrinth (Fragment)":         SnailiadLocationData("Spiralis Silere"),
    "The Labyrinth (High Jump)":        SnailiadLocationData("Spiralis Silere"),
    "Sneaky, Sneaky":                   SnailiadLocationData("Spiralis Silere"),
    "Prismatic Prize (Rainbow Wave)":   SnailiadLocationData("Spiralis Silere"),
    "Prismatic Prize (Heart)":          SnailiadLocationData("Spiralis Silere"),
    # Amastrida Abyssus
    "Hall of Fire":                     SnailiadLocationData("Amastrida Abyssus"),
    "Green Cache":                      SnailiadLocationData("Amastrida Abyssus"),
    "Furnace":                          SnailiadLocationData("Amastrida Abyssus"),
    "Slitherine Grove":                 SnailiadLocationData("Amastrida Abyssus"),
    "Floaty Fortress (Top Left)":       SnailiadLocationData("Amastrida Abyssus"),
    "Floaty Fortress (Bottom Right)":   SnailiadLocationData("Amastrida Abyssus"),
    "Woah Mama":                        SnailiadLocationData("Amastrida Abyssus"),
    "Shocked Shell":                    SnailiadLocationData("Amastrida Abyssus"),
    "Gravity Shrine":                   SnailiadLocationData("Amastrida Abyssus"),
    "Fast Food":                        SnailiadLocationData("Amastrida Abyssus"),
    "The Bridge":                       SnailiadLocationData("Amastrida Abyssus"),
    # lux lirata
    "Transit 90":                       SnailiadLocationData("Lux Lirata"),
    "Steel Shrine":                     SnailiadLocationData("Lux Lirata"),
    "Space Balcony (Heart)":            SnailiadLocationData("Lux Lirata"),
    "Space Balcony (Fragment)":         SnailiadLocationData("Lux Lirata"),
    "The Vault":                        SnailiadLocationData("Lux Lirata"),
    "Holy Hideaway":                    SnailiadLocationData("Lux Lirata"),
    "Arctic Alcove":                    SnailiadLocationData("Lux Lirata"),
    "Reinforcements":                   SnailiadLocationData("Lux Lirata"),
    # Shrine of Iris
    "Glitched Goodies":                 SnailiadLocationData("Shrine of Iris"),
    # Knowledge locations
    "Original Testing Room":            SnailiadLocationData("Snail Town"),
    "Squared Snelks":                   SnailiadLocationData("Spiralis Silere"),
    "Scorching Snelks":                 SnailiadLocationData("Amastrida Abyssus"),
    "Hidden Hideout":                   SnailiadLocationData("Amastrida Abyssus"),
    "Lost Loot":                        SnailiadLocationData("Lux Lirata"),
}

location_name_to_id: Dict[str, int] = {name: location_based_id + index for index, name in enumerate(location_table)}


def get_location_group(location_name: str) -> str:
    loc_group = location_table[location_name].location_group
    if loc_group == "region":
        loc_group = location_table[location_name].region.lower()
    return loc_group


location_name_group: Dict[str, Set[str]] = {
    group: set(location_names) for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group) if group != ""
}
