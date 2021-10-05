import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('nmsf está listo'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    animales=('Zorro', 'Perro', 'Gato')
    intereses=('Música', 'Películas', 'Comida', 'Dormir')
    generos=('Hombre', 'Mujer')
    sexualidades=('Gay', 'Lesbiana')

    if message.content.startswith('MiFursona'):
        ranimal=random.choice(animales)
        rinteres="".join(random.choice(intereses)+", "+random.choice(intereses)+".")
        rgenero=random.choice(generos)
        rsexualidad=random.choice(sexualidades)
        redad=random.randint(1,100)
        nombre = message.author.display_name
        
        await message.channel.send('Nombre: ' + nombre + '\nAnimal: ' + ranimal + '\nEdad: ' + str(redad) + '\nGénero: ' + rgenero + 
                                   '\nSexualidad: ' + rsexualidad + '\nIntereses: ' + rinteres)

client.run('token del bot')
