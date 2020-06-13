# write your code here

def howwin(inp, sign):
    return ((inp[0] == sign and inp[1] == sign and inp[2] == sign) or  # top row
            (inp[3] == sign and inp[4] == sign and inp[5] == sign) or  # middle row
            (inp[6] == sign and inp[7] == sign and inp[8] == sign) or  # last row
            (inp[0] == sign and inp[3] == sign and inp[6] == sign) or  # down left
            (inp[1] == sign and inp[4] == sign and inp[7] == sign) or  # down middle
            (inp[2] == sign and inp[5] == sign and inp[8] == sign) or  # down right
            (inp[0] == sign and inp[4] == sign and inp[8] == sign) or  # diagonal from left
            (inp[2] == sign and inp[4] == sign and inp[6] == sign))  # diagonal from right


cells = list("         ")

print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")
counter = 0
while counter < 9:
    X_list = [x for x in cells if x == "X"]
    O_list = [x for x in cells if x == "O"]
    cord = input("Enter the coordinates:")
    cord_list = cord.split()
    cord_join = "".join(cord_list)
    if not cord_join.isdigit():
        print("You should enter numbers!")
    elif cord_list[0] not in["1", "2", "3"] or cord_list[1] not in ["1", "2", "3"]:
        print("Coordinates should be from 1 to 3!")
    else:
        if cord_list[0] == "1" and cord_list[1] == "1":
            if cells[6] == "X" or cells[6] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[6] = "X"
                else:
                    cells[6] = "O"

        if cord_list[0] == "1" and cord_list[1] == "2":
            if cells[3] == "X" or cells[3] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[3] = "X"
                else:
                    cells[3] = "O"

        if cord_list[0] == "1" and cord_list[1] == "3":
            if cells[0] == "X" or cells[0] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[0] = "X"
                else:
                    cells[0] = "O"
        if cord_list[0] == "2" and cord_list[1] == "1":
            if cells[7] == "X" or cells[7] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[7] = "X"
                else:
                    cells[7] = "O"

        if cord_list[0] == "2" and cord_list[1] == "2":
            if cells[4] == "X" or cells[4] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[4] = "X"
                else:
                    cells[4] = "O"

        if cord_list[0] == "2" and cord_list[1] == "3":
            if cells[1] == "X" or cells[1] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[1] = "X"
                else:
                    cells[1] = "O"
        if cord_list[0] == "3" and cord_list[1] == "1":
            if cells[8] == "X" or cells[8] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[8] = "X"
                else:
                    cells[8] = "O"

        if cord_list[0] == "3" and cord_list[1] == "2":
            if cells[5] == "X" or cells[5] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[5] = "X"
                else:
                    cells[5] = "O"
        if cord_list[0] == "3" and cord_list[1] == "3":
            if cells[2] == "X" or cells[2] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                counter += 1
                if len(X_list) - len(O_list) == 0:
                    cells[2] = "X"
                else:
                    cells[2] = "O"

    print(f"""
---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------""")
    if howwin(cells, "X"):
        print("X wins")
        break

    elif howwin(cells, "O"):
        print("O wins")
        break
    else:
        if counter == 9:
            print("Draw")