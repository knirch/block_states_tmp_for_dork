import json

jj = json.load(open("/home/knirch/mcmeta/summary/registries/data.json"))
block_states = json.load(open("/home/knirch/mcmeta/summary/blocks/data.json"))

blocks_with_state = set(block_states.keys())
blocks_with_data = set(jj["block_entity_type"])

# Fixelidix
#
# blocks_with_data has these that doesn't exist in block_states;
# {'brushable_block', 'banner', 'skull', 'mob_spawner', 'bed', 'sign', 'hanging_sign'}

colors = [
    "black",
    "blue",
    "brown",
    "cyan",
    "gray",
    "green",
    "light_blue",
    "light_gray",
    "lime",
    "magenta",
    "orange",
    "pink",
    "purple",
    "red",
    "white",
    "yellow",
]

banners = [
    f"{color}_{banner}" for color in colors for banner in ("wall_banner", "banner")
]
beds = [f"{color}_bed" for color in colors]

# Woods; sign(+wall), hanging_sign(+wall)

wood_types = [
    "acacia",
    "bamboo",
    "birch",
    "cherry",
    "crimson",
    "dark_oak",
    "jungle",
    "mangrove",
    "oak",
    "pale_oak",
    "spruce",
    "warped",
]

signs = [
    f"{wood}_{sign}"
    for wood in wood_types
    for sign in ("wall_sign", "wall_hanging_sign", "sign", "hanging_sign")
]

blocks_with_data = blocks_with_data - set(['brushable_block', 'banner', 'bed', 'sign', 'hanging_sign'])
blocks_with_data.update(['suspicious_sand', 'suspicious_gravel'])
blocks_with_data.update(banners)
blocks_with_data.update(beds)
blocks_with_data.update(signs)

###

blocks_with_state_without_data = blocks_with_state - blocks_with_data

# Specials;
# hanging_sign == <type>_hanging_sign
#
# do not know if they are defined anywhere, as hanging_sign parent..


bug = blocks_with_data - blocks_with_state


