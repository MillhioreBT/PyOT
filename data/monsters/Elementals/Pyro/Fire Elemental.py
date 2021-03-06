fire_elemental = genMonster("Fire Elemental", 49, 8964)
fire_elemental.health(280, healthmax=280)
fire_elemental.type("blood")
fire_elemental.defense(armor=20, fire=0, earth=1, energy=1, ice=1.25, holy=1, death=0, physical=1, drown=1)
fire_elemental.experience(220)
fire_elemental.speed(200)
fire_elemental.behavior(summonable=690, hostile=True, illusionable=True, convinceable=690, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
fire_elemental.walkAround(energy=1, fire=0, poison=1)
fire_elemental.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
fire_elemental.melee(100)