
from telethon import events
import random
import asyncio

@borg.on(events.NewMessage(pattern=r"\.fk (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "mom":
        gaali = [
            "Teri maa ki chut badi majbut",
			"Jake apni maa ke muh pe hilale",
			"Teri maa randi",
			"Sala Randi Madarchod ladka",
			"Maa ka laadla biwi ka kutta",
			"Randi chod chup kar",
			"Gand na fulao maa chod denge",
			"Maa ki jhat me se bahar to aja",
			"Teri ma ke saath itne nudes nikale",
			"Teri ma ki Chut Mai mera M24 with 15x",
        ]

    elif input_str in "dad":
        gaali = [
            
			"Tera baap Randachoda",
			"Chhinal ka beta",
			"Lavde baap ko mat sikha",
			"Baap ka bhosda",
			"Jaake apne baap ki gand maro",
			"Baap tera randi khane me randiya taar raha.",
        ]
    else:    
        gaali = [
           
			"Topa insaan",
			"Kya Randapaa macha rakha hai bc",
			"Landu",
			"Ghanta fark nahi padta apne ko",
			"abe chirkut ki aulad",
			"chutiya hai kya gandu?",
			"abe tatto ke saudagar",
			"Gaand mein Jhadu dalke mor bana dunga",
			"Agaye lauda lassan karne",
			"Awwal darje ka chutiya insaan",
			"Gandi nasal ke jhantu insaan",
        ]
    index = random.randint(0, len(gaali))
    output_str = gaali[index]
    await event.edit(output_str)
