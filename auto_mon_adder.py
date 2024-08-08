import auto_mon_adder_constants_reader
import tkinter as tk
from tkinter import filedialog

# Get the file name
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

# Define the constants-reader
constants_reader = auto_mon_adder_constants_reader.ConstantsReader(file_path)

# Define a few constants
NAME = constants_reader.get("POKEMON_NAME")
LOWER_NAME = NAME.lower()
UPPER_NAME = NAME.upper()

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
    for line in constants_reader.get_pokedex_text():
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

    text += f"\t\t.categoryName = _(\"{constants_reader.get('CATEGORY_NAME')}\"),\n"
    text += f"\t\t.height = {constants_reader.get('HEIGHT')},\n"
    text += f"\t\t.weight = {constants_reader.get('WEIGHT')},\n"
    text += f"\t\t.description = g{NAME}PokedexText,\n"
    text += f"\t\t.pokemonScale = {constants_reader.get('POKEMON_SCALE')},\n"
    text += "\t\t.pokemonOffset = 0,\n"
    text += f"\t\t.trainerScale = {constants_reader.get('POKEMON_SCALE')},\n"
    text += "\t\t.trainerOffset = 2,\n"

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

    text += f"\t\t.baseHP\t= {constants_reader.get('BASE_HP')},\n"
    text += f"\t\t.baseAttack\t= {constants_reader.get('BASE_ATTACK')},\n"
    text += f"\t\t.baseDefense\t= {constants_reader.get('BASE_DEFENSE')},\n"
    text += f"\t\t.baseSpeed\t= {constants_reader.get('BASE_SPEED')},\n"
    text += f"\t\t.baseSpAttack\t= {constants_reader.get('BASE_SP_ATTACK')},\n"
    text += f"\t\t.baseSpDefense\t= {constants_reader.get('BASE_SP_DEFENSE')},\n"
    text += "\t\t.types = { TYPE_" + constants_reader.get('TYPE_1') + ", TYPE_" + constants_reader.get('TYPE_2') + "},\n"
    text += f"\t\t.catchRate\t= {constants_reader.get('CATCH_RATE')},\n"
    text += f"\t\t.expYield\t= {constants_reader.get('EXP_YIELD')},\n"
    text += f"\t\t.evYield_HP\t= {constants_reader.get('EV_YIELD_HP')},\n"
    text += f"\t\t.evYield_Attack\t= {constants_reader.get('EV_YIELD_ATTACK')},\n"
    text += f"\t\t.evYield_Defense\t= {constants_reader.get('EV_YIELD_DEFENSE')},\n"
    text += f"\t\t.evYield_Speed\t= {constants_reader.get('EV_YIELD_SPEED')},\n"
    text += f"\t\t.evYield_SpAttack\t= {constants_reader.get('EV_YIELD_SP_ATTACK')},\n"
    text += f"\t\t.evYield_SpDefense\t= {constants_reader.get('EV_YIELD_SP_DEFENSE')},\n"
    text += f"\t\t.itemCommon = ITEM_NONE,\n"
    text += f"\t\t.itemRare = ITEM_NONE,\n"
    text += f"\t\t.genderRatio = {constants_reader.get('GENDER_RATIO')},\n"
    text += f"\t\t.eggCycles = {constants_reader.get('EGG_CYCLES')},\n"
    text += f"\t\t.friendship = {constants_reader.get('FRIENDSHIP')},\n"
    text += f"\t\t.growthRate = {constants_reader.get('GROWTH_RATE')},\n"
    text += "\t\t.eggGroups = {" + constants_reader.get('EGG_GROUP_1') + ", " + constants_reader.get('EGG_GROUP_2') + "},\n"
    text += "\t\t.abilities = {ABILITY_" + constants_reader.get('ABILITY_1') + ", ABILITY_" + constants_reader.get('ABILITY_2') + "},\n"
    text += f"\t\t.safariZoneFleeRate = 0,\n"
    text += f"\t\t.bodyColor = BODY_COLOR_{constants_reader.get('BODY_COLOR')},\n"
    text += f"\t\t.noFlip = FALSE\n"

    text += "\t}\n"

    # Add to file
    trigger_line = "};"
    file_path = "pokeemerald/src/data/pokemon/species_info.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def register_moveset():
    # Generate text
    text = f"\n\nstatic const u16 s{NAME}LevelUpLearnset[] = " + "{\n"
    for lvl, name in constants_reader.get_learned_moves():
        text += f"\tLEVEL_UP_MOVE({lvl}, MOVE_{name}),\n"
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
    for tmhm in constants_reader.get_allowed_tms_and_hms():
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
    if not constants_reader.get("HAS_EVOLUTION") == "True":
        print("evolution not defined")
        return
    
    # Generate text
    text = f"\t[SPECIES_{UPPER_NAME}] = " + "{{" + f"{constants_reader.get('EVOLUTION_METHOD')}, {constants_reader.get('EVOLUTION_CRITERIA')}, {constants_reader.get('EVOLUTION_SPECIES')}" + "}},\n"

    # Add to file
    trigger_line = "};"
    file_path = "pokeemerald/src/data/pokemon/evolution.h"

    default_add_text_before_trigger(trigger_line, file_path, text)
    print("Done.")


def warn_left_todos():
    print("After executing all functions, there are a few small manual tasks left to do")
    print("1) add the files. (sprites and cries)")
    print("2) Fix the cry order. New at the bottom")
    print("3) sort the pokedex based on height, weight, and alphabetic order")
    print("4) add the pokemon to easychat")
    print("5) manually add tutor and egg moves (will make this automatic maybe)")

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
