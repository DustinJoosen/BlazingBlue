
# Constants based on the new mon.

NAME = "Orbeetle"
LOWER_NAME = NAME.lower()
UPPER_NAME = NAME.upper()

CATEGORY_NAME = "SEVEN SPOT"
HEIGHT = 0.4
WEIGHT = 40.8
POKEMON_SCALE = 128
POKEMON_OFFSET = 0
TRAINER_SCALE = 290
TRAINER_OFFSET = 2

EVOLUTION = ["EVO_LEVEL", 30, "SPECIES_DITTO"]

POKEDEX_TEXT = [
    "It emits psychic energy to observe",
    "and study what's around it—and what's",
    "around it can include things over six",
    "miles away."
]

LEARNED_MOVES = [
    [1, "MOVE_CONFUSION"],
    [1, "MOVE_LIGHT_SCREEN"],
    [1, "MOVE_REFLECT"],
    [1, "MOVE_PIN_MISSILE"],
    [4, "MOVE_CONFUSE_RAY"],
    [8, "MOVE_MAGIC_COAT"],
    [12, "MOVE_AGILITY"],
    [16, "MOVE_PSYBEAM"],
    [20, "MOVE_HYPNOSIS"],
    [32, "MOVE_MIRROR_COAT"],
    [36, "MOVE_PSYCHIC"],
    [44, "MOVE_CALM_MIND"],
]

ALLOWED_TMS_AND_HMS = [
    "HYPER_BEAM",
    "SOLAR_BEAM",
    "LIGHT_SCREEN",
    "REFLECT",
    "SAFEGUARD",
    "REST",
    "PROTECT",
    "GIGA_DRAIN",
    "ATTRACT",
    "FACADE",
]
SPECIES_INFO = {
    "base_hp": 60,
    "base_attack": 45,
    "base_defense": 110,
    "base_sp_attack": 80,
    "base_sp_defence": 120,
    "base_speed": 90,
    "type_1": "TYPE_BUG",
    "type_2": "TYPE_PSYCHIC",
    "catch_rate": 45,
    "exp_yield": 253,
    "ev_yield_hp": 0,
    "ev_yield_attack": 0,
    "ev_yield_defense": 0,
    "ev_yield_speed": 0,
    "ev_yield_sp_attack": 0,
    "ev_yield_sp_defense": 3,
    "gender_ratio": "PERCENT_FEMALE(50)",
    "egg_cycles": 15,
    "friendship": 50,
    "growth_rate": "GROWTH_MEDIUM_FAST",
    "egg_group_1": "EGG_GROUP_BUG",
    "egg_group_2": "EGG_GROUP_BUG",
    "ability_1": "ABILITY_SWARM",
    "ability_2": "ABILITY_SWARM",
    "body_color": "BODY_COLOR_RED",
    "safari_zone_flee_rate": 0,
    "no_flip": "FALSE",
    "item_common": "ITEM_NONE",
    "item_rare": "ITEM_NONE"
}


# Handy functions

def default_add_text_before_trigger(trigger_line, file_path, text):
    with open(file_path, "r") as inp_handle:
        new_text = ""

        for line in inp_handle.readlines():
            if trigger_line in line:
                new_text += text
            
            new_text += line

        with open(file_path, "w") as out_handle:
            out_handle.write(new_text)


def default_add_text_after_trigger(trigger_line, file_path, text):
    with open(file_path, "r") as inp_handle:
        new_text = ""

        for line in inp_handle.readlines():
            new_text += line

            if trigger_line in line:
                new_text += text
            

        with open(file_path, "w") as out_handle:
            out_handle.write(new_text)


def default_add_text_end_of_file(file_path, text):
    with open(file_path, "r") as inp_handle:
        content = inp_handle.read()
        content += text

        with open(file_path, "w") as out_handle:
            out_handle.write(content)
            print


#1.1

def register_sprite_1():
    # Generate text
    text = ""

    text += f"extern const u32 gMonFrontPic_{NAME}[];\n"
    text += f"extern const u32 gMonPalette_{NAME}[];\n"
    text += f"extern const u32 gMonBackPic_{NAME}[];\n"
    text += f"extern const u32 gMonShinyPalette_{NAME}[];\n"
    text += f"extern const u32 gMonStillFrontPic_{NAME}[];\n"
    text += f"extern const u8 gMonIcon_{NAME}[];\n"
    text += f"extern const u8 gMonFootprint_{NAME}[];\n"

    # Add to file
    trigger_line = "extern const u32 gMonPic_Egg[];"
    file_path = "pokeemerald/include/graphics.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_sprite_2():
    # Generate text
    text = ""

    text += f"const u32 gMonStillFrontPic_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/front.4bpp.lz\");\n"
    text += f"const u32 gMonPalette_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/normal.gbapal.lz\");\n"
    text += f"const u32 gMonBackPic_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/back.4bpp.lz\");\n"
    text += f"const u32 gMonShinyPalette_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/shiny.gbapal.lz\");\n"
    text += f"const u32 gMonIcon_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/icon.4bpp\");\n"
    text += f"const u32 gMonFootprint_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/footprint.1bpp\");\n\n"

    # Add to file
    trigger_line = "// Probably the leftover space from the other Deoxys forms"
    file_path = "pokeemerald/src/data/graphics/pokemon.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_sprite_3():
    # Generate text
    text = f"const u32 gMonFrontPic_{NAME}[] = INCBIN_U32(\"graphics/pokemon/{LOWER_NAME}/anim_front.4bpp.lz\");\n"

    # Add to file
    trigger_line = 'const u32 gMonFrontPic_Egg[] = INCBIN_U32("graphics/pokemon/egg/anim_front.4bpp.lz");'
    file_path = "pokeemerald/src/anim_mon_front_pics.c"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_sprite_4():
    # Generate text
    text = ""

    text += f"static const union AnimCmd sAnim_{NAME}_1[] = \n"
    text += "{\n"
    text += "\tANIMCMD_FRAME(1, 30),\n"
    text += "\tANIMCMD_FRAME(0, 20),\n"
    text += "\tANIMCMD_END,\n"
    text += "};\n\n"

    # Add to file
    trigger_line = "static const union AnimCmd sAnim_Egg_1[] ="
    file_path = "pokeemerald/src/data/pokemon_graphics/front_pic_anims.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_sprite_5():
    # Generate text
    text = f"SINGLE_ANIMATION({NAME});\n"

    # Add to file
    trigger_line = "SINGLE_ANIMATION(Egg);"
    file_path = "pokeemerald/src/data/pokemon_graphics/front_pic_anims.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_sprite_6():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}]         = sAnims_{NAME},\n"

    # Add to file
    trigger_line = "[SPECIES_EGG]         = sAnims_Egg,"
    file_path = "pokeemerald/src/data/pokemon_graphics/front_pic_anims.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_1():
    # Generate text
    text = f"\tSPECIES_SPRITE({UPPER_NAME}, gMonFrontPic_{NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_SPRITE(EGG, gMonFrontPic_Egg),"
    file_path = "pokeemerald/src/data/pokemon_graphics/front_pic_table.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_2():
    # Generate text
    text = f"\tSPECIES_SPRITE({UPPER_NAME}, gMonStillFrontPic_{NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_SPRITE(EGG,           gMonStillFrontPic_Egg),"
    file_path = "pokeemerald/src/data/pokemon_graphics/still_front_pic_table.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_3():
    # Generate text
    text = "\t[SPECIES_" + UPPER_NAME + "]   = { .size = 0x88, .y_offset =  8 },\n"

    # Add to file
    trigger_line = "[SPECIES_EGG]         = { .size = MON_COORDS_SIZE(24, 24), .y_offset = 20 },"
    file_path = "pokeemerald/src/data/pokemon_graphics/front_pic_coordinates.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_4():
    # Generate text
    text = f"\tSPECIES_SPRITE({UPPER_NAME}, gMonBackPic_{NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_SPRITE(EGG, gMonStillFrontPic_Egg),"
    file_path = "pokeemerald/src/data/pokemon_graphics/back_pic_table.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_5():
    # Generate text
    text = "\t[SPECIES_" + UPPER_NAME + "]   = { .size = 0x88, .y_offset =  10 },\n"

    # Add to file
    trigger_line = "[SPECIES_EGG]         = { .size = MON_COORDS_SIZE(24, 48), .y_offset = 10 },"
    file_path = "pokeemerald/src/data/pokemon_graphics/back_pic_coordinates.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_6():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}] = gMonFootprint_{NAME},\n"

    # Add to file
    trigger_line = "[SPECIES_EGG] = gMonFootprint_Bulbasaur,"
    file_path = "pokeemerald/src/data/pokemon_graphics/footprint_table.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_7():
    # Generate text
    text = f"\tSPECIES_PAL({UPPER_NAME}, gMonPalette_{NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_PAL(EGG, gMonPalette_Egg),"
    file_path = "pokeemerald/src/data/pokemon_graphics/palette_table.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_8():
    # Generate text
    text = f"\tSPECIES_SHINY_PAL({UPPER_NAME}, gMonPalette_{NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_SHINY_PAL(EGG, gMonPalette_Egg),"
    file_path = "pokeemerald/src/data/pokemon_graphics/shiny_palette_table.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def update_tables_9():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}] = gMonIcon_{NAME},\n"

    # Add to file
    trigger_line = "[SPECIES_EGG] = gMonIcon_Egg,"
    file_path = "pokeemerald/src/pokemon_icon.c"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")
    

def update_tables_10():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}] = 1,\n"

    # Add to file
    trigger_line = "[SPECIES_EGG] = 1,"
    file_path = "pokeemerald/src/pokemon_icon.c"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def add_species_constant():
    # Get old egg num
    old_egg_num: int = 0
    with open("pokeemerald/include/constants/species.h", "r") as egg_handle:
        for line in egg_handle.readlines():
            if "#define SPECIES_EGG" in line:
                old_egg_num: int = int(line.replace("#define SPECIES_EGG ", ""))

    # Make the new text
    text = ""
    text += f"#define SPECIES_{UPPER_NAME} {old_egg_num}\n"
    text += f"#define SPECIES_EGG {old_egg_num + 1}"

    # Replace the egg definition with both of these.
    with open("pokeemerald/include/constants/species.h", "r") as read_handle:
        content = read_handle.read()
        content = content.replace(f"#define SPECIES_EGG {old_egg_num}", text)

        with open("pokeemerald/include/constants/species.h", "w") as write_handle:
            write_handle.write(content)

    print("Done.")


def register_species_name():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}] = _(\"{UPPER_NAME}\"),\n"

    # Add to file
    trigger_line = "};"
    file_path = "pokeemerald/src/data/text/species_names.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")



def register_species_dex_entry_1():
    # Generate text
    text = f"    NATIONAL_DEX_{UPPER_NAME},\n"

    # Add to file
    trigger_line = "// Old Unown"
    file_path = "pokeemerald/include/constants/pokedex.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_species_dex_entry_2():
    file_path = "pokeemerald/include/constants/pokedex.h"
    trigger = "#define NATIONAL_DEX_COUNT  NATIONAL_DEX_"

    main_line: str = ""
    with open(file_path, "r") as handle:
        for line in handle.readlines():
            if trigger in line:
                main_line = line
                break

    with open(file_path, "r") as r_handle:
        content = r_handle.read()
        content = content.replace(main_line, f"#define NATIONAL_DEX_COUNT  NATIONAL_DEX_{UPPER_NAME}\n")

        with open(file_path, "w") as w_handle:
            w_handle.write(content)

    print("Done.")

def register_species_dex_entry_3():
    # Generate text
    text = f"    HOENN_DEX_{UPPER_NAME},\n"

    # Add to file
    trigger_line = "// End of Hoenn Dex (see HOENN_DEX_COUNT)"
    file_path = "pokeemerald/include/constants/pokedex.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_species_dex_entry_4():
    file_path = "pokeemerald/include/constants/pokedex.h"
    trigger = "#define HOENN_DEX_COUNT HOENN_DEX_"

    main_line: str = ""
    with open(file_path, "r") as handle:
        for line in handle.readlines():
            if trigger in line:
                main_line = line
                break

    with open(file_path, "r") as r_handle:
        content = r_handle.read()
        content = content.replace(main_line, f"#define HOENN_DEX_COUNT HOENN_DEX_{UPPER_NAME}\n")

        with open(file_path, "w") as w_handle:
            w_handle.write(content)

    print("Done.")


def register_species_to_pokedex_1():
    # Generate text
    text = f"\tSPECIES_TO_HOENN({UPPER_NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_TO_HOENN(CHIMECHO),"
    file_path = "pokeemerald/src/pokemon.c"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")


def register_species_to_pokedex_2():
    # Generate text
    text = f"\tSPECIES_TO_NATIONAL({UPPER_NAME}),\n"

    # Add to file
    trigger_line = "SPECIES_TO_NATIONAL(CHIMECHO),"
    file_path = "pokeemerald/src/pokemon.c"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")


def register_species_to_pokedex_3():
    # Generate text
    text = f"\tHOENN_TO_NATIONAL({UPPER_NAME}),\n"

    # Add to file
    trigger_line = "HOENN_TO_NATIONAL(CELEBI),"
    file_path = "pokeemerald/src/pokemon.c"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")


def add_pokedex_text():
    # Generate text

    text = f"const u8 g{NAME}PokedexText[] = _(\n"
    for line in POKEDEX_TEXT:
        text += f"\t\"{line}\\n\"\n"
    text += ");\n\n"

    # Add to file
    trigger_line = "const u8 gDeoxysPokedexText[] = _("
    file_path = "pokeemerald/src/data/pokemon/pokedex_text.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def add_pokedex_entry():
    # Generate text
    text = f"\t[NATIONAL_DEX_{UPPER_NAME}] = \n"
    text += "\t{\n"

    text += f"\t\t.categoryName = _(\"{CATEGORY_NAME}\"),\n"
    text += f"\t\t.height = {HEIGHT},\n"
    text += f"\t\t.weight = {WEIGHT},\n"
    text += f"\t\t.description = g{NAME}PokedexText,\n"
    text += f"\t\t.pokemonScale = {POKEMON_SCALE},\n"
    text += f"\t\t.pokemonOffset = {POKEMON_OFFSET},\n"
    text += f"\t\t.trainerScale = {TRAINER_SCALE},\n"
    text += f"\t\t.trainerOffset = {TRAINER_OFFSET},\n"

    text += "\t},\n\n"

    # Add to file
    trigger_line = "[NATIONAL_DEX_DEOXYS] ="
    file_path = "pokeemerald/src/data/pokemon/pokedex_entries.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")

def add_to_pokedex_order_1():
    # Generate text
    text = f"\tNATIONAL_DEX_{UPPER_NAME},\n"

    # Add to file
    trigger_line = "NATIONAL_DEX_ZUBAT,};"
    file_path = "pokeemerald/src/data/pokemon/pokedex_orders.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def add_to_pokedex_order_2():
    # Generate text
    text = f"\tNATIONAL_DEX_{UPPER_NAME},\n"

    # Add to file
    trigger_line = "NATIONAL_DEX_GROUDON,};"
    file_path = "pokeemerald/src/data/pokemon/pokedex_orders.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")



def add_to_pokedex_order_3():
    # Generate text
    text = f"\tNATIONAL_DEX_{UPPER_NAME},\n"

    # Add to file
    trigger_line = "NATIONAL_DEX_WAILORD,};"
    file_path = "pokeemerald/src/data/pokemon/pokedex_orders.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def define_species_info():
    # Generate text
    text = f"\t,[SPECIES_{UPPER_NAME}] = \n"
    text += "\t{\n"

    text += f"\t\t.baseHP\t= {SPECIES_INFO['base_hp']},\n"
    text += f"\t\t.baseAttack\t= {SPECIES_INFO['base_hp']},\n"
    text += f"\t\t.baseDefense\t= {SPECIES_INFO['base_hp']},\n"
    text += f"\t\t.baseSpeed\t= {SPECIES_INFO['base_hp']},\n"
    text += f"\t\t.baseSpAttack\t= {SPECIES_INFO['base_hp']},\n"
    text += f"\t\t.baseSpDefense\t= {SPECIES_INFO['base_hp']},\n"
    text += "\t\t.types = {" + SPECIES_INFO["type_1"] + ", " + SPECIES_INFO["type_2"] + "},\n"
    text += f"\t\t.catchRate\t= {SPECIES_INFO['catch_rate']},\n"
    text += f"\t\t.expYield\t= {SPECIES_INFO['exp_yield']},\n"
    text += f"\t\t.evYield_HP\t= {SPECIES_INFO['ev_yield_hp']},\n"
    text += f"\t\t.evYield_Attack\t= {SPECIES_INFO['ev_yield_attack']},\n"
    text += f"\t\t.evYield_Defense\t= {SPECIES_INFO['ev_yield_defense']},\n"
    text += f"\t\t.evYield_Speed\t= {SPECIES_INFO['ev_yield_speed']},\n"
    text += f"\t\t.evYield_SpAttack\t= {SPECIES_INFO['ev_yield_sp_attack']},\n"
    text += f"\t\t.evYield_SpDefense\t= {SPECIES_INFO['ev_yield_sp_defense']},\n"
    text += f"\t\t.itemCommon = {SPECIES_INFO['item_common']},\n"
    text += f"\t\t.itemRare = {SPECIES_INFO['item_rare']},\n"
    text += f"\t\t.genderRatio = {SPECIES_INFO['gender_ratio']},\n"
    text += f"\t\t.eggCycles = {SPECIES_INFO['egg_cycles']},\n"
    text += f"\t\t.friendship = {SPECIES_INFO['friendship']},\n"
    text += f"\t\t.growthRate = {SPECIES_INFO['growth_rate']},\n"
    text += "\t\t.eggGroups = {" + SPECIES_INFO["egg_group_1"] + ", " + SPECIES_INFO["egg_group_2"] + "},\n"
    text += "\t\t.abilities = {" + SPECIES_INFO["ability_1"] + ", " + SPECIES_INFO["ability_2"] + "},\n"
    text += f"\t\t.safariZoneFleeRate = {SPECIES_INFO['safari_zone_flee_rate']},\n"
    text += f"\t\t.bodyColor = {SPECIES_INFO['body_color']},\n"
    text += f"\t\t.noFlip = {SPECIES_INFO['no_flip']}\n"

    text += "\t}\n"

    # Add to file
    trigger_line = "};"
    file_path = "pokeemerald/src/data/pokemon/species_info.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_moveset():
    # Generate text
    text = f"\n\nstatic const u16 s{NAME}LevelUpLearnset[] = " + "{\n"
    for lvl, name in LEARNED_MOVES:
        text += f"\tLEVEL_UP_MOVE({lvl}, {name}),\n"
    text += "\tLEVEL_UP_END\n};"

    # Add to file
    file_path = "pokeemerald/src/data/pokemon/level_up_learnsets.h"

    default_add_text_end_of_file(file_path, text)
    print("Done.")


def register_moveset_pointer():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}] = s{NAME}LevelUpLearnset,\n"

    # Add to file
    trigger_line = "[SPECIES_CHIMECHO] = sChimechoLevelUpLearnset,"
    file_path = "pokeemerald/src/data/pokemon/level_up_learnset_pointers.h"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")


def register_tmhms():
    # Generate text
    text = "\t[SPECIES_" + UPPER_NAME + "] = { .learnset = {\n"
    for tmhm in ALLOWED_TMS_AND_HMS:
        text += f"\t\t.{tmhm} = TRUE,\n"
    text += "\t}},\n"

    # Add to file
    trigger_line = "[SPECIES_CHIMECHO] = { .learnset = {"
    file_path = "pokeemerald/src/data/pokemon/tmhm_learnsets.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def add_empty_tutor_moves():
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}]         = (0),\n"
        
    # Add to file
    trigger_line = "[SPECIES_CHIMECHO]"
    file_path = "pokeemerald/src/data/pokemon/tutor_learnsets.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def add_cry_data():
    # Generate text
    text = "\n\t.align 2\n"
    text += f"Cry_{NAME}::\n"
    text += f'\t.incbin "sound/direct_sound_samples/cries/{LOWER_NAME}.bin"\n'
        
    # Add to file
    trigger_line = '.incbin "sound/direct_sound_samples/cries/chimecho.bin"'
    file_path = "pokeemerald/sound/direct_sound_data.inc"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")


def add_cry_table():
    # Generate text
    text = f"\tcry Cry_{NAME}\n"
        
    # Add to file
    trigger_line = "cry Cry_Chimecho"
    file_path = "pokeemerald/sound/cry_tables.inc"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")


def add_cry_table_2():
    # Generate text
    text = f"\tcry_reverse Cry_{NAME}\n"
        
    # Add to file
    trigger_line = "cry_reverse Cry_Chimecho"
    file_path = "pokeemerald/sound/cry_tables.inc"

    default_add_text_after_trigger(trigger_line, file_path, text)
    print("Done.")

	
def add_cry_id():
    new_num = -1
    with open("pokeemerald/src/data/pokemon/cry_ids.h", "r") as read_handle:
        lines = []
        for i, line in enumerate(read_handle.readlines()):
            lines.append(line)
            
            if "};" in line:
                last_mon_line = lines[i - 1]
                last_mon_line = last_mon_line.replace(",", "")

                old_num = int(last_mon_line[len(last_mon_line) - 4:])
                new_num = old_num + 1

    text = f"\t[SPECIES_{UPPER_NAME} - 277] = {new_num},\n"

    trigger_line = "};"
    file_path = "pokeemerald/src/data/pokemon/cry_ids.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def add_evolution():
    # Generate text
    text = "\t[SPECIES_" + UPPER_NAME + "]     = {{" + EVOLUTION[0] + ", " + str(EVOLUTION[1]) + ", " + EVOLUTION[2] + "}},\n"

    # Add to file
    trigger_line = "};"
    file_path = "pokeemerald/src/data/pokemon/evolution.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def warn_left_todos():
    print("After executing all functions, there are a few small manual tasks left to do")
    print("1) add the files. (sprites and cries)")
    print("2) sort the pokedex based on height, weight, and alphabetic order")
    print("3) add the pokemon to easychat")
    print("4) manually add tutor and egg moves (will make this automatic maybe)")

    print(f"And then you are done! Add the mon via porymap, and good luck with {NAME}!")

register_sprite_1()
register_sprite_2()
register_sprite_3()
register_sprite_4()
register_sprite_5()
register_sprite_6()
update_tables_1()
update_tables_2()
update_tables_3()
update_tables_4()
update_tables_5()
update_tables_6()
update_tables_7()
update_tables_8()
update_tables_9()
update_tables_10()
add_species_constant()
register_species_name()
register_species_dex_entry_1()
register_species_dex_entry_2()
register_species_dex_entry_3()
register_species_dex_entry_4()
register_species_to_pokedex_1()
register_species_to_pokedex_2()
register_species_to_pokedex_3()
add_pokedex_text()
add_pokedex_entry()
add_to_pokedex_order_1()
add_to_pokedex_order_2()
add_to_pokedex_order_3()
define_species_info()
register_moveset()
register_moveset_pointer()
register_tmhms()
add_empty_tutor_moves()
add_cry_data()
add_cry_table()
add_cry_table_2()
add_cry_id()
add_evolution()
warn_left_todos()


#TODO: Fix problem where an apostroph in dex_text is unown (Toxel's)