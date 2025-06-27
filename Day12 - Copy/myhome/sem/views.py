from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def mca101(request):
    temp=loader.get_template('mca101.html')
    return HttpResponse(temp.render())
def mca102(request):
    temp=loader.get_template('mca102.html')
    return HttpResponse(temp.render())
def mca103(request):
    temp=loader.get_template('mca103.html')
    return HttpResponse(temp.render())
def mca104(request):
    temp=loader.get_template('mca104.html')
    return HttpResponse(temp.render())
def mca105(request):
    temp=loader.get_template('mca105.html')
    return HttpResponse(temp.render())
def mca106(request):
    temp=loader.get_template('mca106.html')
    return HttpResponse(temp.render())
def mca107(request):
    temp=loader.get_template('mca107.html')
    return HttpResponse(temp.render())
def mca108(request):
    temp=loader.get_template('mca108.html')
    return HttpResponse(temp.render())
def mca201(request):
    temp=loader.get_template('mca201.html')
    return HttpResponse(temp.render())
def mca202(request):
    temp=loader.get_template('mca202.html')
    return HttpResponse(temp.render())
def mca203(request):
    temp=loader.get_template('mca203.html')
    return HttpResponse(temp.render())
def mca204(request):
    temp=loader.get_template('mca204.html')
    return HttpResponse(temp.render())
def mca205(request):
    temp=loader.get_template('mca205.html')
    return HttpResponse(temp.render())
def mca206(request):
    temp=loader.get_template('mca206.html')
    return HttpResponse(temp.render())
def mca207(request):
    temp=loader.get_template('mca207.html')
    return HttpResponse(temp.render())
def mca208(request):
    temp=loader.get_template('mca208.html')
    return HttpResponse(temp.render())
def mca209(request):
    temp=loader.get_template('mca209.html')
    return HttpResponse(temp.render())
def mca301(request):
    temp=loader.get_template('mca301.html')
    return HttpResponse(temp.render())
def mca302(request):
    temp=loader.get_template('mca302.html')
    return HttpResponse(temp.render())
def mca303(request):
    temp=loader.get_template('mca303.html')
    return HttpResponse(temp.render())
def mca304(request):
    temp=loader.get_template('mca304.html')
    return HttpResponse(temp.render())
def mca305(request):
    temp=loader.get_template('mca305.html')
    return HttpResponse(temp.render())
def mca306(request):
    temp=loader.get_template('mca306.html')
    return HttpResponse(temp.render())
def mca307(request):
    temp=loader.get_template('mca307.html')
    return HttpResponse(temp.render())
def mca308(request):
    temp=loader.get_template('mca308.html')
    return HttpResponse(temp.render())
def mca309(request):
    temp=loader.get_template('mca309.html')
    return HttpResponse(temp.render())
def mca310(request):
    temp=loader.get_template('mca310.html')
    return HttpResponse(temp.render())
def mca401(request):
    temp=loader.get_template('mca401.html')
    return HttpResponse(temp.render())
def mca402(request):
    temp=loader.get_template('mca402.html')
    return HttpResponse(temp.render())
def mca403(request):
    temp=loader.get_template('mca403.html')
    return HttpResponse(temp.render())
def mca501(request):
    temp=loader.get_template('mca501.html')
    return HttpResponse(temp.render())
def mca502(request):
    temp=loader.get_template('mca502.html')
    return HttpResponse(temp.render())
def mca503(request):
    temp=loader.get_template('mca503.html')
    return HttpResponse(temp.render())
def mca504(request):
    temp=loader.get_template('mca504.html')
    return HttpResponse(temp.render())
def mca505(request):
    temp=loader.get_template('mca505.html')
    return HttpResponse(temp.render())
def about(request):
    temp=loader.get_template('about.html')
    return HttpResponse(temp.render())




def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    return result if not pisa_status.err else HttpResponse('PDF generation failed')


def pdf_view(request):
    data = {
        'name': 'Praveen Choudhary',
        'course': 'Django Development',
        'date': '2025-06-27'
    }
    return render_to_pdf('pdf_template.html', data)




# Create your views here.
