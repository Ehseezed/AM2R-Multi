from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld, CollectionState
from .rules import AM2RLogic
from .options import MetroidsAreChecks, is_option_enabled


EventId: Optional[int] = None


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    game_id: int = 0
    rule: Callable[[CollectionState], bool] = lambda state: True

def get_location_datas(world: Optional[MultiWorld], player: Optional[int]):
    location_table = [LocationData, ...]
    logic = AM2RLogic(world, player)

    location_table: List[LocationData] = [
        LocationData("Main Caves", "Main Caves: Spider Ball Challenge Upper",  8680000, 53, lambda state: logic.AM2R_can_fly(state) and logic.AM2R_can_bomb(state)),  # spider + bomb
        LocationData("Main Caves", "Main Caves: Spider Ball Challenge Lower",  8680001, 52, lambda state: state.has("Power Bomb", player, 3) or state.has("Bombs", player)),  # bomb
        LocationData("Main Caves", "Main Caves: Hi-Jump Challenge",  8680002, 57, lambda state: state.has_any({'Hi Jump', 'Space Jump'}, player) and logic.AM2R_can_bomb(state)),  # jump. just jump. ibj and dbj can come later in advanced logic frogtroll
        LocationData("Main Caves", "Main Caves: Spiky Maze",  8680003, 210),
        LocationData("Main Caves", "Main Caves: Shinespark Before The Pit",  8680004, 54, lambda state: state.has("Speed Booster", player)),  # speed
        LocationData("Main Caves", "Main Caves: Shinespark After The Pit",  8680005, 55, lambda state: state.has("Speed Booster", player)),  # speed

        LocationData("Golden Temple", "Golden Temple: Bombs",  8680006, 0),
        LocationData("Golden Temple", "Golden Temple: Below Bombs",  8680007, 100, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Hidden Energy Tank",  8680008, 103, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Charge Beam",  8680009, 10),
        LocationData("Golden Temple", "Golden Temple: Armory Left",  8680010, 104),
        LocationData("Golden Temple", "Golden Temple: Armory Upper",  8680011, 106),
        LocationData("Golden Temple", "Golden Temple: Armory Lower",  8680012, 105),
        LocationData("Golden Temple", "Golden Temple: Armory False Wall",  8680013, 107, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: 3-Orb Hallway Left",  8680014, 101),
        LocationData("Golden Temple", "Golden Temple: 3-Orb Hallway Middle",  8680015, 108),
        LocationData("Golden Temple", "Golden Temple: 3-Orb Hallway Right",  8680016, 102),
        LocationData("Golden Temple", "Golden Temple: Spider Ball",  8680017, 2),
        LocationData("Golden Temple", "Golden Temple: Exterior Ceiling",  8680018, 109, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),  # canspider
        LocationData("Golden Temple", "Golden Temple: EMP Room",  8680019, 110, lambda state: state.has("Super Missile", player) and logic.AM2R_has_ballspark(state) and logic.AM2R_can_bomb(state) and state.has("Screw Attack", player)),  # super + ballspark

        LocationData("Guardian", "Guardian: Up Above",  8680020, 111, lambda state: logic.AM2R_can_bomb(state) and ((logic.AM2R_can_schmove(state) and state.has("Bombs", player)) or logic.AM2R_can_fly(state))),  # bomb + schmove
        LocationData("Guardian", "Guardian: Behind The Door",  8680021, 112, lambda state: state.has("Power Bomb", player, 2) and ((logic.AM2R_can_spider(state)) or logic.AM2R_can_fly(state))),  # PB + schmove

        LocationData("Hydro Station", "Hydro Station: Cliff",  8680022, 163, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Hydro Station", "Hydro Station: Side Morph Tunnel",  8680023, 152),
        LocationData("Hydro Station", "Hydro Station: Turbine Room",  8680024, 150, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: Not so Secret Tunnel",  8680025, 151, logic.AM2R_can_schmove),  # schmove
        LocationData("Hydro Station", "Hydro Station: Water Pressure Pre-Varia",  8680026, 159, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: Varia Suit",  8680027, 5, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: EMP Room",  8680028, 162, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),  # super + speed

        LocationData("Arachnus", "Arachnus: Boss", 8680029, 3),

        LocationData("Inner Hydro Station", "Hydro Station: Wave Beam",  8680030, 12, logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Below Tower Pipe Upper",  8680031, 153, lambda state: logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),  # schmove
        LocationData("Inner Hydro Station", "Hydro Station: Below Tower Pipe Lower",  8680032, 154, logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Dead End",  8680033, 155, logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Hi-Jump Boots",  8680034, 4),
        LocationData("Inner Hydro Station", "Hydro Station: Behind Hi-Jump Boots Upper",  8680035, 156, lambda state: logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),
        LocationData("Inner Hydro Station", "Hydro Station: Behind Hi-Jump Boots Lower",  8680036, 157, logic.AM2R_can_bomb),

        LocationData("Hydro Nest", "Hydro Nest: Below the Walkway",  8680037, 158, logic.AM2R_can_bomb),  # Bomb
        LocationData("Hydro Nest", "Hydro Nest: Speed Ceiling",  8680038, 161, lambda state: state.has("Speed Booster", player)),  # speed
        LocationData("Hydro Nest", "Hydro Nest: Behind The Wall",  8680039, 160, lambda state: state.has("Power Bomb", player) and state.has("Screw Attack", player) and state.has("Speed Booster", player)),  # PB + screw/speed

        LocationData("Industrial Complex Nest", "Industrial Complex: Above Save",  8680040, 214),
        LocationData("Industrial Complex Nest", "Industrial Complex: EMP Room",  8680041, 213, lambda state: state.has("Power Bomb", player) and state.has("Super Missile", player) and state.can_reach("EMP", "Region", player)),  # PB + super
        LocationData("Industrial Complex Nest", "Industrial Complex Nest: Nest Shinespark",  8680042, 209, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player) and logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),  # super + schmove

        LocationData("Pre Industrial Complex", "Industrial Complex: In the Sand",  8680043, 211),
        LocationData("Pre Industrial Complex", "Industrial Complex: Complex Side After Tunnel",  8680044, 202, lambda state: (state.has("Speed Booster", player) or logic.AM2R_can_spider(state)) and logic.AM2R_can_bomb(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Complex Side Tunnel",  8680045, 200, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Behind the Green Door", 8680146, 212, lambda state: state.has("Speed Booster", player) and state.has("Power Bomb", player) and state.has("Super Missile", player) and logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Save Room",  8680046, 203, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Spazer Beam",  8680047, 13, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Sisyphus Spark",  8680048, 204, lambda state: state.has("Speed Booster", player)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Speed Booster",  8680049, 7, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_bomb(state)),  # bomb

        LocationData("Torizo Ascended", "Torizo Ascended: Boss", 8680050, 6, logic.AM2R_can_schmove),

        LocationData("Industrial Complex", "Industrial Complex: Conveyor Belt Room",  8680051, 205, lambda state: state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Doom Treadmill",  8680052, 201, lambda state: state.has("Speed Booster", player) and logic.AM2R_can_bomb(state)),
        LocationData("Industrial Complex", "Industrial Complex: Complex Hub Shinespark",  8680053, 208, lambda state: state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Complex Hub in the Floor", 8680054, 207, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Skippy Reward",  8680055, 206, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),

        LocationData("GFS Thoth", "GFS Thoth: Research Camp",  8680056, 215),
        LocationData("GFS Thoth", "GFS Thoth: Hornoad Room",  8680057, 58, lambda state: state.has("Power Bomb", player)),
        LocationData("GFS Thoth", "GFS Thoth: Outside the Front of the Ship",  8680058, 59, lambda state: state.has("Power Bomb", player)),
        LocationData("Genesis", "Genesis: Boss",  8680059, 50, lambda state: state.has("Power Bomb", player, 2)),

        LocationData("The Tower", "The Tower: Beside Hydro Pipe",  8680060, 259, lambda state: state.has("Screw Attack", player)),
        LocationData("The Tower", "The Tower: Right Side of Tower",  8680061, 250),
        LocationData("The Tower", "The Tower: In the Ceiling",  8680062, 257, lambda state: logic.AM2R_can_bomb(state) and (state.has("Space Jump", player) or state.has("Spider Ball", player))),  # spider + bomb
        LocationData("The Tower", "The Tower: Dark Maze",  8680063, 252, lambda state: state.has("Power Bomb", player, 4) or state.has("Bombs", player) and state.has("Spider Ball", player)),  # bomb
        LocationData("The Tower", "The Tower: After Dark Maze",  8680064, 251, lambda state: state.has("Power Bomb", player, 4) or state.has("Bombs", player) and state.has("Spider Ball", player)),
        LocationData("The Tower", "The Tower: Plasma Beam",  8680065, 14, lambda state: logic.AM2R_can_bomb(state) and state.can_reach("Tester", "Region", player)),
        LocationData("The Tower", "The Tower: After Tester",  8680066, 256, lambda state: state.has("Power Bomb", player)),  # pb
        LocationData("The Tower", "The Tower: Outside Reactor",  8680067, 258, lambda state: state.has("Power Bomb", player)),  # pb

        LocationData("Geothermal", "The Tower: Geothermal Reactor",  8680068, 253, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player) and logic.AM2R_can_schmove(state)),  # pb + speed + spider
        LocationData("Geothermal", "The Tower: Post Reactor Chozo",  8680069, 254, lambda state: state.has("Power Bomb", player, 3) and state.has("Speed Booster", player) and logic.AM2R_can_schmove(state)),  # pb
        LocationData("Geothermal", "The Tower: Post Reactor Shinespark",  8680070, 255, lambda state: state.has("Power Bomb", player, 3) and state.has("Speed Booster", player) and logic.AM2R_can_schmove(state) and state.has("Super Missile", player)),  # Pb + spped + super

        LocationData("Underwater Distribution Center", "Distribution Center: Main Room Shinespark",  8680071, 309, lambda state: state.has("Gravity Suit", player) and state.has("Speed Booster", player)),  # grav + screw
        LocationData("Underwater Distribution Center", "Distribution Center: Underwater Speed Hallway",  8680072, 307, lambda state: state.has("Speed Booster", player) and state.has("Gravity Suit", player)),  # speed + grav

        LocationData("EMP", "Distribution Center: After EMP Activation",  8680073, 300, lambda state: state.has("Screw Attack", player) and state.has("Speed Booster", player)),  # screw

        LocationData("Underwater Distro Connection", "Distribution Center: Spider Ball Crumble Spiky \"Maze\"",  8680074, 303, lambda state: state.has("Spider Ball", player) and state.has("Gravity Suit", player)),  # spiderball underwater
        LocationData("Underwater Distro Connection", "Distribution Center: Before Spiky Trial",  8680075, 304),
        LocationData("Underwater Distro Connection", "Distribution Center: Spiky Trial Shinespark",  8680076, 305, lambda state: state.has("Gravity Suit", player) and state.has("Speed Booster", player)),  # grav + speed
        LocationData("Underwater Distro Connection", "Distribution Center: After Spiky Trial",  8680078, 306, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player) and state.has("Gravity Suit", player) and state.has("Space Jump", player)),  # speed + grav + space + pb

        LocationData("Screw Attack", "Distribution Center: Screw Attack", 8680080, 8),
        LocationData("Pipe Hell Outside", "Distribution Center: Exterior Post-Gravity", 8680081, 302, lambda state: state.has("Power Bomb", player) and state.has("Space Jump", player) and state.has("Gravity Suit", player)),  # pb + space + grav
        LocationData("Pipe Hell R", "Distribution Center: Spectator Jail", 8680082, 301, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player)),  # pb + speed

        LocationData("Gravity", "Distribution Center: Before Gravity", 8680083, 308, lambda state: (state.has("Bombs", player) and (state.has("Charge Beam", player) or state.has("Gravity Suit", player))) or state.has("Power Bomb", player)),  # bomb + charge/gravity / PB
        LocationData("Gravity", "Distribution Center: Gravity Suit", 8680084, 9, logic.AM2R_can_bomb),  # can bomb

        LocationData("Ice Beam", "Serris: Ice Beam", 8680085, 11, lambda state: state.has("Ice Beam", player) and (state.has("Super Missile", player) or state.has("Speed Booster", player))),  # speed / Supers

        LocationData("Deep Caves", "Deep Caves: Drivel Ballspark",  8680086, 56, lambda state: state.has("Gravity Suit", player) and logic.AM2R_has_ballspark(state)),
        LocationData("Deep Caves", "Deep Caves: Ramulken Lava Pool",  8680087, 60, lambda state: state.has("Gravity Suit", player) and logic.AM2R_can_bomb),

        LocationData("Deep Caves", "Deep Caves: After Omega",  8680088, 51),

        LocationData("Research Station", "The Last Metroid is in Captivity", EventId),

        LocationData("First Alpha", "The Forgotten Alpha", 8680100, 310),

        LocationData("Golden Temple", "Golden Temple: Friendly Spider", 8680101, 311,  lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Golden Temple Nest", "Golden Temple Nest: Moe", 8680102, 312, logic.AM2R_can_bomb),  # Loj
        LocationData("Golden Temple Nest", "Golden Temple Nest: Larry", 8680103, 313, logic.AM2R_can_bomb),    # Loj
        LocationData("Golden Temple Nest", "Golden Temple Nest: Curly", 8680104, 314, logic.AM2R_can_bomb),    # Loj

        LocationData("Main Caves", "Main Caves: Freddy Fazbear", 8680105, 315),  # Epsilon
        LocationData("Hydro Station", "Hydro Station: Turbine Terror", 8680106, 316),  # Xander
        LocationData("Hydro Station", "Hydro Station: The Lookout", 8680107, 318, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_schmove),  # Xander
        LocationData("Hydro Station", "Hydro Station: Recent Guardian", 8680108, 317),  # ANX

        LocationData("Hydro Nest", "Hydro Nest: EnderMahan", 8680109, 319),
        LocationData("Hydro Nest", "Hydro Nest: Carnage Awful", 8680110, 320),
        LocationData("Hydro Nest", "Hydro Nest: Venom Awesome", 8680111, 321),
        LocationData("Hydro Nest", "Hydro Nest: Something More, Something Awesome", 8680112, 322),

        LocationData("Industrial Complex Nest", "Industrial Nest: Mimolette", 8680113, 326, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: The Big Cheese", 8680114, 327, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: Mohwir", 8680115, 328, lambda state: logic.AM2R_can_bomb(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: Chirn", 8680116, 329, lambda state: logic.AM2R_can_bomb(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: BHHarbinger", 8680117, 330, lambda state: logic.AM2R_can_bomb(state) and logic.AM2R_can_schmove(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: The Abyssal Creature", 8680118, 331, lambda state: logic.AM2R_can_bomb(state) and logic.AM2R_can_schmove(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),

        LocationData("Pre Industrial Complex", "Industrial Complex: Sisyphus", 8680119, 323, logic.AM2R_can_spider),  # Mimo
        LocationData("Pre Industrial Complex", "Industrial Complex: And then there\'s this Asshole", 8680120, 332, logic.AM2R_can_spider),  # ANX

        LocationData("Industrial Complex", "Inside Industrial: Guardian of Doom Treadmill", 8680121, 324, lambda state: state.has("Speed Booster", player) and logic.AM2R_can_bomb(state)),
        LocationData("Industrial Complex", "Inside Industrial: Rawsome1234 by the Lava Lake", 8680122, 325, lambda state: state.has("Speed Booster", player) and logic.AM2R_can_bomb(state) and (state.has("Gravity Suit", player) or state.has("Space Jump", player))),

        LocationData("GFS Thoth", "Dual Alphas: Marco", 8680123, 333),  # Epsilon
        LocationData("GFS Thoth", "Dual Alphas: Polo", 8680124, 334),  # Epsilon

        LocationData("Mines", "Mines: Unga", 8680125, 335, lambda state: state.has("Super Missile", player) and logic.AM2R_can_bomb(state) and (state.has("Space Jump", player) or state.has("Spider Ball", player))),
        LocationData("Mines", "Mines: Gunga", 8680126, 336, lambda state: state.has("Super Missile", player) and logic.AM2R_can_bomb(state) and (state.has("Space Jump", player) or state.has("Spider Ball", player))),

        LocationData("The Tower", "The Tower: Patricia", 8680127, 337, logic.AM2R_can_fly),  # Mahan
        LocationData("The Tower", "The Tower: Variable \"GUH\"", 8680128, 338, logic.AM2R_can_spider),  # ANX
        LocationData("The Tower", "Ruler of The Tower: Slagathor", 8680129, 340, lambda state: state.has("Power Bomb", player, 3) or state.has("Bombs", player)),  # Rawsome
        LocationData("The Tower", "The Tower: Mr.Sandman", 8680130, 339, lambda state: state.has("Space Jump", player) or state.has("Hi Jump") and state.has("Speed Booster")),  # Xander
        LocationData("The Tower", "The Tower: Anakin", 8680131, 341, lambda state: state.has("Space Jump", player)),  # Xander
        LocationData("The Tower", "The Tower: Xander", 8680132, 342, lambda state: state.has("Space Jump", player)),

        LocationData("EMP", "EMP: Sir Zeta Commander of the Alpha Squadron", 8680133, 343, lambda state: logic.AM2R_can_bomb(state) and state.has("Speed Booster", player)),  # Lucina

        LocationData("Pipe Hell R", "Alpha Squadron: Timmy", 8680134, 346),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Tommy", 8680135, 345),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Terry", 8680136, 348),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Telly", 8680137, 347),  # Lucina
        LocationData("Pipe Hell R", "Alpha Squadron: Martin", 8680138, 344),

        LocationData("Underwater Distro Connection", "Underwater: Gamma Bros Mario", 8680139, 349),  # Lucina
        LocationData("Underwater Distro Connection", "Underwater: Gamma Bros Luigi", 8680140, 350),  # Lucina

        LocationData("Deep Caves", "Deep Caves: Lil\' Bro", 8680141, 351),
        LocationData("Deep Caves", "Deep Caves: Big Sis", 8680142, 352),
        LocationData("Omega Nest", "Omega Nest: SA-X Queen Lucina", 8680143, 355),
        LocationData("Omega Nest", "Omega Nest: Epsilon", 8680144, 354),
        LocationData("Omega Nest", "Omega Nest: Druid", 8680145, 353),
    ]

    return tuple(location_table)
