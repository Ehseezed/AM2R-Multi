from typing import List, Tuple, Dict, Set, Optional, Callable


am2r_regions: Dict[str, Set[str]] = {
    "Menu": {"Main Caves"},
    "Main Caves": {"Guardian", "First Alpha", "Hydro Station", "Mines", "Industrial Complex Nest", "Lower Main Caves"
                   "GFS Thoth"},
    "Lower Main Caves": {"The Tower", "Underwater Distribution Center", "Deep Caves"},
    "GFS Thoth": {"Genesis"},
    "Guardian": {"Golden Temple", "Golden Temple Nest"},
    "Golden Temple": set(),
    "Golden Temple Nest": set(),
    "First Alpha": set(),
    "Hydro Station": {"Hydro Nest", "The Tower", "The Lab", "Arachnus", "Inner Hydro Station"},
    "Hydro Nest": set(),
    "Arachnus": set(),
    "Inner Hydro Station": set(),
    "Industrial Complex Nest": {"Pre Industrial Complex"},
    "Pre Industrial Complex": {"Industrial Complex", "Torizo Ascended"},
    "Torizo Ascended": set(),
    "Industrial Complex": set(),
    "Mines": set(),
    "The Tower": {"Tester Lower", "Tester Upper", "Geothermal"},
    "Tester Lower": {"Tester"},
    "Tester Upper": {"Tester"},
    "Tester": set(),
    "Geothermal": set(),
    ""
}
    # A5
    connect(world, player, "Underwater Distribution Center", "EMP", logic.AM2R_can_bomb),
    connect(world, player, "EMP", "Underwater Distribution Center", logic.AM2R_can_bomb),

    connect(world, player, "Underwater Distribution Center", "Serris"),
    connect(world, player, "Serris", "Underwater Distribution Center", lambda state: state.has("Gravity Suit", player)),

    connect(world, player, "Ice Beam", "Serris"),
    connect(world, player, "Serris", "Ice Beam", lambda state: state.has("Gravity Suit", player)),

    # Pipe Hell Fuckery
    connect(world, player, "EMP", "Pipe Hell BL"),
    connect(world, player, "Pipe Hell BL", "EMP"),

    connect(world, player, "Pipe Hell BL", "Pipe Hell BR"),
    connect(world, player, "Pipe Hell BR", "Pipe Hell BL"),

    connect(world, player, "Pipe Hell L", "Pipe Hell BL", lambda state: state.has("Screw Attack", player)),
    connect(world, player, "Pipe Hell BL", "Pipe Hell L", lambda state: state.has("Screw Attack", player)),

    connect(world, player, "Pipe Hell BR", "Pipe Hell L"),
    connect(world, player, "Pipe Hell L", "Pipe Hell BR"),

    connect(world, player, "Pipe Hell BR", "Pipe Hell R", lambda state: state.has("Screw Attack", player)),
    connect(world, player, "Pipe Hell R", "Pipe Hell BR", lambda state: state.has("Screw Attack", player)),

    connect(world, player, "Pipe Hell R", "Pipe Hell L", logic.AM2R_can_bomb),
    connect(world, player, "Pipe Hell L", "Pipe Hell R", logic.AM2R_can_bomb),

    connect(world, player, "Pipe Hell L", "Fast Travel", lambda state: state.has("Screw Attack", player)),
    connect(world, player, "Fast Travel", "Pipe Hell L", lambda state: state.has("Screw Attack", player)),

    connect(world, player, "Fast Travel", "Gravity", lambda state: state.has("Gravity Suit", player)),  # one way transition due to crumbles

    connect(world, player, "Fast Travel", "Underwater Distribution Center"),
    connect(world, player, "Underwater Distribution Center", "Fast Travel", lambda state: state.can_reach("Fast Travel", "Region", player)),

    connect(world, player, "Gravity", "Pipe Hell Outside", lambda state: state.has("Gravity Suit", player) and state.has("Space Jump", player)),
    connect(world, player, "Pipe Hell Outside", "Gravity"),

    connect(world, player, "Pipe Hell Outside", "Pipe Hell R", logic.AM2R_can_bomb),
    connect(world, player, "Pipe Hell R", "Pipe Hell Outside", lambda state: state.can_reach("Pipe Hell Outside", "Region", player)),

    connect(world, player, "Screw Attack", "Pipe Hell R", lambda state: state.has("Screw Attack", player) and logic.AM2R_can_schmove(state)),
    connect(world, player, "Pipe Hell R", "Screw Attack", logic.AM2R_can_spider),

    connect(world, player, "Underwater Distribution Center", "Underwater Distro Connection", lambda state: state.has("Ice Beam", player) or (state.has("Gravity Suit", player) and state.has("Speed Booster", player))),
    connect(world, player, "Underwater Distro Connection", "Underwater Distribution Center", lambda state: state.has("Ice Beam", player) or (state.has("Gravity Suit", player) and state.has("Speed Booster", player))),

    connect(world, player, "Underwater Distro Connection", "Pipe Hell R"),
    connect(world, player, "Pipe Hell R", "Underwater Distro Connection", lambda state: state.has("Super Missile", player) or (state.has("Gravity Suit", player) and state.has("Speed Booster", player)))

    connect(world, player, "Deep Caves", "Omega Nest")
    connect(world, player, "Omega Nest", "Deep Caves")

    connect(world, player, "Omega Nest", "The Lab", logic.AM2R_can_lab)  # , logic.AM2R_can_lab
    connect(world, player, "The Lab", "Omega Nest")

    connect(world, player, "The Lab", "Research Station")


def throwIfAnyLocationIsNotAssignedToARegion(regions: List[Region], regionNames: Set[str]):
    existingRegions: Set[str] = set()

    for region in regions:
        existingRegions.add(region.name)

    if regionNames - existingRegions:
        raise Exception(
            "AM2R: the following regions are used in locations: {}, but no such region exists".format(
                regionNames - existingRegions))


def create_location(player: int, location_data: LocationData, region: Region) -> Location:
    location = Location(player, location_data.name, location_data.code, region)
    location.access_rule = location_data.rule

    if id is None:
        location.event = True
        location.locked = True

    return location


def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]],name: str) -> Region:
    region = Region(name, player, world)

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, region)
            region.locations.append(location)

    return region


def connect(world: MultiWorld, player: int, source: str, target: str,
            rule: Optional[Callable[[CollectionState], bool]] = None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, "", sourceRegion)

    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)


def split_location_datas_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[AM2RLocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region

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