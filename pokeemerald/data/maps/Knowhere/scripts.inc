Knowhere_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Knowhere_Set_Cherry_Invisible
	.byte 0


Knowhere_Set_Cherry_Invisible::
	setflag FLAG_UNUSED_0x493
	return


Knowhere_EventScript_Technology::
	lockall
	faceplayer
	msgbox Knowhere_EventScript_Technology_Text_0
	releaseall
	return


Knowhere_EventScript_LoveYou::
	lockall
	faceplayer
	msgbox Knowhere_EventScript_LoveYou_Text_0
	releaseall
	return


Knowhere_EventScript_FirstFight::
	lockall
	additem 264, 1
	setflag FLAG_RECEIVED_SUPER_ROD
	additem 339, 1
	setflag FLAG_RECEIVED_HM_CUT
	msgbox Knowhere_EventScript_FirstFight_Text_0, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq Knowhere_EventScript_FirstFight_2
	msgbox Knowhere_EventScript_FirstFight_Text_3
Knowhere_EventScript_FirstFight_1:
	releaseall
	return

Knowhere_EventScript_FirstFight_2:
	trainerbattle_single TRAINER_JADZIA, Knowhere_EventScript_FirstFight_Text_1, Knowhere_EventScript_FirstFight_Text_2
	setflag FLAG_UNUSED_0x93C
	goto Knowhere_EventScript_FirstFight_1


Knowhere_EventScript_Roadblock::
	lockall
	msgbox Knowhere_EventScript_Roadblock_Text_0
	applymovement OBJ_EVENT_ID_PLAYER, Movement_MovePlayerLeft
	waitmovement 0
	releaseall
	return


Knowhere_EventScript_PreventFishingWithoutMon::
	lockall
	msgbox Knowhere_EventScript_Roadblock_Text_0
	applymovement OBJ_EVENT_ID_PLAYER, Movement_MovePlayerAwayFromPond
	waitmovement 0
	releaseall
	return


Knowhere_EventScript_GiveRunningShoes::
	lockall
	faceplayer
	goto_if_unset FLAG_RECEIVED_RUNNING_SHOES, Knowhere_EventScript_GiveRunningShoes_2
	msgbox Knowhere_EventScript_GiveRunningShoes_Text_2
Knowhere_EventScript_GiveRunningShoes_1:
	releaseall
	return

Knowhere_EventScript_GiveRunningShoes_2:
	msgbox Text_MomGivesRunningShoes
	playfanfare MUS_OBTAIN_ITEM
	msgbox Knowhere_EventScript_GiveRunningShoes_Text_0
	waitfanfare
	setflag FLAG_RECEIVED_RUNNING_SHOES
	setflag FLAG_SYS_B_DASH
	msgbox Text_RunningShoesExplanation
	msgbox Knowhere_EventScript_GiveRunningShoes_Text_1
	closemessage
	goto Knowhere_EventScript_GiveRunningShoes_1


Knowhere_EventScript_WaitPlayerPokedex_Top::
	lockall
	clearflag FLAG_UNUSED_0x493
	addobject 8
	applymovement 8, Movement_CherryMovesToTownExit_Top
	applymovement OBJ_EVENT_ID_PLAYER, Movement_PlayerLookLeft
	msgbox Knowhere_EventScript_WaitPlayerPokedex_Top_Text_0
	waitmovement 8
	call Knowhere_EventScript_GivePokdex
	releaseall
	return


Knowhere_EventScript_WaitPlayerPokedex_Bottom::
	lockall
	clearflag FLAG_UNUSED_0x493
	addobject 8
	applymovement 8, Movement_CherryMovesToTownExit_Bottom
	applymovement OBJ_EVENT_ID_PLAYER, Movement_PlayerLookLeft
	msgbox Knowhere_EventScript_WaitPlayerPokedex_Top_Text_0
	waitmovement 8
	call Knowhere_EventScript_GivePokdex
	releaseall
	return


Knowhere_EventScript_GivePokdex::
	setvar VAR_UNUSED_0x40F7, 2
	msgbox Text_GivePokedex
	playfanfare MUS_OBTAIN_ITEM
	msgbox Knowhere_EventScript_GivePokdex_Text_0
	waitfanfare
	setflag FLAG_SYS_POKEDEX_GET
	special SetUnlockedPokedexFlags
	setflag FLAG_RECEIVED_POKEDEX_FROM_BIRCH
	msgbox Knowhere_EventScript_GivePokdex_Text_1
	call Knowhere_EventScript_MoveCherryAwayAgain
	return


Knowhere_EventScript_MoveCherryAwayAgain::
	applymovement 8, Movement_CherryReturnsToHerLab
	waitmovement 8
	applymovement OBJ_EVENT_ID_PLAYER, Movement_PlayerLookRight
	removeobject 8
	return


Knowhere_Sign_RivalHouse::
	lockall
	msgbox Knowhere_Sign_RivalHouse_Text_0
	releaseall
	return


Knowhere_Sign_PlayerHouse::
	lockall
	msgbox Knowhere_Sign_PlayerHouse_Text_0
	releaseall
	return


Knowhere_Sign_CherrysLab::
	lockall
	msgbox Knowhere_Sign_CherrysLab_Text_0
	releaseall
	return


Knowhere_EventScript_Item_UltraBall::
	finditem ITEM_ULTRA_BALL
	return


Movement_MovePlayerLeft:
	face_left
	walk_left
	walk_left
	face_right
	step_end

Movement_MovePlayerAwayFromPond:
	face_right
	walk_right
	walk_right
	face_left
	step_end

Movement_CherryMovesToTownExit_Top:
	face_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	face_right
	walk_right
	walk_right
	step_end

Movement_CherryMovesToTownExit_Bottom:
	face_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	face_right
	walk_right
	walk_right
	step_end

Movement_CherryReturnsToHerLab:
	face_left
	walk_left
	walk_left
	face_down
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	face_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	step_end

Movement_PlayerLookLeft:
	face_left
	step_end

Movement_PlayerLookRight:
	face_right
	step_end

Knowhere_EventScript_Technology_Text_0:
	.string "Technology is amazing!$"

Knowhere_EventScript_LoveYou_Text_0:
	.string "Ik ga naar bed. Love you lots!$"

Knowhere_EventScript_FirstFight_Text_0:
	.string "You want to fight?$"

Knowhere_EventScript_FirstFight_Text_1:
	.string "Hell yeah! Let's go$"

Knowhere_EventScript_FirstFight_Text_2:
	.string "Here's a kiss, as reward$"

Knowhere_EventScript_FirstFight_Text_3:
	.string "Prude.$"

Knowhere_EventScript_Roadblock_Text_0:
	.string "You remember Professor Cherry said she\nwanted to see you at her lab yesterday$"

Knowhere_EventScript_GiveRunningShoes_Text_0:
	.string "{PLAYER} switches shoes with the\nRUNNING SHOES.$"

Knowhere_EventScript_GiveRunningShoes_Text_1:
	.string "Enjoy your new shoes!$"

Knowhere_EventScript_GiveRunningShoes_Text_2:
	.string "How is your journey going honey?$"

Knowhere_EventScript_WaitPlayerPokedex_Top_Text_0:
	.string "Wait {PLAYER}!$"

Knowhere_EventScript_GivePokdex_Text_0:
	.string "{PLAYER} recieved the Pokedex$"

Knowhere_EventScript_GivePokdex_Text_1:
	.string "Now go on out, and explore\nthe REGIONNAME Region!$"

Knowhere_Sign_RivalHouse_Text_0:
	.string "Dylan's House$"

Knowhere_Sign_PlayerHouse_Text_0:
	.string "{PLAYER} House$"

Knowhere_Sign_CherrysLab_Text_0:
	.string "Professor Cherry's lab$"

Text_RunningShoesExplanation::
	.string "I heard that if you press the B Button\n"
	.string "while wearing these RUNNING SHOES you\p"
	.string "run extra-fast!$"

Text_MomGivesRunningShoes::
	.string "Hi honey!\p"
	.string "I just got an extra pair of running\n"
	.string "shoes from the mailman.\p"
	.string "You can have one of them$"

Text_GivePokedex::
	.string "I forgot to give you this pokedex!\p"
	.string "This pokedex will allow you to\n"
	.string "Record data about the pokemon that\p"
	.string "you will come across on your journey!$"
