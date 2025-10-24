import json

block_states = json.load(open("/home/knirch/mcmeta/summary/blocks/data.json"))

properties = set()

for block, x in block_states.items():
    for state, values in x[0].items():
        properties.add(state)

print("data remove storage kch:block arg")
for state in sorted(properties):
    print(f"execute if data storage kch:block properties.{state} run function block_states:prop {{p: {state}}}")
