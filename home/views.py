from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail

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

    return pont_ans, pont_dep

def index(request):

    if(request.method == 'POST'):
        user_email = request.POST['userEmail']
        pont_ans, pont_dep = calc_had(request)    
        send_mail('Pontuacao HAD', f'Sua pontuacao ansiedade é: {pont_ans} e sua pontuacao para depressão é {pont_dep}', 'ti@bgsaude.med.br', [user_email], fail_silently = False)
    return render(request, 'home/index.html')