# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

gullit = "Ruud Gullit"
basten = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{gullit} {goal_0}, {basten} {goal_1}"

report = f'{gullit} scored in the {goal_0}nd minute\n{basten} scored in the {goal_1}th minute' 

player = "Ronald Koeman"
first_name = player.split()[0]
last_name_len = len(player.split()[1])

name_short = f"{first_name[0]}. {player.split()[1]}"

chant_with_space = f"{first_name}! " * len(first_name)
chant = chant_with_space[:-1]

good_chant = chant[-1] != " "