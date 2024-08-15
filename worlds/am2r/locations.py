from typing import Dict, Set, NamedTuple
from itertools import groupby


class AM2RLocationData(NamedTuple):
    region: str
    game_id: int = 0
    location_group: str = "region"


location_based_id = 8678000

location_table: Dict[str, AM2RLocationData] = {
    "Main Caves: Spider Ball Challenge Upper":                  AM2RLocationData("Main Caves", 53),
    "Main Caves: Spider Ball Challenge Lower":                  AM2RLocationData("Main Caves", 52),
    "Main Caves: Hi-Jump Challenge":                            AM2RLocationData("Main Caves", 57),
    "Main Caves: Spiky Maze":                                   AM2RLocationData("Main Caves", 210),
    "Main Caves: Shinespark Before The Pit":                    AM2RLocationData("Main Caves", 54),
    "Main Caves: Shinespark After The Pit":                     AM2RLocationData("Main Caves", 55),

    "Golden Temple: Bombs":                                     AM2RLocationData("Golden Temple", 0),
    "Golden Temple: Below Bombs":                               AM2RLocationData("Golden Temple", 100),
    "Golden Temple: Hidden Energy Tank":                        AM2RLocationData("Golden Temple", 103),
    "Golden Temple: Charge Beam":                               AM2RLocationData("Golden Temple", 10),
    "Golden Temple: Armory Left":                               AM2RLocationData("Golden Temple", 104),
    "Golden Temple: Armory Upper":                              AM2RLocationData("Golden Temple", 106),
    "Golden Temple: Armory Lower":                              AM2RLocationData("Golden Temple", 105),
    "Golden Temple: Armory False Wall":                         AM2RLocationData("Golden Temple", 107),
    "Golden Temple: 3-Orb Hallway Left":                        AM2RLocationData("Golden Temple", 101),
    "Golden Temple: 3-Orb Hallway Middle":                      AM2RLocationData("Golden Temple", 108),
    "Golden Temple: 3-Orb Hallway Right":                       AM2RLocationData("Golden Temple", 102),
    "Golden Temple: Spider Ball":                               AM2RLocationData("Golden Temple", 2),
    "Golden Temple: Exterior Ceiling":                          AM2RLocationData("Golden Temple", 109),
    "Golden Temple: EMP Room":                                  AM2RLocationData("Golden Temple", 110),

    "Guardian: Up Above":                                       AM2RLocationData("Guardian", 111),
    "Guardian: Behind The Door":                                AM2RLocationData("Guardian", 112,),

    "Hydro Station: Cliff":                                     AM2RLocationData("Hydro Station", 163),
    "Hydro Station: Side Morph Tunnel":                         AM2RLocationData("Hydro Station", 152),
    "Hydro Station: Turbine Room":                              AM2RLocationData("Hydro Station", 150),
    "Hydro Station: Not so Secret Tunnel":                      AM2RLocationData("Hydro Station", 151),
    "Hydro Station: Water Pressure Pre-Varia":                  AM2RLocationData("Hydro Station", 159),
    "Hydro Station: Varia Suit":                                AM2RLocationData("Hydro Station", 5),
    "Hydro Station: EMP Room":                                  AM2RLocationData("Hydro Station", 162),

    "Arachnus: Boss":                                           AM2RLocationData("Arachnus", 3),

    "Hydro Station: Wave Beam":                                 AM2RLocationData("Inner Hydro Station", 12),
    "Hydro Station: Below Tower Pipe Upper":                    AM2RLocationData("Inner Hydro Station", 153),
    "Hydro Station: Below Tower Pipe Lower":                    AM2RLocationData("Inner Hydro Station", 154),
    "Hydro Station: Dead End":                                  AM2RLocationData("Inner Hydro Station", 155),
    "Hydro Station: Hi-Jump Boots":                             AM2RLocationData("Inner Hydro Station", 4),
    "Hydro Station: Behind Hi-Jump Boots Upper":                AM2RLocationData("Inner Hydro Station", 156),
    "Hydro Station: Behind Hi-Jump Boots Lower":                AM2RLocationData("Inner Hydro Station", 157),

    "Hydro Nest: Below the Walkway":                            AM2RLocationData("Hydro Nest", 158),
    "Hydro Nest: Speed Ceiling":                                AM2RLocationData("Hydro Nest", 161),
    "Hydro Nest: Behind The Wall":                              AM2RLocationData("Hydro Nest", 160),

    "Industrial Complex: Above Save":                           AM2RLocationData("Industrial Complex Nest", 214),
    "Industrial Complex: EMP Room":                             AM2RLocationData("Industrial Complex Nest", 213),
    "Industrial Complex Nest: Nest Shinespark":                 AM2RLocationData("Industrial Complex Nest", 209),

    "Industrial Complex: In the Sand":                          AM2RLocationData("Pre Industrial Complex", 211),
    "Industrial Complex: Complex Side After Tunnel":            AM2RLocationData("Pre Industrial Complex", 202),
    "Industrial Complex: Complex Side Tunnel":                  AM2RLocationData("Pre Industrial Complex", 200),
    "Industrial Complex: Behind the Green Door":                AM2RLocationData("Pre Industrial Complex", 212),
    "Industrial Complex: Save Room":                            AM2RLocationData("Pre Industrial Complex", 203),
    "Industrial Complex: Spazer Beam":                          AM2RLocationData("Pre Industrial Complex", 13),
    "Industrial Complex: Sisyphus Spark":                       AM2RLocationData("Pre Industrial Complex", 204),
    "Industrial Complex: Speed Booster":                        AM2RLocationData("Pre Industrial Complex", 7),

    "Torizo Ascended: Boss":                                    AM2RLocationData("Torizo Ascended", 6),

    "Industrial Complex: Conveyor Belt Room":                   AM2RLocationData("Industrial Complex", 205),
    "Industrial Complex: Doom Treadmill":                       AM2RLocationData("Industrial Complex", 201),
    "Industrial Complex: Complex Hub Shinespark"                AM2RLocationData("Industrial Complex", 208),
    "Industrial Complex: Complex Hub in the Floor":             AM2RLocationData("Industrial Complex", 207),
    "Industrial Complex: Skippy Reward":                        AM2RLocationData("Industrial Complex", 206),

    "GFS Thoth: Research Camp":                                 AM2RLocationData("GFS Thoth", 215),
    "GFS Thoth: Hornoad Room":                                  AM2RLocationData("GFS Thoth", 58),
    "GFS Thoth: Outside the Front of the Ship":                 AM2RLocationData("GFS Thoth", 59),

    "Genesis: Boss":                                            AM2RLocationData("Genesis", 50),

    "The Tower: Beside Hydro Pipe":                             AM2RLocationData("The Tower", 259),
    "The Tower: Right Side of Tower":                           AM2RLocationData("The Tower", 250),
    "The Tower: In the Ceiling":                                AM2RLocationData("The Tower", 257),
    "The Tower: Dark Maze":                                     AM2RLocationData("The Tower", 252),
    "The Tower: After Dark Maze":                               AM2RLocationData("The Tower", 251),
    "The Tower: Plasma Beam":                                   AM2RLocationData("The Tower", 14),
    "The Tower: After Tester":                                  AM2RLocationData("The Tower", 256),
    "The Tower: Outside Reactor":                               AM2RLocationData("The Tower", 258),

    "The Tower: Geothermal Reactor":                            AM2RLocationData("Geothermal", 253),
    "The Tower: Post Reactor Chozo":                            AM2RLocationData("Geothermal", 254),
    "The Tower: Post Reactor Shinespark":                       AM2RLocationData("Geothermal", 255),

    "Distribution Center: Main Room Shinespark":                AM2RLocationData("Underwater Distribution Center", 309),
    "Distribution Center: Underwater Speed Hallway":            AM2RLocationData("Underwater Distribution Center", 307),

    "Distribution Center: After EMP Activation":                AM2RLocationData("EMP", 300),

    "Distribution Center: Spider Ball Crumble Spiky \"Maze\"":  AM2RLocationData("Underwater Distro Connection", 303),
    "Distribution Center: Before Spiky Trial":                  AM2RLocationData("Underwater Distro Connection", 304),
    "Distribution Center: Spiky Trial Shinespark":              AM2RLocationData("Underwater Distro Connection", 305),
    "Distribution Center: After Spiky Trial":                   AM2RLocationData("Underwater Distro Connection", 306),

    "Distribution Center: Screw Attack":                        AM2RLocationData("Screw Attack", 8),
    "Distribution Center: Exterior Post-Gravity":               AM2RLocationData("Pipe Hell Outside", 302),
    "Distribution Center: Spectator Jail":                      AM2RLocationData("Pipe Hell R", 301),

    "Distribution Center: Before Gravity":                      AM2RLocationData("Gravity", 308),
    "Distribution Center: Gravity Suit":                        AM2RLocationData("Gravity", 9),

    "Serris: Ice Beam":                                         AM2RLocationData("Ice Beam", 11),

    "Deep Caves: Drivel Ballspark":                             AM2RLocationData("Deep Caves", 56),
    "Deep Caves: Ramulken Lava Pool":                           AM2RLocationData("Deep Caves", 60),

    "Deep Caves: After Omega":                                  AM2RLocationData("Deep Caves", 51),

    "The Forgotten Alpha":                                      AM2RLocationData("First Alpha", 310),

    "Golden Temple: Friendly Spider":                           AM2RLocationData("Golden Temple", 311),

    "Golden Temple Nest: Moe":                                  AM2RLocationData("Golden Temple Nest", 312),
    "Golden Temple Nest: Larry":                                AM2RLocationData("Golden Temple Nest", 313),
    "Golden Temple Nest: Curly":                                AM2RLocationData("Golden Temple Nest", 314),

    "Main Caves: Freddy Fazbear":                               AM2RLocationData("Main Caves", 315),

    "Hydro Station: Turbine Terror":                            AM2RLocationData("Hydro Station", 316),
    "Hydro Station: The Lookout":                               AM2RLocationData("Hydro Station", 318),
    "Hydro Station: Recent Guardian":                           AM2RLocationData("Hydro Station", 317),

    "Hydro Nest: EnderMahan":                                   AM2RLocationData("Hydro Nest", 319),
    "Hydro Nest: Carnage Awful":                                AM2RLocationData("Hydro Nest", 320),
    "Hydro Nest: Venom Awesome":                                AM2RLocationData("Hydro Nest", 321),
    "Hydro Nest: Something More, Something Awesome":            AM2RLocationData("Hydro Nest", 322),

    "Industrial Nest: Mimolette":                               AM2RLocationData("Industrial Complex Nest", 326),
    "Industrial Nest: The Big Cheese":                          AM2RLocationData("Industrial Complex Nest", 327),
    "Industrial Nest: Mohwir":                                  AM2RLocationData("Industrial Complex Nest", 328),
    "Industrial Nest: Chirn":                                   AM2RLocationData("Industrial Complex Nest", 329),
    "Industrial Nest: BHHarbinger":                             AM2RLocationData("Industrial Complex Nest", 330),
    "Industrial Nest: The Abyssal Creature":                    AM2RLocationData("Industrial Complex Nest", 331),

    "Industrial Complex: Sisyphus":                             AM2RLocationData("Pre Industrial Complex", 323),
    "Industrial Complex: And then there\'s this Asshole":       AM2RLocationData("Pre Industrial Complex", 332),

    "Inside Industrial: Guardian of Doom Treadmill":            AM2RLocationData("Industrial Complex", 324),
    "Inside Industrial: Rawsome1234 by the Lava Lake":          AM2RLocationData("Industrial Complex", 325),

    "Dual Alphas: Marco":                                       AM2RLocationData("GFS Thoth", 333),
    "Dual Alphas: Polo":                                        AM2RLocationData("GFS Thoth", 334),

    "Mines: Unga":                                              AM2RLocationData("Mines", 335),
    "Mines: Gunga":                                             AM2RLocationData("Mines", 336),

    "The Tower: Patricia":                                      AM2RLocationData("The Tower", 337),
    "The Tower: Variable \"GUH\"":                              AM2RLocationData("The Tower", 338),
    "Ruler of The Tower: Slagathor":                            AM2RLocationData("The Tower", 340),
    "The Tower: Mr.Sandman":                                    AM2RLocationData("The Tower", 339),
    "The Tower: Anakin":                                        AM2RLocationData("The Tower", 341),
    "The Tower: Xander":                                        AM2RLocationData("The Tower", 342),

    "EMP: Sir Zeta Commander of the Alpha Squadron":            AM2RLocationData("EMP", 343),

    "Alpha Squadron: Timmy":                                    AM2RLocationData("Pipe Hell R", 346),
    "Alpha Squadron: Tommy":                                    AM2RLocationData("Pipe Hell R", 345),
    "Alpha Squadron: Terry":                                    AM2RLocationData("Pipe Hell R", 348),
    "Alpha Squadron: Telly":                                    AM2RLocationData("Pipe Hell R", 347),
    "Alpha Squadron: Martin":                                   AM2RLocationData("Pipe Hell R", 344),

    "Underwater: Gamma Bros Mario":                             AM2RLocationData("Underwater Distro Connection", 349),
    "Underwater: Gamma Bros Luigi":                             AM2RLocationData("Underwater Distro Connection", 350),

    "Deep Caves: Lil\' Bro":                                    AM2RLocationData("Deep Caves", 351),
    "Deep Caves: Big Sis":                                      AM2RLocationData("Deep Caves", 352),
    "Omega Nest: Lucina":                                       AM2RLocationData("Omega Nest", 355),
    "Omega Nest: Epsilon":                                      AM2RLocationData("Omega Nest", 354),
    "Omega Nest: Druid":                                        AM2RLocationData("Omega Nest", 353),

    "The Last Metroid is in Captivity":                         AM2RLocationData("Research Station", None),
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
