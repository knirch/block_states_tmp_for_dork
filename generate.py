from collections import defaultdict
from rich import pretty
import json

block_states = json.load(open("/home/knirch/mcmeta/summary/blocks/data.json"))

loot_table = {
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "minecraft:item",
                    "name": "minecraft:stick",
                    "functions": [],
                }
            ],
        }
    ]
}

example_function = {
    "function": "set_custom_data",
    "tag": {"axis": "x"},
    "conditions": [
        {
            "condition": "location_check",
            "predicate": {"block": {"state": {"axis": "x"}}},
        }
    ],
}

states = defaultdict(set)

for block, x in sorted(block_states.items()):
    #print(x[1])
    for state, values in x[0].items():
        states[state].update(values)
        # print(f"{block} {state} {values}")


txt_func = "functions:[{{function:set_custom_data,tag:{{{tag}: {value}}}}}]"

# pretty.pprint(states)

for block_state, values in sorted(states.items()):
    for value in sorted(values):
        loot_table["pools"][0]["entries"][0]['functions'].append(
            {
                "function": "set_custom_data",
                "tag": {block_state: value},
                "conditions": [
                    {
                        "condition": "location_check",
                        "predicate": {"block": {"state": {block_state: value}}},
                    }
                ],
            }
        )

#pretty.pprint(loot_table)

print(json.dumps(loot_table, indent=2))
