Knowhere_MapScripts::
	.byte 0


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
	goto_if_set FLAG_SYS_POKEMON_GET, Knowhere_EventScript_Roadblock_2
	msgbox Knowhere_EventScript_Roadblock_Text_0
	applymovement OBJ_EVENT_ID_PLAYER, Movement_MovePlayerLeft
	waitmovement 0
	releaseall
	return

Knowhere_EventScript_Roadblock_2:
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


Movement_MovePlayerLeft:
	face_left
	walk_left
	walk_left
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
