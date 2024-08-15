from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, PerGameCommonOptions


class RandomizationType(Choice):
    """Changes the type of randomization between a Major Minor split
    a full item randomizer and one that accounts for knowledge."""
    display_name = "Randomization Type"
    option_split = 0
    option_full = 1
    option_pro = 2
    default = 1


class DifficultySelect(Choice):
    """Changes the ingame difficulty."""
    display_name = "Difficulty"
    option_easy = 0
    option_normal = 1
    option_insane = 2
    default = 1


class CharacterSelect(Choice):
    """Chose your Adventurer"""
    display_name = "Character Select"
    option_snaily = 0
    option_sluggy = 1
    option_upside = 2
    option_leggy = 3
    option_blobby = 4
    option_leechy = 5
    default = 0


class ProgressiveItems(DefaultOnToggle):
    """an on/off switch that toggles the stacking of various items.
    There are three progressive items: Weapon (pea > boom > wave),
    Weapon Mod (rapid > devastator), and Shell (ice > grav > metal)"""
    display_name = "Progressive Items"


class StartWithBroom(Toggle):
    """toggles the option to start the character with a Broom weapon
    in slot zero. The Broom acts like a melee version of the Peashooter,
    able to dispatch enemies, open blue doors, and get upgraded by
    Rapid Fire and Devastator, but is held back by its rate of fire and range"""
    display_name = "Start with Broom"


class OpenAreas(Toggle):
    """Removes the grey boss doors separating the areas of the game"""
    display_name = "Open Areas"


class HelixLocks(Toggle):
    """lets you lock boss doors until you have a certain
    number of helix fragments under your belt.  You need
    5 for boss 1, 10 for boss 2, 15 for boss 3, and 25 for boss 4"""
    display_name = "Helix Locks"


class MusicShuffle(Choice):
    """Enables the Music Randomizer"""
    display_name = "Music Shuffle"
    option_off = 0
    option_area = 1
    option_full = 2
    default = 0


class SnailsHaveHints(Toggle):
    """Enables the Snail Randomizer"""
    display_name = "Snails Have Hints"


class TrapFill(Range):
    """Number of traps to be placed in the world"""
    display_name = "Trap Fill"
    range_start = 0
    range_end = 25
    default = 0


class HiddenItems(Toggle):
    """Changes the item appearance to not have a visual tell for what it is"""
    display_name = "Hidden Items"


@dataclass
class SnailiadOptions(PerGameCommonOptions):
    Randomization_Type: RandomizationType
    Difficulty_Select: DifficultySelect
    Character_Select: CharacterSelect
    Progressive_Items: ProgressiveItems
    Start_With_Broom: StartWithBroom
    Open_Areas: OpenAreas
    Helix_Locks: HelixLocks
    Music_Shuffle: MusicShuffle
    Snails_Have_Hints: SnailsHaveHints
    Trap_Fill: TrapFill
    Hidden_Items: HiddenItems
    start_inventory_from_pool: StartInventoryPool
