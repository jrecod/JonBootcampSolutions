from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import PokemonType, Pokemon
from django.core.paginator import Paginator

def index(request):
    pokemon = Pokemon.objects.all()
    pokemon_type = PokemonType.objects.all()
    search = request.GET.get('search', '')
    if search !='':
        pokemon = pokemon.filter(Q(name__icontains=search))

    page_number = request.GET.get('page', 1)
    pokemon_per_page = 20
    paginator = Paginator(pokemon, pokemon_per_page)
    poke_page = paginator.page(page_number)
    context = {
        'pokemons': pokemon,
        'pokemon': poke_page,
        'search': search,
    }
    return render(request, 'pokedex/index.html', context)

def details(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokedex/details.html', context)