from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/4%20Django/labs/pokemon.json')
        data = response.json()
        # print(data)
        for pokemon_data in data['pokemon']:
            number = pokemon_data['number']
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            image_front = pokemon_data['image_front']
            image_back = pokemon_data['image_back']
            type_names = pokemon_data['types']

            pokemon = Pokemon(number=number, name=name, height=height, weight=weight, image_front=image_front, image_back=image_back)
            pokemon.save()

            # print(type_names)
            for type_name in type_names:
                # print(type_name)
                pokemon_type, created = PokemonType.objects.get_or_create(
                    name = type_name
                )
                pokemon.types.add(pokemon_type)