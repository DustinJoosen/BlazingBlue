LittlerootTown_ProfessorCherrysLab_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, LittlerootTown_ProfessorCherrysLab_EventScript_BallDefault
	.byte 0


LittlerootTown_ProfessorCherrysLab_EventScript_BallDefault::
	setvar VAR_UNUSED_0x40F7, 0
	return


ProfessorCherrysLab_EventScript_Professor::
	lockall
	faceplayer
	msgbox ProfessorCherrysLab_EventScript_Professor_Text_0, MSGBOX_YESNO
	releaseall
	return


ProfessorCherrysLab_EventScript_Pokeball::
	lockall
	msgbox ProfessorCherrysLab_EventScript_Pokeball_Text_0, MSGBOX_YESNO
	showmonpic SPECIES_BODILAD, 10, 3
	compare VAR_RESULT, YES
	goto_if_eq ProfessorCherrysLab_EventScript_Pokeball_2
	hidemonpic
	msgbox ProfessorCherrysLab_NotChosen
ProfessorCherrysLab_EventScript_Pokeball_1:
	waitmessage
	releaseall
	end

ProfessorCherrysLab_EventScript_Pokeball_2:
	givemon SPECIES_BODILAD, 50, ITEM_MASTER_BALL
	compare VAR_RESULT, MON_GIVEN_TO_PARTY
	goto_if_eq ProfessorCherrysLab_EventScript_Pokeball_5
	compare VAR_RESULT, MON_GIVEN_TO_PC
	goto_if_eq ProfessorCherrysLab_EventScript_Pokeball_6
	hidemonpic
	msgbox ProfessorCherrysLab_EventScript_Pokeball_Text_2
	goto ProfessorCherrysLab_EventScript_Pokeball_1

ProfessorCherrysLab_EventScript_Pokeball_5:
	playfanfare MUS_OBTAIN_ITEM
	msgbox ProfessorCherrysLab_EventScript_Pokeball_Text_1
	removeobject 1
	setflag FLAG_UNUSED_0x020
	call NicknamePartyMon
	goto ProfessorCherrysLab_EventScript_Pokeball_1

ProfessorCherrysLab_EventScript_Pokeball_6:
	playfanfare MUS_OBTAIN_ITEM
	msgbox ProfessorCherrysLab_EventScript_Pokeball_Text_1
	removeobject 1
	setflag FLAG_UNUSED_0x020
	call NicknameBoxMon
	goto ProfessorCherrysLab_EventScript_Pokeball_1


NicknamePartyMon::
	msgbox NicknamePartyMon_Text_0, MSGBOX_YESNO
	hidemonpic
	compare VAR_RESULT, YES
	goto_if_eq NicknamePartyMon_1
	return

NicknamePartyMon_1:
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	return


NicknameBoxMon::
	msgbox NicknamePartyMon_Text_0, MSGBOX_YESNO
	hidemonpic
	compare VAR_RESULT, YES
	goto_if_eq NicknameBoxMon_2
NicknameBoxMon_1:
	msgbox NicknameBoxMon_Text_0
	return

NicknameBoxMon_2:
	call Common_EventScript_NameReceivedBoxMon
	goto NicknameBoxMon_1


ProfessorCherrysLab_EventScript_Professor_Text_0:
	.string "Do you wanna swap the starters?$"

ProfessorCherrysLab_EventScript_Pokeball_Text_0:
	.string "Do you want to choose Bodilad?$"

ProfessorCherrysLab_EventScript_Pokeball_Text_1:
	.string "Recieved Bodilad$"

ProfessorCherrysLab_EventScript_Pokeball_Text_2:
	.string "No more room$"

NicknamePartyMon_Text_0:
	.string "Give it a nickname?$"

NicknameBoxMon_Text_0:
	.string "Transferred to PC$"

ProfessorCherrysLab_NotChosen::
	.string "You did not choose the pokemon$"
