$data modify storage kch:block args.property set value "$(p)"
$data modify storage kch:block args.value set from storage kch:block properties.$(p)
data modify storage kch:block args.arg set value ""
data modify storage kch:block args.arg set from storage kch:block arg

function block_states:aarg with storage kch:block args
