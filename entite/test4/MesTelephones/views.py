from MesTelephones.models import Type
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from MesTelephones.models import Telephone
from django.urls import reverse
def index(request):
    prod = Telephone.objects.all().values()
    type=Type.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'prod': prod,
        'type':type
    }
    return HttpResponse(template.render(context, request))

def del_prod(request, id):
    produits = Telephone.objects.get(id=id)
    produits.delete()
    return HttpResponseRedirect(reverse('MesTelephones'))

def list_typ(request):
    typ = Type.objects.all().values()
    template = loader.get_template('type.html')
    context = {
    'typ':typ,
    }
    return HttpResponse(template.render(context, request))