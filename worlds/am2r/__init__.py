import types
from typing import Dict
from .items import item_table
from .locations import get_location_datas, EventId
from .regions import create_regions_and_locations
from BaseClasses import Tutorial, Item
from .options import AM2R_options, MetroidsAreChecks
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type, launch_subprocess


def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="AM2RClient")


components.append(Component("AM2R Client", "AM2RClient", func=launch_client, component_type=Type.CLIENT))


class AM2RWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago AM2R software on your computer. This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Zed"]
    )]


class AM2RWorld(World):
    """
    AM2R is a remake of the classic Metroid 2 game for the Game Boy that tries its best to keep the feel
    of the original as well as filling in some gaps to more closely tie into Metroid Fusion and brings some
    items from there as well.
    """
    game = "AM2R"
    option_definitions = options.AM2R_options
    web = AM2RWeb()

    item_name_to_id = items.item_name_to_id
    location_name_to_id = {location.name: location.code for location in get_location_datas(None, None)}

    item_name_groups = items.item_name_groups
    data_version = 1

    def fill_slot_data(self) -> Dict[str, object]:
        return {name: getattr(self.multiworld, name)[self.player].value for name in self.option_definitions}

    def create_regions(self) -> None:
        create_regions_and_locations(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return items.create_item(self.player, name)

    def create_items(self) -> None:
        if self.options.MetroidsAreChecks != MetroidsAreChecks.option_include_A6:
            self.multiworld.get_location("Deep Caves: Lil\' Bro", self.player).place_locked_item(self.create_item("Metroid"))
            self.multiworld.get_location("Deep Caves: Big Sis", self.player).place_locked_item(self.create_item("Metroid"))
            self.multiworld.get_location("Omega Nest: SA-X Queen Lucina", self.player).place_locked_item(self.create_item("Metroid"))
            self.multiworld.get_location("Omega Nest: Epsilon", self.player).place_locked_item(self.create_item("Metroid"))
            self.multiworld.get_location("Omega Nest: Druid", self.player).place_locked_item(self.create_item("Metroid"))
            if self.options.MetroidsAreChecks == MetroidsAreChecks.option_disabled:
                self.multiworld.get_location("The Forgotten Alpha", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Golden Temple: Friendly Spider", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Golden Temple Nest: Moe", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Golden Temple Nest: Larry", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Golden Temple Nest: Curly", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Main Caves: Freddy Fazbear", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Station: Turbine Terror", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Station: The Lookout", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Station: Recent Guardian", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Nest: EnderMahan", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Nest: Carnage Awful", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Nest: Venom Awesome", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Hydro Nest: Something More, Something Awesome",self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Nest: Mimolette", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Nest: The Big Cheese", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Nest: Mohwir", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Nest: Chirn", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Nest: BHHarbinger", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Nest: The Abyssal Creature", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Complex: Sisyphus", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Industrial Complex: And then there\'s this Asshole",self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Inside Industrial: Guardian of Doom Treadmill",self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Inside Industrial: Rawsome1234 by the Lava Lake",self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Dual Alphas: Marco", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Dual Alphas: Polo", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Mines: Unga", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Mines: Gunga", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("The Tower: Patricia", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("The Tower: Variable \"GUH\"", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Ruler of The Tower: Slagathor", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("The Tower: Mr.Sandman", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("The Tower: Anakin", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("The Tower: Xander", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("EMP: Sir Zeta Commander of the Alpha Squadron", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Alpha Squadron: Timmy", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Alpha Squadron: Tommy", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Alpha Squadron: Terry", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Alpha Squadron: Telly", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Alpha Squadron: Martin", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Underwater: Gamma Bros Mario", self.player).place_locked_item(self.create_item("Metroid"))
                self.multiworld.get_location("Underwater: Gamma Bros Luigi", self.player).place_locked_item(self.create_item("Metroid"))

        self.multiworld.get_location("The Last Metroid is in Captivity", self.player).place_locked_item(self.create_item("The Galaxy is at Peace"))
        items.create_all_items(self.multiworld, self.player)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("The Galaxy is at Peace", self.player)
