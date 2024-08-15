from typing import Dict, Set

snailiad_regions: Dict[str, Set[str]] = {
    "Menu": {"Snail Town"},
    "Snail Town": {"Mare Carelia", "Spiralis Silere", "Amastrida Abyssus", "Lux Lirata", "Shrine of Iris"},
    "Mare Carelia": {"Spiralis Silere"},
    "Spiralis Silere": {"Amastrida Abyssus"},
    "Amastrida Abyssus": {"Lux Lirata"},
    "Lux Lirata": set(),
    "Shrine of Iris": set()
}
