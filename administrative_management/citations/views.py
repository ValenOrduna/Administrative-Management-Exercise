from django.shortcuts import render,redirect
from citations.models import Citation
from django.contrib.auth.decorators import login_required
from datetime import datetime
from officers.models import Officer
from citations.forms.citationForm import CitationForm

# Controller Informacion Multa
# Validamos si el usuario ya esta logueado, sino lo redirigimos al login
@login_required(login_url='/login')
def informationCitation(request,idCitation):
    if request.user.is_authenticated:
        try:
            # Realizamos sentencia y obtenemos la citation
            citation = Citation.objects.get(pk=idCitation)
            return render(request,'informationCitation.html',{'title':f'Citation {citation.id}','citation':citation})
        except Exception as e:
            return redirect('/')
        
# Controller Informacion Multa
# Validamos si el usuario ya esta logueado, sino lo redirigimos al login
@login_required(login_url='/login')
def createCitation(request):
    if request.user.groups.filter(name='Officer').exists() or request.user.groups.filter(name='Admin').exists():
        if request.method == 'POST':
            form =  CitationForm(request.POST)
            if form.is_valid():
                try:
                    user = request.user.username
                    user = user.replace('_',' ')
                    user = user.title()
                    officer = Officer.objects.get(name=user)
                    now = datetime.now()
                    form.cleaned_data['violationDate'] = now.strftime("%Y-%m-%d")
                    form.cleaned_data['violationTime'] = now.strftime('%H:%M')
                    form.cleaned_data['officer'] = officer
                    citation = Citation(**form.cleaned_data)
                    citation.save()
                    return render(request, 'createCitation.html',{'alert':{'success':'The citation has been uploaded successfully'}})
                except Exception as e:
                    print(e)
                    return render(request, 'createCitation.html',{'alert':{'error':'An unexpected error has occurred, please try again later.'}})
            return render(request, 'createCitation.html',{'alert':{'error':'You have entered some information incorrectly in the form.'}})
        return render(request, 'createCitation.html')
    return redirect('/')