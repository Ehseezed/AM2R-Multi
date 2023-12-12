from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld, CollectionState
from .rules import AM2RLogic
from .options import MetroidsAreChecks, is_option_enabled


EventId: Optional[int] = None


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable[[CollectionState], bool] = lambda state: True

def get_location_datas(world: Optional[MultiWorld], player: Optional[int]):
    location_table = [LocationData, ...]
    logic = AM2RLogic(world, player)

    location_table: List[LocationData] = [
        LocationData("Main Caves", "Main Caves: Vertical Spike Room Upper",  8680000, lambda state: logic.AM2R_can_fly(state) and logic.AM2R_can_bomb(state)),  # spider + bomb
        LocationData("Main Caves", "Main Caves: Vertical Spike Room Lower",  8680001, logic.AM2R_can_bomb),  # bomb
        LocationData("Main Caves", "Main Caves: Crumble Spike Room",  8680002, lambda state: state.has_any({'Hi Jump', 'Space Jump'}, player) and logic.AM2R_can_bomb(state)),  # jump. just jump. ibj and dbj can come later in advanced logic frogtroll
        LocationData("Main Caves", "Main Caves: Maze",  8680003),
        LocationData("Main Caves", "Main Caves: Shinespark Before the drop",  8680004, lambda state: state.has("Speed Booster", player)),  # speed
        LocationData("Main Caves", "Main Caves: Shinespark After the drop",  8680005, lambda state: state.has("Speed Booster", player)),  # speed

        LocationData("Golden Temple", "Golden Temple: Bombs",  8680006),
        LocationData("Golden Temple", "Golden Temple: Below Bombs",  8680007, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Hidden Energy Tank",  8680008, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Charge Beam",  8680009),
        LocationData("Golden Temple", "Golden Temple: Armory Left",  8680010),
        LocationData("Golden Temple", "Golden Temple: Armory Upper",  8680011),
        LocationData("Golden Temple", "Golden Temple: Armory Lower",  8680012),
        LocationData("Golden Temple", "Golden Temple: Armory Behind The False Wall ",  8680013, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Puzzle Room 1",  8680014),
        LocationData("Golden Temple", "Golden Temple: Puzzle Room 2",  8680015),
        LocationData("Golden Temple", "Golden Temple: Puzzle Room 3",  8680016),
        LocationData("Golden Temple", "Golden Temple: Spider Ball",  8680017),
        LocationData("Golden Temple", "Golden Temple: Celling Missile",  8680018, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),  # canspider
        LocationData("Golden Temple", "Golden Temple: EMP room",  8680019, lambda state: state.has("Super Missile", player) and logic.AM2R_has_ballspark(state) and logic.AM2R_can_bomb(state) and state.has("Screw Attack", player)),  # super + ballspark

        LocationData("Guardian", "Guardian: Up Above",  8680020, lambda state: logic.AM2R_can_bomb(state) and ((logic.AM2R_can_schmove(state) and state.has("Bombs", player)) or logic.AM2R_can_fly(state))),  # bomb + schmove
        LocationData("Guardian", "Guardian: Behind The Door",  8680021, lambda state: state.has("Power Bomb", player) and ((logic.AM2R_can_schmove(state) and state.has("Bombs", player)) or logic.AM2R_can_fly(state))),  # PB + schmove

        LocationData("Hydro Station", "Hydro Station: Cliff",  8680022, logic.AM2R_can_fly),
        LocationData("Hydro Station", "Hydro Station: Morph Tunnel",  8680023),
        LocationData("Hydro Station", "Hydro Station: Turbine Room",  8680024, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: Not so Secret Tunnel",  8680025, logic.AM2R_can_schmove),  # schmove
        LocationData("Hydro Station", "Hydro Station: Water puzzle Beside Varia",  8680026, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: Varia Suit",  8680027, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: EMP room",  8680028, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),  # super + speed

        LocationData("Arachnus", "Arachnus: Boss", 8680029),

        LocationData("Inner Hydro Station", "Hydro Station: Wave Beam",  8680030, logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Below Tower Pipe Upper",  8680031, lambda state: logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),  # schmove
        LocationData("Inner Hydro Station", "Hydro Station: Below Tower Pipe Lower",  8680032,  logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Dead End Missile ",  8680033,  logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Hi Jump",  8680034),
        LocationData("Inner Hydro Station", "Hydro Station: Behind Hi Jump Upper",  8680035, lambda state: logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),
        LocationData("Inner Hydro Station", "Hydro Station: Behind Hi Jump",  8680036, logic.AM2R_can_bomb),

        LocationData("Hydro Nest", "Hydro Nest: Below the Walkway",  8680037, logic.AM2R_can_bomb),  # Bomb
        LocationData("Hydro Nest", "Hydro Nest: Speed Celling",  8680038, lambda state: state.has("Speed Booster", player) and state.has("Speed Booster", player)),  # speed
        LocationData("Hydro Nest", "Hydro Nest: Behind the Wall",  8680039, lambda state: state.has("Power Bomb", player) and state.has("Screw Attack", player) and state.has("Speed Booster", player)),  # PB + screw/speed

        LocationData("Industrial Complex Nest", "Industrial Complex: Above Save",  8680040),
        LocationData("Industrial Complex Nest", "Industrial Complex: EMP Room",  8680041, lambda state: state.has("Power Bomb", player) and state.has("Super Missile", player) and state.can_reach("EMP", "Region", player)),  # PB + super
        LocationData("Industrial Complex Nest", "Industrial Complex Nest: Nest Shinespark",  8680042, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player) and logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),  # super + schmove

        LocationData("Pre Industrial Complex", "Industrial Complex: In the Sand",  8680043),
        LocationData("Pre Industrial Complex", "Industrial Complex: Complex Side After Tunnel",  8680044, lambda state: (state.has("Speed Booster", player) or logic.AM2R_can_spider(state)) and logic.AM2R_can_bomb(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Complex Side Tunnel",  8680045, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Save Room",  8680046, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Spazer",  8680047, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Gamma Spark",  8680048, lambda state: state.has("Speed Booster", player)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Speed Booster",  8680049, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_bomb(state)),  # bomb

        LocationData("Torizo Ascended", "Torizo Ascended: Boss", 8680050, logic.AM2R_can_schmove),

        LocationData("Industrial Complex", "Industrial Complex: Conveyor Belt Room",  8680051, lambda state: state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Doom Treadmill",  8680052, lambda state: state.has("Speed Booster", player) and logic.AM2R_can_bomb(state)),
        LocationData("Industrial Complex", "Industrial Complex: Robot room in the Wall",  8680053, lambda state: state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Robot room in the Floor", 8680054, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: First Supers",  8680055, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),

        LocationData("GFS Thoth", "GFS Thoth: Research Camp",  8680056),
        LocationData("GFS Thoth", "GFS Thoth: Hornoad room",  8680057, lambda state: state.has("Power Bomb", player)),
        LocationData("GFS Thoth", "GFS Thoth: Outside the Front of the Ship",  8680058, lambda state: state.has("Power Bomb", player)),
        LocationData("Genesis", "Genesis: Boss",  8680059, lambda state: state.has("Power Bomb", player)),

        LocationData("The Tower", "The Tower: Beside Hydro Pipe",  8680060, lambda state: state.has("Screw Attack", player)),
        LocationData("The Tower", "The Tower: Right Side of Tower",  8680061),
        LocationData("The Tower", "The Tower: In the Ceiling",  8680062, lambda state: logic.AM2R_can_bomb(state) and (state.has("Space Jump", player) or state.has("Spider Ball", player))),  # spider + bomb
        LocationData("The Tower", "The Tower: Dark Maze",  8680063, logic.AM2R_can_bomb),  # bomb
        LocationData("The Tower", "The Tower: Outside the Dark Maze",  8680064, logic.AM2R_can_bomb),
        LocationData("The Tower", "The Tower: Plasma Beam",  8680065, lambda state: logic.AM2R_can_bomb(state) and state.can_reach("Tester", "Region", player)),
        LocationData("The Tower", "The Tower: Beside Tester",  8680066, lambda state: state.has("Power Bomb", player)),  # pb
        LocationData("The Tower", "The Tower: Left side of tower",  8680067, lambda state: state.has("Power Bomb", player)),  # pb

        LocationData("Geothermal", "The Tower: Geothermal Reactor",  8680068),
        LocationData("Geothermal", "The Tower: Post Geothermal Chozo",  8680069, lambda state: state.has("Power Bomb", player)),  # pb
        LocationData("Geothermal", "The Tower: Post Geothermal Shinespark",  8680070, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player) and state.has("Super Missile", player)),  # Pb + spped + super

        LocationData("Underwater Distribution Center", "Distribution Center: Main Room Shinespark",  8680071, lambda state: state.has("Gravity Suit", player) and state.has("Speed Booster", player)),  # grav + screw
        LocationData("Underwater Distribution Center", "Distribution Center: Speed Hallway",  8680072, lambda state: state.has("Speed Booster", player) and state.has("Gravity Suit", player)),  # speed + grav

        LocationData("EMP", "Distribution Center: After EMP Activation",  8680073, lambda state: state.has("Screw Attack", player)),  # screw

        LocationData("Underwater Distro Connection", "Distribution Center: Spiderball Spike \"Maze\"",  8680074, lambda state: state.has("Spider Ball", player) and state.has("Gravity Suit", player)),  # spiderball underwater
        LocationData("Underwater Distro Connection", "Distribution Center: Before Spikey Tunnel",  8680075),
        LocationData("Underwater Distro Connection", "Distribution Center: Spikey Tunnel Shinespark",  8680076, lambda state: state.has("Gravity Suit", player) and state.has("Speed Booster", player)),  # grav + speed
        LocationData("Underwater Distro Connection", "Distribution Center: After Spikey Tunnel",  8680078, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player) and state.has("Gravity Suit", player) and state.has("Space Jump", player)),  # speed + grav + space + pb

        LocationData("Screw Attack", "Distribution Center: Screw Attack", 8680080),
        LocationData("Pipe Hell Outside", "Distribution Center: Outside after Gravity", 8680081, lambda state: state.has("Power Bomb", player) and state.has("Space Jump", player) and state.has("Gravity Suit", player)),  # pb + space + grav
        LocationData("Pipe Hell R", "Distribution Center: Before Underwater Pipe", 8680082, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player)),  # pb + speed

        LocationData("Gravity", "Distribution Center: Before Gravity", 8680083, lambda state: (state.has("Bombs", player) and (state.has("ChargeBeam", player) or state.has("Gravity Suit", player))) or state.has("Power Bomb", player)),  # bomb + charge/gravity / PB
        LocationData("Gravity", "Distribution Center: Gravity", 8680084, logic.AM2R_can_bomb),  # can bomb

        LocationData("Ice Beam", "Serris: Ice Beam", 8680085, lambda state: state.has("Ice Beam", player) and (state.has("Super Missile", player) or state.has("Speed Booster", player))),  # speed / Supers

        LocationData("Deep Caves", "Deep Caves: Ball Spark",  8680086, lambda state: state.has("Gravity Suit", player) and logic.AM2R_has_ballspark(state)),
        LocationData("Deep Caves", "Deep Caves: Behind the Bomb Block",  8680087, logic.AM2R_can_bomb),

        LocationData("Deep Caves", "Deep Caves: After Omega",  8680088),

        LocationData("Research Station", "The Last Metroid is in Captivity", EventId),

        LocationData("First Alpha", "The Forgotten Alpha", 8680100),

        LocationData("Golden Temple", "Golden Temple: Metroid above Spider Ball", 8680101, logic.AM2R_can_spider),
        LocationData("Golden Temple Nest", "Golden Temple Nest: Moe", 8680102, logic.AM2R_can_bomb),  # Loj
        LocationData("Golden Temple Nest", "Golden Temple Nest: Larry", 8680103, logic.AM2R_can_bomb),    # Loj
        LocationData("Golden Temple Nest", "Golden Temple Nest: Curly", 8680104, logic.AM2R_can_bomb),    # Loj

        LocationData("Main Caves", "Main Caves: Freddy Fazbear", 8680105),  # Epsilon
        LocationData("Hydro Station", "Hydro Station: Turbine Terror", 8680106),  # Xander
        LocationData("Hydro Station", "Hydro Station: The Lookout", 8680107, logic.AM2R_can_schmove),  # Xander
        LocationData("Hydro Station", "Hydro Station: Recent Guardian", 8680108),  # ANX

        LocationData("Hydro Nest", "Hydro Nest: Spiderman Decent", 8680109),
        LocationData("Hydro Nest", "Hydro Nest: Carnage Awful", 8680110),
        LocationData("Hydro Nest", "Hydro Nest: Venom Awesome", 8680111),
        LocationData("Hydro Nest", "Hydro Nest: Something More Something Awesome", 8680112),

        LocationData("Industrial Complex Nest", "Industrial Nest: Mimolette", 8680113, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: The Big Cheese", 8680114, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: Mohwir", 8680115, lambda state: logic.AM2R_can_bomb(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: Chirn", 8680116, lambda state: logic.AM2R_can_bomb(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: BHHarbinger", 8680117, lambda state: logic.AM2R_can_bomb(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: The Inanimate Sky", 8680118, lambda state: logic.AM2R_can_bomb(state) and state.has("Spider Ball", player) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),

        LocationData("Pre Industrial Complex", "Industrial Complex: Sisyphus", 8680119, logic.AM2R_can_spider),  # Mimo
        LocationData("Pre Industrial Complex", "Industrial Complex: And then there\'s this Asshole", 8680120, logic.AM2R_can_spider),  # ANX

        LocationData("Industrial Complex", "Inside Industrial: Guardian of Doom Treadmill", 8680121, lambda state: state.has("Speed Booster", player) and logic.AM2R_can_bomb(state)),
        LocationData("Industrial Complex", "Inside Industrial: Rawsome1234 by the Lava", 8680122, lambda state: state.has("Speed Booster", player) and logic.AM2R_can_bomb(state)),

        LocationData("GFS Thoth", "Dual Alphas: Marco", 8680123),  # Epsilon
        LocationData("GFS Thoth", "Dual Alphas: Polo", 8680124),  # Epsilon

        LocationData("Mines", "Mines: Unga", 8680125, lambda state: state.has("Super Missile", player) and (state.has("Space Jump", player) or state.has("Spider Ball", player))),
        LocationData("Mines", "Mines: Gunga", 8680126, lambda state: state.has("Super Missile", player) and (state.has("Space Jump", player) or state.has("Spider Ball", player))),

        LocationData("The Tower", "The Tower: Patricia", 8680127, logic.AM2R_can_fly),  # Mahan
        LocationData("The Tower", "The Tower: Variable \"GUH\"", 8680128, logic.AM2R_can_fly),  # ANX
        LocationData("The Tower", "Ruler of The Tower: Slagathor", 8680129, logic.AM2R_can_schmove),  # Rawsome
        LocationData("The Tower", "The Tower: Anakin", 8680130, logic.AM2R_can_bomb),  # Xander
        LocationData("The Tower", "The Tower: Mr.Sandman", 8680131, logic.AM2R_can_fly),  # Xander
        LocationData("The Tower", "The Tower: Xander", 8680132, lambda state: state.has("Space Jump", player)),

        LocationData("EMP", "EMP: Sir Zeta Commander of the Alpha Squadron", 8680133, logic.AM2R_can_bomb),  # Lucina

        LocationData("Pipe Hell R", "Alpha Squadron: Timmy", 8680134),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Tommy", 8680135),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Terry", 8680136),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Telly", 8680137),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Martin", 8680138),

        LocationData("Underwater Distro Connection", "Underwater: Gamma Bros Mario", 8680139),  # Lucina
        LocationData("Underwater Distro Connection", "Underwater: Gamma Bros Luigi", 8680140),  # Lucina

        LocationData("Deep Caves", "Deep Caves: Little Bro", 8680141),
        LocationData("Deep Caves", "Deep Caves: Big Sis", 8680142),
        LocationData("Omega Nest", "Omega Nest: SA-X Queen Lucina", 8680143),
        LocationData("Omega Nest", "Omega Nest: Epsilon", 8680144),
        LocationData("Omega Nest", "Omega Nest: Druid", 8680145),
    ]

    return tuple(location_table)
