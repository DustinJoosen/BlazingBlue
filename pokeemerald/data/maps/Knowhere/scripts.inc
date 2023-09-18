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


Knowhere_EventScript_Technology_Text_0:
	.string "Technology is amazing!$"

Knowhere_EventScript_LoveYou_Text_0:
	.string "Ik ga naar bed. Love you!$"

Knowhere_Sign_RivalHouse_Text_0:
	.string "Dylan's House$"

Knowhere_Sign_PlayerHouse_Text_0:
	.string "Your House$"

Knowhere_Sign_CherrysLab_Text_0:
	.string "Professor Cherry's lab$"
