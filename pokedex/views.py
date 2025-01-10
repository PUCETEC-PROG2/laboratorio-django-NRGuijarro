from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    
    context = {
        'pokemons': pokemons,
        'trainers': trainers,
    }
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))
