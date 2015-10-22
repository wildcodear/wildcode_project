from django.shortcuts import render, get_object_or_404

from .models import Proform


def index(request, proform_id):
    proform = get_object_or_404(Proform, id=proform_id)
    context = {}
    context['proform'] = proform
    context['works'] = proform.works.all()
    return render(request, 'documents/proform/print.html', context)
