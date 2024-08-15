from typing import Dict, List, Any

from BaseClasses import Region, Location, Item, Tutorial, ItemClassification
from worlds.generic.Rules import set_rule
from .items import item_name_to_id, item_table, filler_items, item_name_group, slot_data_item_names
from .locations import location_table, location_name_group, location_name_to_id
from .rules import create_region_rules, create_location_rules, blue_door, green_door, red_door, pink_door, \
    has_devastator
from .regions import snailiad_regions
from .options import SnailiadOptions
from worlds.AutoWorld import WebWorld, World
from decimal import Decimal, ROUND_HALF_UP


class SnailiadWeb(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name= "Multiworld Setup Guide",
            description= "A Guide to setting up a Snailiad+ Multiworld",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["Ehseezed, EpsilonTheDerg"]
        )
    ]
    theme = "ice"
    game = "Snailiad+"


class SnailiadItem(Item):
    game: str = "Snailiad"


class SnailiadLocation(Location):
    game: str = "Snailiad"


class SnailiadWorld(World):
    """
    Snail™
    """  # todo Description
    game = "Snailiad+"
    web = SnailiadWeb()

    data_version = 0
    options: SnailiadOptions
    options_dataclass = SnailiadOptions
    item_name_groups = item_name_group
    location_name_groups = location_name_group

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    slot_data_items: List[SnailiadItem]

    def generate_early(self) -> None:
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Snailiad" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Snailiad"]
                self.options.Progressive_Items.value = passthrough["Progressive_Items"]
                self.options.Randomization_Type.value = passthrough["Randomization_Type"]

    def create_item(self, name: str) -> SnailiadItem:
        item_data = item_table[name]
        return SnailiadItem(name, item_data.classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        character = self.options.Character_Select
        progressive = self.options.Progressive_Items
        helix_locks = self.options.Helix_Locks
        difficulty = self.options.Difficulty_Select
        traps = self.options.Trap_Fill

        nothings = 2  # SSB and DRW will never be generated
        nothings += 3  # Squared Snelks, Scorching Snelks, and Hidden Hideout did not have items in the original game they are rando exclusive

        snailiad_items: List[SnailiadItem] = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        if self.options.Randomization_Type.value != self.options.Randomization_Type.option_pro:
            nothings -= 5  # Original Testing Room, Scorching Snelks, Squared Snelks, Hidden Hideout and Lost Loot are not locations

        if progressive:
            items_to_create["Pea Shooter"] = 0
            items_to_create["Boomerang"] = 0
            items_to_create["Rainbow Wave"] = 0
            items_to_create["Progressive Weapon"] = 3

            items_to_create["Rapid Fire"] = 0
            items_to_create["Devastator"] = 0
            items_to_create["Progressive Modifier"] = 2

            items_to_create["Ice Snail"] = 0
            items_to_create["Gravity Shell"] = 0
            items_to_create["Full Metal Snail"] = 0
            if difficulty == difficulty.option_insane:
                items_to_create["Progressive Shell"] = 2
                nothings += 1
            else:
                items_to_create["Progressive Shell"] = 3

        if difficulty == difficulty.option_insane:
            items_to_create["Ice Snail"] = 0
            nothings += 1

        if character == character.option_sluggy:
            items_to_create["Shell Shield"] = 0
            nothings += 1

        if character == character.option_upside:
            items_to_create["Gravity Shell"] = 0
            items_to_create["Magnetic Foot"] = 1

        if character == character.option_leggy:
            items_to_create["Gravity Shell"] = 0
            items_to_create["Corkscrew Jump"] = 1

        if character == character.option_blobby:
            items_to_create["Gravity Shell"] = 0
            items_to_create["Angel Hop"] = 1

            items_to_create["High Jump"] = 0
            items_to_create["Wall Grab"] = 1

        if character == character.option_leechy:
            items_to_create["Shell Shield"] = 0
            nothings += 1

            items_to_create["Rapid Fire"] = 0
            items_to_create["Backfire"] = 1

    # my initial plan to swap the progression status did not work so I swapped to this combo setup from TUNIC and Mssenger for readbility and functionality
        if helix_locks:
            if self.options.Trap_Fill:
                total_pieces = 25
            else:
                total_pieces = 30
            req_pieces = 25
            fragments = [self.create_item("Helix Fragment") for _ in range(total_pieces)]
            for i in range(0, req_pieces):
                fragments[i].classification = ItemClassification.progression_skip_balancing
            items_to_create["Helix Fragment"] = 0

        items_to_create["Nothing"] = nothings

        req_hearts = 4
        hearts = [self.create_item("Heart Container") for _ in range(11)]
        for i in range(0, req_hearts):
            hearts[i].classification = ItemClassification.progression
        self.multiworld.itempool += hearts

        for item, quantity in items_to_create.items():
            for i in range(0, quantity):
                snailiad_item: SnailiadItem = self.create_item(item)
                snailiad_items.append(snailiad_item)

        self.multiworld.itempool += snailiad_items

    def create_regions(self) -> None:
        for region_name in snailiad_regions:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in snailiad_regions.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_exits(exits)

        for location_name, location_id in self.location_name_to_id.items():
            region = self.multiworld.get_region(location_table[location_name].region, self.player)
            location = SnailiadLocation(self.player, location_name, location_id, region)
            region.locations.append(location)

        if self.options.Randomization_Type.value != self.options.Randomization_Type.option_pro:
            a0 = self.multiworld.get_region("Snail Town", self.player)
            a0.locations.remove(self.multiworld.get_location("Original Testing Room", self.player))

            a2 = self.multiworld.get_region("Spiralis Silere", self.player)
            a2.locations.remove(self.multiworld.get_location("Squared Snelks", self.player))

            a3 = self.multiworld.get_region("Amastrida Abyssus", self.player)
            a3.locations.remove(self.multiworld.get_location("Scorching Snelks", self.player))
            a3.locations.remove(self.multiworld.get_location("Hidden Hideout", self.player))

            a4 = self.multiworld.get_region("Lux Lirata", self.player)
            a4.locations.remove(self.multiworld.get_location("Lost Loot", self.player))

        boss_1_region = self.multiworld.get_region("Mare Carelia", self.player)
        boss_1_location = SnailiadLocation(self.player, "Shell Breaker", None, boss_1_region)

        boss_1_location.place_locked_item(SnailiadItem("Boss 1", ItemClassification.progression, None, self.player))
        boss_1_region.locations.append(boss_1_location)

        boss_2_region = self.multiworld.get_region("Spiralis Silere", self.player)
        boss_2_location = SnailiadLocation(self.player, "Stompy", None, boss_2_region)
        boss_2_location.place_locked_item(SnailiadItem("Boss 2", ItemClassification.progression, None, self.player))
        boss_2_region.locations.append(boss_2_location)

        boss_3_region = self.multiworld.get_region("Amastrida Abyssus", self.player)
        boss_3_location = SnailiadLocation(self.player, "Space Box", None, boss_3_region)
        boss_3_location.place_locked_item(SnailiadItem("Boss 3", ItemClassification.progression, None, self.player))
        boss_3_region.locations.append(boss_3_location)

        boss_4_region = self.multiworld.get_region("Lux Lirata", self.player)
        boss_4_location = SnailiadLocation(self.player, "Moon Snail", None, boss_4_region)
        boss_4_location.place_locked_item(SnailiadItem("Boss 4", ItemClassification.progression, None, self.player))
        boss_4_region.locations.append(boss_4_location)

        helix_region = self.multiworld.get_region("Shrine of Iris", self.player)
        helix_location = SnailiadLocation(self.player, "Helix Fragment Cutscene", None, helix_region)
        helix_location.place_locked_item(SnailiadItem("All Helix\'s", ItemClassification.progression, None, self.player))
        helix_region.locations.append(helix_location)

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Boss 4", self.player)

    def set_rules(self) -> None:
        create_region_rules(self)
        create_location_rules(self)
        # Boss event location requirements
        if self.options.Helix_Locks:
            set_rule(self.multiworld.get_location("Shell Breaker", self.player),
                     lambda state: blue_door(state, self.player, self) and state.has("Helix Fragment", self.player, 5))
            set_rule(self.multiworld.get_location("Stompy", self.player),
                     lambda state: pink_door(state, self.player, self) and state.has("Helix Fragment", self.player, 10))
            set_rule(self.multiworld.get_location("Space Box", self.player),
                     lambda state: red_door(state, self.player, self) and state.has("Helix Fragment", self.player, 15))
            set_rule(self.multiworld.get_location("Moon Snail", self.player),
                     lambda state: green_door(state, self.player, self) and state.has("Helix Fragment", self.player, 25))
        else:
            set_rule(self.multiworld.get_location("Shell Breaker", self.player),
                     lambda state: blue_door(state, self.player, self))
            set_rule(self.multiworld.get_location("Stompy", self.player),
                     lambda state: pink_door(state, self.player, self))
            set_rule(self.multiworld.get_location("Space Box", self.player),
                     lambda state: red_door(state, self.player, self))
            set_rule(self.multiworld.get_location("Moon Snail", self.player),
                     lambda state: green_door(state, self.player, self) and has_devastator(state, self.player))


    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "seed": self.random.randint(0, 2147483647),
            "Randomization_Type": self.options.Randomization_Type.value,
            "Difficulty_Select": self.options.Difficulty_Select.value,
            "Character_Select": self.options.Character_Select.value,
            "Progressive_Items": self.options.Progressive_Items.value,
            "Start_With_Broom": self.options.Start_With_Broom.value,
            "Open_Areas": self.options.Open_Areas.value,
            "Helix_Locks": self.options.Helix_Locks.value,
            "Music_Shuffle": self.options.Music_Shuffle.value,
            "Snails_Have_Hints": self.options.Snails_Have_Hints.value,
            "Trap_Fill": self.options.Trap_Fill.value,
            "Hidden_Items": self.options.Hidden_Items.value
        }

        for start_item in self.options.start_inventory_from_pool:
            if start_item in slot_data_item_names:
                if start_item not in slot_data:
                    slot_data[start_item] = []
                for i in range(0, self.options.start_inventory_from_pool[start_item]):
                    slot_data[start_item].extend(["Your Shell(?)", self.player])

        for plando_item in self.multiworld.plando_items[self.player]:
            if plando_item["from_pool"]:
                items_to_find = set()
                for item_type in [key for key in ["item", "items"] if key in plando_item]:
                    for item in plando_item[item_type]:
                        items_to_find.add(item)
                for item in items_to_find:
                    if item in slot_data_item_names:
                        slot_data[item] = []
                        for item_location in self.multiworld.find_item_locations(item, self.player):
                            slot_data[item].extend([item_location.name, item_location.player])

        return slot_data

    @staticmethod  # for universal tracker
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
