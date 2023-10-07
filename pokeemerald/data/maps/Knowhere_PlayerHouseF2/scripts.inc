Knowhere_PlayerHouseF2_MapScripts::
	.byte 0


Knowhere_PlayerHouseF2_EventScript_WallClock::
	lockall
	goto_if_set FLAG_SET_WALL_CLOCK, Knowhere_PlayerHouseF2_EventScript_WallClock_2
	msgbox ClockIsStopped
	call SetWallClock
	delay 30
	setflag FLAG_SET_WALL_CLOCK
	releaseall
	return

Knowhere_PlayerHouseF2_EventScript_WallClock_2:
	releaseall
	return


SetWallClock::
	fadescreen FADE_TO_BLACK
	special StartWallClock
	waitstate
	return


ClockIsStopped::
	.string "The clock is stopped...\p"
	.string "Better set it!$"
