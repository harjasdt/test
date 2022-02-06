from django.shortcuts import render
from bigapp.models import QUESTION,add,nomi
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
con=0
ex=0
openness=0
neuro=0
agree=0
global res
res=[]

def home(request):
    return render(request,'home.html')

def nominate(request):
    if request.method=='POST':
        name=request.POST['name']
        msg=request.POST['msg']
        mail=request.POST['mail']
        sender_name=request.POST['sender_name']
        data=add.objects.create( mail=mail)
        data.save()
        #email
        html_message = render_to_string('nomi_mail.html', {'name': name,'msg':msg,'sender_name':sender_name})
        from_email = 'firsttry73@gmail.com'
        recipient_list = [request.POST['mail'],'']  # put your real email here
        subject = 'Nominated for Big 5 Personality Test'
        message = render_to_string(template_name='nomi_mail.html')
        send_mail(subject, message, from_email, recipient_list,html_message=html_message)
        return render(request,'home.html')
    return render(request,'nominate.html')

def logic(request):
    return render(request,'logic.html')

def question(request):
    return render(request,'question.html')

def test(request):
    if request.method=='POST':
        q1=int(request.POST['q1'])
        q2=int(request.POST['q2'])
        q3=int(request.POST['q3'])
        q4=int(request.POST['q4'])
        q5=int(request.POST['q5'])
        q6=int(request.POST['q6'])
        q7=int(request.POST['q7'])
        q8=int(request.POST['q8'])
        q9=int(request.POST['q9'])
        q10=int(request.POST['q10'])
        q11=int(request.POST['q11'])
        q12=int(request.POST['q12'])
        q13=int(request.POST['q13'])
        q14=int(request.POST['q14'])
        q15=int(request.POST['q15'])
        q16=int(request.POST['q16'])
        q17=int(request.POST['q17'])
        q18=int(request.POST['q18'])
        q19=int(request.POST['q19'])
        q20=int(request.POST['q20'])
        q21=int(request.POST['q21'])
        q22=int(request.POST['q22'])
        q23=int(request.POST['q23'])
        q24=int(request.POST['q24'])
        q25=int(request.POST['q25'])
        q26=int(request.POST['q26'])
        q27=int(request.POST['q27'])
        q28=int(request.POST['q28'])
        q29=int(request.POST['q29'])
        q30=int(request.POST['q30'])
        q31=int(request.POST['q31'])
        q32=int(request.POST['q32'])
        q33=int(request.POST['q33'])
        q34=int(request.POST['q34'])
        q35=int(request.POST['q35'])
        q36=int(request.POST['q36'])
        q37=int(request.POST['q37'])
        q38=int(request.POST['q38'])
        q39=int(request.POST['q39'])
        q40=int(request.POST['q40'])
        q41=int(request.POST['q41'])
        q42=int(request.POST['q42'])
        q43=int(request.POST['q43'])
        q44=int(request.POST['q44'])
        q45=int(request.POST['q45'])
        q46=int(request.POST['q46'])
        q47=int(request.POST['q47'])
        q48=int(request.POST['q48'])
        q49=int(request.POST['q49'])
        q50=int(request.POST['q50'])

        data=QUESTION.objects.create(
        q1=int(q1),
        q2=int(q2),
        q3=int(q3),
        q4=int(q4),
        q5=int(q5),
        q6=int(q6),
        q7=int(q7),
        q8=int(q8),
        q9=int(q9),
        q10=int(q10),
        q11=int(q11),
        q12=int(q12),
        q13=int(q13),
        q14=int(q14),
        q15=int(q15),
        q16=int(q16),
        q17=int(q17),
        q18=int(q18),
        q19=int(q19),
        q20=int(q20),
        q21=int(q21),
        q22=int(q22),
        q23=int(q23),
        q24=int(q24),
        q25=int(q25),
        q26=int(q26),
        q27=int(q27),
        q28=int(q28),
        q29=int(q29),
        q30=int(q30),
        q31=int(q31),
        q32=int(q32),
        q33=int(q33),
        q34=int(q34),
        q35=int(q35),
        q36=int(q36),
        q37=int(q37),
        q38=int(q38),
        q39=int(q39),
        q40=int(q40),
        q41=int(q41),
        q42=int(q42),
        q43=int(q43),
        q44=int(q44),
        q45=int(q45),
        q46=int(q46),
        q47=int(q47),
        q48=int(q48),
        q49=int(q49),
        q50=int(q50),
        )
        data.save()
        openness=(q5+q15+q25+q35+q40+q45+q50)+((6-q10)+(6-q20)+(6-q30))
        con=(q3+q13+q23+q33+q43+q48)+((6-q8)+(6-q18)+(6-q28)+(6-q38))
        ex=(q1+q11+q21+q31+q41)+((6-q6)+(6-q16)+(6-q26)+(6-q36)+(6-q46))
        agree=(q7+q17+q27+q37+q42+q47)+((6-q2)+(6-q12)+(6-q22)+(6-q32))
        neuro=(q5+q19)+((6-q4)+(6-q14)+(6-q24)+(6-q29)+(6-q34)+(6-q39)+(6-q44)+(6-q49))
        request.session['openness'] = openness
        request.session['con'] = con
        request.session['ex'] = ex
        request.session['agree'] = agree
        request.session['neuro'] = neuro      
        context={'openness':openness,'con':con,'ex':ex,'agree':agree,'neuro':neuro}
        return render(request,'result.html',context)
    return render(request,'test.html')

def result(request):
    if request.method=='POST':
        mail=request.POST['mail']
        data=add.objects.create( mail=mail)
        data.save()
        #email
        openness = request.session['openness']
        con = request.session['con']
        ex = request.session['ex']
        agree = request.session['agree']
        neuro = request.session['neuro']
        html_message = render_to_string('email.html', {'openness':openness,'con':con,'ex':ex,'agree':agree,'neuro':neuro})
        from_email = 'firsttry73@gmail.com'
        recipient_list = [request.POST['mail'],'']  # put your real email here
        subject = 'Big 5 Personality Test Result'
        message = render_to_string(template_name='email.html')
        send_mail(subject, message, from_email, recipient_list,html_message=html_message)
        return render(request,'home.html')
    return render(request,'result.html')