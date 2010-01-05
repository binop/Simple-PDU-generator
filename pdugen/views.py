from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect

from pdugen.forms import SMSDataForm
from pdugen.models import SMSData
from pdugen.helpers import generate_pdu


def list(request):
    return render_to_response('pdugen/list.html',
                              {'smsdata_list' : SMSData.objects.all() },
                              context_instance=RequestContext(request))


def new(request):
    PDU, length_in_oct = None, 0

    if request.method == 'POST': 
        form = SMSDataForm(request.POST)
        if form.is_valid():
            if 'save_draft_flag' in request.POST:
                sms_data = form.save()
                return HttpResponseRedirect(sms_data.get_absolute_url())
            else:
                sms_data = form.save(commit=False)
            
            PDU = generate_pdu(sms_data.__dict__)
            length_in_oct = len(PDU)
    else:
        form = SMSDataForm()
        
    return render_to_response('pdugen/result.html', 
                              {'form': form,
                               'PDU' : PDU,
                               'length_in_oct': length_in_oct }, 
                              context_instance=RequestContext(request))


def details(request, object_id):
    sms_data = get_object_or_404(SMSData, pk=object_id)

    if request.method == 'POST':
        form = SMSDataForm(request.POST, instance=sms_data)
        
        if form.is_valid():
            if 'save_draft_flag' in request.POST:
                sms_data = form.save()
    else: 
        form = SMSDataForm(instance=sms_data)

    PDU = generate_pdu(sms_data.__dict__)    
    return render_to_response('pdugen/result.html',
                              {'PDU' : PDU,
                               'length_in_oct': len(PDU), 
                               'form' : form },
                              context_instance=RequestContext(request)) 


def remove(request, object_id):
    get_object_or_404(SMSData, pk=object_id).delete()
    return redirect('list')
