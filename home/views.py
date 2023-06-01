from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from bg.settings import EMAIL_HOST_USER

def calc_had(request):

    # pontuaçõe ansiedade e depressão
    pont_ans = 0
    pont_dep = 0

    # obtendo as variáveis do formulário preenchido
    varEuMeSintoTen = request.POST['radioEuMeSintoTen']
    varEuAindaSinto = request.POST['radioEuAindaSinto']
    varEuSintoUmaEsp = request.POST['radioEuSintoUmaEsp']
    varDouRis = request.POST['radioDouRis']
    varEstouComACab = request.POST['radioEstouComACab']
    varEuMeSinto = request.POST['radioEuMeSinto']
    varConsigoFicarSent = request.POST['radioConsigoFicarSent']
    varEuEstouLent = request.POST['radioEuEstouLent']
    varEuTenhoUmaSen = request.POST['radioEuTenhoUmaSen']
    varEuPer = request.POST['radioEuPer']
    varEuMeSintoInq = request.POST['radioEuMeSintoInq']
    varFicoAnim = request.POST['radioFicoAnim']
    varDeRep = request.POST['radioDeRep']
    varConsigoSent = request.POST['radioConsigoSent']

    # Cálculo da pontuação da ansiedade
    if(varEuMeSintoTen == 'a maior parte do tempo'):
        pont_ans = 3
    elif(varEuMeSintoTen == 'boa parte do tempo'):
        pont_ans = 2
    elif(varEuMeSintoTen == 'de vez em quando'):
        pont_ans = 1
    else:
        pont_ans = 0

    if(varEuSintoUmaEsp == 'sim, de jeito muito forte'):
        pont_ans = pont_ans + 3
    elif(varEuSintoUmaEsp == 'sim, mas não tão forte'):
        pont_ans = pont_ans + 2
    elif(varEuSintoUmaEsp == 'um pouco, mas isso não me preocupa'):
        pont_ans = pont_ans + 1
    else:
        pont_ans = pont_ans


    if(varEstouComACab == 'a maior parte do tempo'):
        pont_ans = pont_ans + 3
    elif(varEstouComACab == 'boa parte do tempo'):
        pont_ans = pont_ans + 2
    elif(varEstouComACab == 'de vez em quando'):
        pont_ans = pont_ans + 1
    else:
        pont_ans = pont_ans

    if(varConsigoFicarSent == 'sim, quase sempre'):
        pont_ans = pont_ans
    elif(varConsigoFicarSent == 'muitas vezes'):
        pont_ans = pont_ans + 1
    elif(varConsigoFicarSent == 'poucas vezes'):
        pont_ans = pont_ans + 2
    else:
        pont_ans = pont_ans + 3 


    if(varEuTenhoUmaSen == 'nunca'):
        pont_ans = pont_ans 
    elif(varEuTenhoUmaSen == 'de vez em quando'):
        pont_ans = pont_ans + 1
    elif(varEuTenhoUmaSen == 'muitas vezes'):
        pont_ans = pont_ans + 2
    else:
        pont_ans = pont_ans + 3

    if(varEuMeSintoInq == 'sim, demais'):
        pont_ans = pont_ans + 3
    elif(varEuMeSintoInq == 'bastante'):
        pont_ans = pont_ans + 2
    elif(varEuMeSintoInq == 'um pouco'):
        pont_ans = pont_ans + 1
    else:
        pont_ans = pont_ans

    if(varDeRep == 'a quase todo momento'):
        pont_ans = pont_ans + 3
    elif(varDeRep == 'várias vezes'):
        pont_ans = pont_ans + 2
    elif(varDeRep == 'de vez em quando'):
        pont_ans = pont_ans + 1
    else:
        pont_ans = pont_ans

    # cálculo da pontuação da depressão

    if(varEuAindaSinto == 'sim, do mesmo jeito que antes'):
        pont_dep = pont_dep + 0
    elif(varEuAindaSinto == 'não tanto quanto antes'):
        pont_dep = pont_dep + 1
    elif(varEuAindaSinto == 'só um pouco'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3

    if(varEuAindaSinto == 'sim, do mesmo jeito que antes'):
        pont_dep = pont_dep + 0
    elif(varEuAindaSinto == 'não tanto quanto antes'):
        pont_dep = pont_dep + 1
    elif(varEuAindaSinto == 'só um pouco'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3
    
    if(varDouRis == 'do mesmo jeito que antes'):
        pont_dep = pont_dep + 0
    elif(varEuAindaSinto == 'atualmente um pouco menos'):
        pont_dep = pont_dep + 1
    elif(varEuAindaSinto == 'atualmente bem menos'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3
    
    if(varDouRis == 'do mesmo jeito que antes'):
        pont_dep = pont_dep + 0
    elif(varDouRis == 'atualmente um pouco menos'):
        pont_dep = pont_dep + 1
    elif(varDouRis == 'atualmente bem menos'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3

    if(varEuMeSinto == 'a maior parte do tempo'):
        pont_dep = pont_dep + 0
    elif(varEuMeSinto == 'muitas vezes'):
        pont_dep = pont_dep + 1
    elif(varEuMeSinto == 'poucas vezes'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3
    
    if(varEuEstouLent == 'nunca'):
        pont_dep = pont_dep + 0
    elif(varEuEstouLent == 'poucas vezes'):
        pont_dep = pont_dep + 1
    elif(varEuEstouLent == 'muitas vezes'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3

    if(varEuPer == 'me cuido do mesmo jeito que antes'):
        pont_dep = pont_dep + 0
    elif(varEuPer == 'talvez não tanto quanto antes'):
        pont_dep = pont_dep + 1
    elif(varEuPer == 'não estou mais me cuidando como eu deveria'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3

    if(varFicoAnim == 'do mesmo jeito que antes'):
        pont_dep = pont_dep + 0
    elif(varFicoAnim == 'um pouco menos que antes'):
        pont_dep = pont_dep + 1
    elif(varFicoAnim == 'bem menos do que antes'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3

    if(varConsigoSent == 'quase sempre'):
        pont_dep = pont_dep + 0
    elif(varConsigoSent == 'várias vezes'):
        pont_dep = pont_dep + 1
    elif(varConsigoSent == 'poucas vezes'):
        pont_dep = pont_dep + 2
    else:
        pont_dep = pont_dep + 3

    return pont_ans, pont_dep

def cal_suggestions(pontuacao_ansiedade, pontuacao_depressao):
    pontuacao_ansiedade_string = ''
    pontuacao_depressao_string = ''

    if(pontuacao_ansiedade <=7):
        pontuacao_ansiedade_string = "Ansiedade improvável"
        sugestao_ansiedade = "Índices dentro dos valores normais; improvável situação de ansiedade. Mas sugerimos que sempre pratique alguma atividade física, dedique um tempo para si e pratique meditação."
    elif(pontuacao_ansiedade<=10):   
        pontuacao_ansiedade_string = "Ansiedade moderada provável"
        sugestao_ansiedade = "Ansiedade com índices “possível”; sugerimos fortemente práticas de meditação/mindfulness, atividade física minima 3x semana, reforço na rede de apoio e avaliação psicológica."
    elif(pontuacao_ansiedade<=15):
        pontuacao_ansiedade_string = "Ansiedade significativa provável"
        sugestao_ansiedade = "Ansiedade com índices preocupantes, possível quadro de ansiedade. Sugerimos avaliação profissional para acompanhamento e confirmar diagnóstico. Lembre-se : peça ajuda e melhore sua qualidade de vida. Todos somos pacientes!"
    else:
        pontuacao_ansiedade_string = "Índices altos de ansiedade"
        sugestao_ansiedade = "Ansiedade com índices alarmantes, extremamente provável quadro de ansiedade. Recomendamos imediata procura por profissional especializado. Se quiser uma sessão devolutiva confidencial para orientação, agende horário com contato@bgtreinamentos.com.br Sta ALINE, nossos profissionais da saúde podem orientá-lo a buscar ajuda."
    

    if(pontuacao_depressao <=7):
        pontuacao_depressao_string = "Depressão pouco provável"
        sugestao_depressao = "Índices dentro dos valores normais; improvável situação de depressão. Mas sugerimos que sempre pratique alguma atividade física, dedique um tempo para si, pratique meditação."
    elif(pontuacao_depressao<=11):
        pontuacao_depressao_string = "Depressão possível"
        sugestao_depressao = "Depressão com índices “possível”; sugerimos fortemente práticas de meditação/mindfulness, atividade física minima 3x semana, reforço na rede de apoio e avaliação psicológica."
    elif(pontuacao_depressao<=15):
        pontuacao_depressao_string = "Depressão provável"
        sugestao_depressao = "Depressão com índices preocupantes, possível quadro de depressão. Sugerimos avaliação profissional para acompanhamento e confirmar diagnóstico. Lembre-se : peça ajuda e melhore sua qualidade de vida. Todos somos pacientes!"
    else:
        pontuacao_ansiedade_string = "Índices altos de depressão"
        sugestao_depressao = "Depressão com índices alarmantes, extremamente provável quadro de depressão. Recomendamos imediata procura por profissional especializado. Se quiser uma sessão devolutiva confidencial para orientação, agende horário com contato@bgtreinamentos.com.br ."
    
    return pontuacao_ansiedade_string, pontuacao_depressao_string, sugestao_ansiedade, sugestao_depressao

def index(request):

    if request.method == 'POST':
        user_email = request.POST['userEmail']
        pont_ans, pont_dep = calc_had(request)
        pont_ans_str, pont_dep_str, sug_ans, sug_dep = cal_suggestions(pont_ans, pont_dep)

        image_url = 'https://raw.githubusercontent.com/estevanrlima/bgtreinamentos/main/logo%20BG%20treinamentos.png'
        context = {'image_url': image_url}

        subject = 'Devolutiva - BG Saúde'
        html_content = render_to_string('home/email_template.html', {
            'pontuacao_ansiedade_string': pont_ans_str,
            'sugestao_ansiedade': sug_ans,
            'pontuacao_depressao_string': pont_dep_str,
            'sug_dep': sug_dep,
            'image_url': image_url,
        })

        # Create the plain text version of the email (optional)
        plain_message = strip_tags(html_content)

        send_mail(
            subject,
            plain_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user_email],
            fail_silently=False,
            html_message=html_content
        )

    return render(request, 'home/index.html')