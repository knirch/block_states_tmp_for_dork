execute positioned ~ ~-2 ~ run loot spawn ~ -65 ~ loot id.block:block
execute positioned ~ -65 ~ run data modify storage example:data block set from entity @n[type=item] Item.components."minecraft:custom_data".block
execute positioned ~ -65 ~ run kill @n[type=item,distance=..1]

tellraw @s {"nbt":"block","storage":"example:data"}

