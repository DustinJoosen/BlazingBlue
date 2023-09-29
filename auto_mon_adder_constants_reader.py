
class ConstantsReader:

    def __init__(self, fp):
        self.file_lines = []

        with open(fp, "r") as read_handle:
            for line in read_handle.readlines():
                self.file_lines.append(line)


    def get(self, key: str, return_type: type = str):
        if key is None:
            return None
        
        return_value: str = ""

        for line in self.file_lines:
            if line is None or line == "\n":
                continue

            if key in line:
                return_value = line

                # Filter out everything, to get the actual value
                return_value = return_value.replace(key, "")
                return_value = return_value.replace(" ", "")
                return_value = return_value.replace("=", "")
                return_value = return_value.replace("\"", "")
                return_value = return_value.replace("\n", "")


        return return_type(return_value)


    # Multiline, so can't be used with .get(key)
    def get_pokedex_text(self):
        for i, line in enumerate(self.file_lines):
            if line is None or line == "\n":
                continue

            if "POKEDEX_TEXT" in line:
                lines = [self.file_lines[i + n].replace("\n", "").strip(" ") for n in range(1, 5)]
                return lines

        return "===POKEDEX_ENTRY_NOT_FOUND==="
    

    def get_learned_moves(self):
        learned_moves = []

        for i, line in enumerate(self.file_lines):
            if line is None or line == "\n":
                continue

            # Found the learned moves
            if "LEARNED_MOVES" in line:
                
                not_ended = True
                j = 1

                # Continue adding moves until not_ended false.
                while not_ended:

                    # Stop when the } is found
                    if "}" in self.file_lines[i + j]:
                        not_ended = False
                        continue

                    # Find the move and equal sign idx
                    move = self.file_lines[i + j].replace("\n", "").strip(" ")
                    equal_idx = move.find("=")
                    
                    # Add it to the return value
                    learned_moves.append([
                        int(move[0:equal_idx]),         # 1
                        str(move[equal_idx + 2: -1])    # LIGHT_SCREEN
                    ])

                    j += 1

        return learned_moves
    

    def get_allowed_tms_and_hms(self):
        allowed_moves = []

        for i, line in enumerate(self.file_lines):
            if line is None or line == "\n":
                continue

            # Found the allowed moves
            if "ALLOWED_TMS_AND_HMS" in line:
                
                not_ended = True
                j = 1

                # Continue adding moves until not_ended false.
                while not_ended:

                    # Stop when the } is found
                    if "}" in self.file_lines[i + j]:
                        not_ended = False
                        continue

                    # Find the move and add to the return value
                    move = self.file_lines[i + j].replace("\n", "").replace("\"", "").strip(" ")
                    allowed_moves.append(move)

                    j += 1

        return allowed_moves
