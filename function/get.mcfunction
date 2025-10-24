function kch.lib:block/get
loot spawn ~ -65 ~ loot block_states:get_state
execute positioned ~ -65 ~ run data modify storage kch:block properties set from entity @n[type=item] Item.components."minecraft:custom_data"
execute positioned ~ -65 ~ run kill @n[type=item,distance=..1]
data modify storage kch:block data set from block ~ ~ ~
data remove storage kch:block data.x
data remove storage kch:block data.y
data remove storage kch:block data.z


