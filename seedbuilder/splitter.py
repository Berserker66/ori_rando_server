import random
dungeon_keys = ["RB|17", "RB|19", "RB|21", "EV|0", "EV|2", "EV|4"] # WV, GS, SS
skills = ["SK|3", "SK|2", "SK|50", "SK|4", "SK|5", "SK|14", "SK|0", "SK|12", "SK|51", "SK|8"] # WJ, CFlame, Dash, Stomp, DJ, Glide, Bash, Climb, Grenade, CJ
events = ["EV|1", "EV|3", "EV|5"] # Water, Wind, Warmth C:
bonuses = ["RB|8","RB|9","RB|10", "RB|11", "RB|12", "RB|6", "RB|13", "RB|15", "RB|30", "RB|31", "RB|32", "RB|33", "RB|101", "RB|102", "RB|103", "RB|104"]
teleporters = ["TP|Forlorn", "TP|Swamp", "TP|Valley", "TP|Grove", "TP|Grotto", "TP|Sorrow"]	
hint_text = {"SK": "Skill", "TP": "Teleporter", "RB": "Upgrade", "EV": "Event"}
def split_seed(seed, gameId, player, max_players, hints=False, dk=True, sk=True, ev=True, rb=True, tp=True):
	pickups = (dungeon_keys if dk else []) + (skills if sk else []) + (events if ev else []) + (bonuses if rb else []) + (teleporters if tp else [])
	random.seed(gameId+max_players)
	outlines = []
	for line in seed.split("\n"):
		if any(i in line for i in pickups):
			if player == random.randint(1, max_players):
				outlines.append(line)
			else:
				outln = line.split("|")
				if hints:
					if (outln[1] == "RB" and outln[2] in ["17", "19", "21"]) or (outln[1] == "EV" and outln[2] in ["0", "2", "4"]):
						outln[2] = "@Dungeon Key@"
					else:
						outln[2] = "@%s@" % hint_text[outln[1]]
					outln[1] = "SH"
				else:
					outln[1] = "EV"
					outln[2] = "5"
				outlines.append("|".join(outln))
		else:
			outlines.append(line)
	#outlines[0] = "Sync%s.%s," %(gameId,player) + outlines[0]
	return "\n".join(outlines)