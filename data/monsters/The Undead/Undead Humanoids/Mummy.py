mummy = genMonster("Mummy", 65, 6004)
mummy.health(240)
mummy.type("undead")
mummy.defense(armor=15, fire=1, earth=1, energy=1, ice=0.8, holy=1.25, death=1, physical=1, drown=1)
mummy.experience(150)
mummy.speed(220)
mummy.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=False, targetDistance=1, runOnHealth=0)
mummy.walkAround(energy=1, fire=1, poison=0)
mummy.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=0)
mummy.voices("I will ssswallow your sssoul!", "Mort ulhegh dakh visss.", "Flesssh to dussst!", "I will tassste life again!", "Ahkahra exura belil mort!", "Yohag Sssetham!")
mummy.melee(85)
mummy.loot( (2148, 100, 80), ("flask of embalming fluid", 11.75), (2162, 6.0), (3976, 35.5, 3), ("gauze bandage", 10.0), ("silver brooch", 3.75), ("strange talisman", 5.25), ("yellow piece of cloth", 1.0, 3), ("poison dagger", 0.5), ("crystal ring", 1.75), ("black shield", 0.25), ("black pearl", 1.0), ("silver amulet", 0.25) )