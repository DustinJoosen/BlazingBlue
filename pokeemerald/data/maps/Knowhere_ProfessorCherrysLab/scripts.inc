Knowhere_ProfessorCherrysLab_MapScripts::
	.byte 0


Knowhere_ProfessorCherrysLab_EventScript_Professor::
	lockall
	faceplayer
	goto_if_set FLAG_SYS_POKEMON_GET, Knowhere_ProfessorCherrysLab_EventScript_Professor_2
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Professor_Text_1
Knowhere_ProfessorCherrysLab_EventScript_Professor_1:
	releaseall
	return

Knowhere_ProfessorCherrysLab_EventScript_Professor_2:
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Professor_Text_0
	goto Knowhere_ProfessorCherrysLab_EventScript_Professor_1


Knowhere_ProfessorCherrysLab_EventScript_AhPlayer::
	lockall
	goto_if_set FLAG_UNUSED_0x264, Knowhere_ProfessorCherrysLab_EventScript_AhPlayer_2
	msgbox Knowhere_ProfessorCherrysLab_EventScript_AhPlayer_Text_0
	applymovement 1, Knowhere_ProfessorCherrysLab_CherryMovesToEntry
	waitmovement 0
	msgbox Knowhere_ProfessorCherrysLab_EventScript_AhPlayer_Text_1
	applymovement 1, Knowhere_ProfessorCherrysLab_CherryMovesUp
	applymovement OBJ_EVENT_ID_PLAYER, Knowhere_ProfessorCherrysLab_PlayerMovesUp
	waitmovement 1
	waitmovement OBJ_EVENT_ID_PLAYER
	setflag FLAG_UNUSED_0x264
	msgbox Knowhere_ProfessorCherrysLab_ChoosePokemon
	releaseall
	return

Knowhere_ProfessorCherrysLab_EventScript_AhPlayer_2:
	return


Knowhere_ProfessorCherrysLab_EventScript_Pokeball::
	lockall
	showmonpic SPECIES_BODILAD, 10, 3
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_0, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq Knowhere_ProfessorCherrysLab_EventScript_Pokeball_2
	hidemonpic
	msgbox Knowhere_ProfessorCherrysLab_NotChosen
Knowhere_ProfessorCherrysLab_EventScript_Pokeball_1:
	waitmessage
	releaseall
	end

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_2:
	givemon SPECIES_BODILAD, 50, ITEM_MASTER_BALL
	setflag FLAG_SYS_POKEMON_GET
	setflag FLAG_SYS_POKEDEX_GET
	setflag FLAG_RECEIVED_POKEDEX_FROM_BIRCH
	special SetUnlockedPokedexFlags
	compare VAR_RESULT, MON_GIVEN_TO_PARTY
	goto_if_eq Knowhere_ProfessorCherrysLab_EventScript_Pokeball_5
	compare VAR_RESULT, MON_GIVEN_TO_PC
	goto_if_eq Knowhere_ProfessorCherrysLab_EventScript_Pokeball_6
	hidemonpic
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_2
	goto Knowhere_ProfessorCherrysLab_EventScript_Pokeball_1

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_5:
	playfanfare MUS_OBTAIN_ITEM
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_1
	removeobject 2
	setflag FLAG_UNUSED_0x020
	call Knowhere_NicknamePartyMon
	goto Knowhere_ProfessorCherrysLab_EventScript_Pokeball_1

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_6:
	playfanfare MUS_OBTAIN_ITEM
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_1
	removeobject 2
	setflag FLAG_UNUSED_0x020
	call Knowhere_NicknameBoxMon
	goto Knowhere_ProfessorCherrysLab_EventScript_Pokeball_1


Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett::
	lockall
	showmonpic SPECIES_DRIPLETT, 10, 3
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_Text_0, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_2
	hidemonpic
	msgbox Knowhere_ProfessorCherrysLab_NotChosen
Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_1:
	waitmessage
	releaseall
	end

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_2:
	givemon SPECIES_DRIPLETT, 5
	setflag FLAG_SYS_POKEMON_GET
	setflag FLAG_SYS_POKEDEX_GET
	setflag FLAG_RECEIVED_POKEDEX_FROM_BIRCH
	special SetUnlockedPokedexFlags
	compare VAR_RESULT, MON_GIVEN_TO_PARTY
	goto_if_eq Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_5
	compare VAR_RESULT, MON_GIVEN_TO_PC
	goto_if_eq Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_6
	hidemonpic
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_2
	goto Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_1

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_5:
	playfanfare MUS_OBTAIN_ITEM
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_Text_1
	removeobject 2
	setflag FLAG_UNUSED_0x020
	call Knowhere_NicknamePartyMon
	goto Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_1

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_6:
	playfanfare MUS_OBTAIN_ITEM
	msgbox Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_Text_1
	removeobject 2
	setflag FLAG_UNUSED_0x020
	call Knowhere_NicknameBoxMon
	goto Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_1


Knowhere_NicknamePartyMon::
	msgbox Knowhere_NicknamePartyMon_Text_0, MSGBOX_YESNO
	hidemonpic
	compare VAR_RESULT, YES
	goto_if_eq Knowhere_NicknamePartyMon_1
	return

Knowhere_NicknamePartyMon_1:
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	return


Knowhere_NicknameBoxMon::
	msgbox Knowhere_NicknamePartyMon_Text_0, MSGBOX_YESNO
	hidemonpic
	compare VAR_RESULT, YES
	goto_if_eq Knowhere_NicknameBoxMon_2
Knowhere_NicknameBoxMon_1:
	msgbox Knowhere_NicknameBoxMon_Text_0
	return

Knowhere_NicknameBoxMon_2:
	call Common_EventScript_NameReceivedBoxMon
	goto Knowhere_NicknameBoxMon_1


Knowhere_ProfessorCherrysLab_CherryMovesToEntry:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	face_left
	walk_left
	step_end

Knowhere_ProfessorCherrysLab_CherryMovesUp:
	face_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	face_left
	step_end

Knowhere_ProfessorCherrysLab_PlayerMovesUp:
	face_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	step_end

Knowhere_ProfessorCherrysLab_EventScript_Professor_Text_0:
	.string "Enjoy your new pokemon$"

Knowhere_ProfessorCherrysLab_EventScript_Professor_Text_1:
	.string "Go ahead and grab this Pokemon$"

Knowhere_ProfessorCherrysLab_EventScript_AhPlayer_Text_0:
	.string "Ah {PLAYER}!$"

Knowhere_ProfessorCherrysLab_EventScript_AhPlayer_Text_1:
	.string "I was waiting for you.\nCome with me$"

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_0:
	.string "Do you want to choose Bodilad?$"

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_1:
	.string "Recieved Bodilad$"

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Text_2:
	.string "No more room$"

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_Text_0:
	.string "Do you want to choose Driplett?$"

Knowhere_ProfessorCherrysLab_EventScript_Pokeball_Driplett_Text_1:
	.string "Recieved Driplett$"

Knowhere_NicknamePartyMon_Text_0:
	.string "Give it a nickname?$"

Knowhere_NicknameBoxMon_Text_0:
	.string "Transferred to PC$"

Knowhere_ProfessorCherrysLab_NotChosen::
	.string "You did not choose the pokemon$"

Knowhere_ProfessorCherrysLab_ChoosePokemon::
	.string "I wanted to give you a pokemon.\p"
	.string "This will allow you to travel\n"
	.string "outside of knowhere$"