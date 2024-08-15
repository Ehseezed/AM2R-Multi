from typing import Union, List, Dict
from BaseClasses import MultiWorld
from Options import AssembleOptions, Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool, Toggle


class MetroidsRequired(Range):
    """Chose how many Metroids need to be killed or obtained to go through to the Omega Nest"""
    display_name = "Metroids Required for Omega Nest"
    range_start = 0
    range_end = 100
    default = 46


class MetroidsInPool(Range):
    """Chose how many Metroids will be in the pool, if Metroids are randomized.
    This will value will be ignored if smaller than the required amount"""
    display_name = "Total Metroids in Pool"
    range_start = 0
    range_end = 100
    default = 46


class LocationSettings(Choice):
    """Chose what items you want in the pool
    not including checks via the no_A6 will force them to be excluded
    not adding Metroids will force them to be vanilla and will not randomize them into item locations
    adding metroids but excluding A6 will leave the A6 and omega nest metroids vanilla but will leave the full amount in the pool"""
    display_name = "Locations to Check"
    default = 2
    option_items_no_A6 = 0
    option_items_and_A6 = 1
    option_add_metroids_no_A6 = 2
    option_add_metroids_and_A6 = 3


class TrapFillPercentage(Range):
    """Adds in slightly inconvenient traps into the item pool"""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class RemoveFloodTrap(Toggle):
    """Removes Flood Traps from trap fill"""
    display_name = "Remove Flood Trap"


class RemoveTossTrap(Toggle):
    """There is a pipebomb in your mailbox"""
    display_name = "Remove Toss Trap"


class RemoveShortBeam(Toggle):
    """Remove muscle memory trap"""
    display_name = "Remove Short Beam"


class RemoveEMPTrap(Toggle):
    """Yes we know that it looks weird during the idle animation, but it's a vanilla bug"""
    display_name = "Remove EMP Trap"


class RemoveTouhouTrap(Toggle):
    """Removes Touhou Traps from trap fill"""
    display_name = "Remove Touhou Trap"


class RemoveOHKOTrap(Toggle):
    """Removes OHKO Traps from trap fill"""
    display_name = "Remove OHKO Trap"


#class ItemSprites(OptionList):
#    """Changes Item Sprites.  Does not affect gameplay
#    Sprite Authors appear in the item description"""
#    display_name = "Item Sprites"
#    default = 0
#    option_default = 0
#    option_themed = 1
#    option_chiny = 2
#    option_ungrouped = 3
#    option_lies = 4


#class StartingWeapons(Choice):
#    """Removes your Arm Cannon and makes it a findable item"""
#    display_name = "Starting Weapons"
#    default = 0
#    option_normal = 0
#    option_missiles_only = 1
#    option_beam_only = 2
#    option_none = 3


#class RandomizeBaby(Toggle):
#    """Randomizes the baby metroid as a cosmetic find"""
#    display_name = "Randomize Baby"


#class AreaRando(Choice):
#    """Activates Area Randomization and or Boss Randomization, also activates rolling saves as softlock prevention
#    Area Randomizer will shuffle various Areas arround in order to create a new expierence
#    Boss Randomization randomizes Arachnus, Torizo Ascended, and Genesis with each other also then randomizes
#    Temple Guardian, Tester and Serris
#    Both activates Both independently on their own"""
#    display_name = "Area Randomizer"
#
#    default = 0
#    option_disabled = 0
#    option_area = 1
#    option_boss = 2
#    option_both = 3


#  class IceMissiles(Toggle):
#  """Changes missiles to have Ice properties
#  Does not account for jumping off enemies
#  only counts as being able to freeze meboids and metroid larva"""
#  display_name = "Ice Missiles"


AM2R_options: Dict[str, AssembleOptions] = {
    "MetroidsRequired": MetroidsRequired,
    "MetroidsInPool": MetroidsInPool,
    "LocationSettings": LocationSettings,
    "TrapFillPercentage": TrapFillPercentage,
    "RemoveFloodTrap": RemoveFloodTrap,
    "RemoveTossTrap": RemoveTossTrap,
    "RemoveShortBeam": RemoveShortBeam,
    "RemoveEMPTrap": RemoveEMPTrap,
    "RemoveTouhouTrap": RemoveTouhouTrap,
    "RemoveOHKOTrap": RemoveOHKOTrap,
    #  "Item Sprites": ItemSprites,
    #  "Starting Weapons": StartingWeapons,
    #  "Randomize Baby", RandomizeBaby
    #  "Area Rando": AreaRando,
    #  "Ice Missiles":  IceMissiles,
    #  "DeathLink": DeathLink,
}


def is_option_enabled(world: MultiWorld, player: int, name: str) -> bool:
    return get_option_value(world, player, name) > 0


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
