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

def cal_suggestions_had(pontuacao_ansiedade, pontuacao_depressao):
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

def calc_resili(request):
    #pontuações
    pont_resil = 0
    pont_qp = 0
    pont_qe = 0
    pont_qi = 0
    pont_sono = 0
    pont_at_fis = 0
    pont_vida_social = 0

    # obtendo as variáveis do formulário preenchido
    varAcordaMais2x = request.POST['radioAcordaMais2x']
    varEmGeralConsDormir = request.POST['radioEmGeralConsDormir']
    varPesoAdeq = request.POST['radioPesoAdeq']
    varPossuiRotina = request.POST['radioPossuiRotina']
    varSenteSobrec = request.POST['radioSenteSobrec']
    varTemVidaSocial = request.POST['radioTemVidaSocial']
    varPraticaMed = request.POST['radioPraticaMed']
    varVicio = request.POST['radioVicio']
    varDivideTempo = request.POST['radioDivideTempo']
    varTiraTempo = request.POST['radioTiraTempo']
    varOtimismo = request.POST['radioOtimismo']
    varEuMeEntusia = request.POST['radioEuMeEntusia']
    varSouAlegre = request.POST['radioSouAlegre']
    varMeSintoCapaz = request.POST['radioMeSintoCapaz']
    varObs = request.POST['radioObs']
    varOrganizado = request.POST['radioOrganizado']
    varEq = request.POST['radioEq']
    varEmGeralReage = request.POST['radioEmGeralReage']
    varDesiste = request.POST['radioDesiste']
    varConsegueVer = request.POST['radioConsegueVer']
    varConsegueCeder = request.POST['radioConsCeder']
    varPensaMuito = request.POST['radioPensaMuito']
    varReconhece = request.POST['radioReconhece']
    varDianteCrise = request.POST['radioDianteCrise']
    varSenteForca = request.POST['radioSenteForca']
    varCapazPerdoar = request.POST['radioCapazPerdoar']
    varPossuiForcaEsp = request.POST['radioPossuiForcaEsp']
    varAcredita = request.POST['radioAcredita']
    varViveBem = request.POST['radioViveBem']
    varSenteRealiza = request.POST['radioSenteRealiza']
    varSabeReal = request.POST['radioSabeReal']

    
    if(varAcordaMais2x == 'sim, muito comum'):
        pont_resil = 0
    elif(varAcordaMais2x == 'boa parte do tempo'):
        pont_resil = 2
    elif(varAcordaMais2x == ' médio, talvez, as vezes'):
        pont_resil = 4
    else:
        pont_resil = 6

    if(varEmGeralConsDormir == 'sim, muito comum'):
        pont_resil = pont_resil + 3
    elif(varEmGeralConsDormir == 'nem sempre, às vezes'):
        pont_resil = pont_resil + 2
    elif(varEmGeralConsDormir == 'raramente'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varPesoAdeq == 'sim, me sinto com peso adequado'):
        pont_resil = pont_resil + 3
    elif(varPesoAdeq == 'médio, talvez um pouco acima do peso (até 6 kg do ideal)'):
        pont_resil = pont_resil + 2
    elif(varPesoAdeq == 'Não estou com peso ideal, estou muito acima (ou abaixo) do peso'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varPossuiRotina == 'sim, tenho rotina frequente'):
        pont_resil = pont_resil + 6
    elif(varPossuiRotina == 'médio, às vezes falho ou não me dedico firme'):
        pont_resil = pont_resil + 4
    elif(varPossuiRotina == 'eventualmente faço alguma atividade, sem rotina'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varSenteSobrec == 'sim, muito comum'):
        pont_resil = pont_resil + 0
    elif(varSenteSobrec == 'médio, talvez, às vezes'):
        pont_resil = pont_resil + 2
    elif(varSenteSobrec == 'não é comum, raramente'):
        pont_resil = pont_resil + 4
    else:
        pont_resil = pont_resil + 6

    if(varTemVidaSocial == 'sim, muito comum ; tenho vida social'):
        pont_resil = pont_resil + 6
    elif(varTemVidaSocial == 'médio, talvez, as vezes saio com amigos/familiares'):
        pont_resil = pont_resil + 4
    elif(varTemVidaSocial == 'fraca, raramente saio de casa,sou muito caseiro'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varPraticaMed == 'sim, muito comum'):
        pont_resil = pont_resil + 6
    elif(varPraticaMed == 'médio, talvez, as vezes'):
        pont_resil = pont_resil + 4
    elif(varPraticaMed == 'fraco, raramente'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varPraticaMed == 'sim, muito comum'):
        pont_resil = pont_resil + 6
    elif(varPraticaMed == 'médio, talvez, as vezes'):
        pont_resil = pont_resil + 4
    elif(varPraticaMed == 'fraco, raramente'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varVicio == 'sim, muito comum,praticamente todo dia'):
        pont_resil = pont_resil + 0
    elif(varVicio == 'médio, talvez, não todo dia mas frequente'):
        pont_resil = pont_resil + 3
    elif(varVicio == 'fraco, raramente,esporadicamente'):
        pont_resil = pont_resil + 6
    else:
        pont_resil = pont_resil + 9

    if(varDivideTempo == 'sim, separo um tempo para descansar e um tempo para me divertir'):
        pont_resil = pont_resil + 3
    elif(varDivideTempo == 'médio, talvez, às vezes esqueço de lazer e descanso'):
        pont_resil = pont_resil + 2
    elif(varDivideTempo == 'fraco, raramente tenho vida social ou descanso'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varTiraTempo == 'sim, tenho minhas preferências/hobby'):
        pont_resil = pont_resil + 6
    elif(varTiraTempo == 'eventualmente faço algo só para mim'):
        pont_resil = pont_resil + 4
    elif(varTiraTempo == 'raramente penso só em mim, atividade que eu goste só para mim'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varOtimismo == 'sim, muito comum pensar que as coisas vão mehorar'):
        pont_resil = pont_resil + 6
    elif(varOtimismo == 'médio, talvez, as vezes é dificil ser otimista'):
        pont_resil = pont_resil + 4
    elif(varOtimismo == 'raramente, está bem dificil pensar que as coisas vão melhorar'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varEuMeEntusia == 'sim, muito comum estar motivado'):
        pont_resil = pont_resil + 3
    elif(varEuMeEntusia == 'médio, talvez, nem sempre estou motivado /entusiasmado'):
        pont_resil = pont_resil + 2
    elif(varEuMeEntusia == 'fraco, raramente estou entusiasmado'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varSouAlegre == 'sim, muito comum'):
        pont_resil = pont_resil + 3
    elif(varSouAlegre == 'médio, talvez, as vezes'):
        pont_resil = pont_resil + 2
    elif(varSouAlegre == 'fraco, raramente'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varMeSintoCapaz == 'sim, sinto que sou capaz'):
        pont_resil = pont_resil + 3
    elif(varMeSintoCapaz == 'médio, talvez, as vezes fico inseguro da minha capacidade'):
        pont_resil = pont_resil + 2
    elif(varMeSintoCapaz == 'fraco, raramente confio na minha entrega'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varObs == 'sim, muito comum eu não desisto'):
        pont_resil = pont_resil + 6
    elif(varObs == 'médio, talvez, às vezes desanimo'):
        pont_resil = pont_resil + 4
    elif(varObs == 'fraco, muitas vezes não persisto'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varOrganizado == 'sim, gosto de tudo em ordem e sou focado'):
        pont_resil = pont_resil + 6
    elif(varOrganizado == 'médio, talvez, mas me acho na minha bagunça'):
        pont_resil = pont_resil + 4
    elif(varOrganizado == 'pouco organizado, as vezes perco o foco'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varEq == 'sim, muito comum me manter equilibrado e sereno'):
        pont_resil = pont_resil + 3
    elif(varEq == 'médio, talvez, as vezes perco o controle ou o equilíbrio'):
        pont_resil = pont_resil + 2
    elif(varEq == 'fraco, raramente tenho vida social ou descanso'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varEmGeralReage == 'sim, muito comum'):
        pont_resil = pont_resil + 0
    elif(varEmGeralReage == 'médio, talvez, as vezes'):
        pont_resil = pont_resil + 1
    elif(varEmGeralReage == 'fraco, raramente'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 3

    if(varDesiste == 'sim, muito comum eu desanimar de algum projeto'):
        pont_resil = pont_resil + 0
    elif(varDesiste == 'médio, talvez, as vezes eu desanimo e acho que é melhor desisitir'):
        pont_resil = pont_resil + 2
    elif(varDesiste == 'raramente eu desisto ou dou o braço a torcer, eu persisto'):
        pont_resil = pont_resil + 4
    else:
        pont_resil = pont_resil + 6

    if(varConsegueVer == 'sim, tenho visão clara da situação,sou pragmatico'):
        pont_resil = pont_resil + 6
    elif(varConsegueVer == 'médio, talvez, as vezes demoro a entender a situação'):
        pont_resil = pont_resil + 4
    elif(varConsegueVer == 'fraco, é comum sob pressão eu ter dificuldade de entender a situação e sair dela'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varConsegueCeder == 'sim, sou uma pessoa bastante flexivel e adaptavel'):
        pont_resil = pont_resil + 3
    elif(varConsegueCeder == 'médio, talvez, as vezes cedo e sou flexível mas nem sempre'):
        pont_resil = pont_resil + 2
    elif(varConsegueCeder == 'sou mais resistente a mudanças, em geral resisto'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varPensaMuito == 'sim, muito comum pensar mais nos outros que em mim'):
        pont_resil = pont_resil + 3
    elif(varPensaMuito == 'médio, talvez, as vezes penso demais nos outros'):
        pont_resil = pont_resil + 2
    elif(varPensaMuito == 'raramente, em geral penso em mim e na familia primeiro e depois ajudo quando posso'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varReconhece == 'sim, muito comum'):
        pont_resil = pont_resil + 3
    elif(varReconhece == 'médio, talvez, as vezes'):
        pont_resil = pont_resil + 2
    elif(varReconhece == 'fraco, raramente'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varDianteCrise == 'sim, muito comum procurar alternativas'):
        pont_resil = pont_resil + 6
    elif(varDianteCrise == 'médio, talvez, as vezes tento buscar ajuda e soluções'):
        pont_resil = pont_resil + 4
    elif(varDianteCrise == 'fraco, raramente eu tomo a frente para soluções,sou mais de apoiar'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varSenteForca == 'sim, muito comum me chamarem de guerreiro(a)'):
        pont_resil = pont_resil + 6
    elif(varSenteForca == 'médio, talvez, as vezes surpreendo e me mostro forte'):
        pont_resil = pont_resil + 4
    elif(varSenteForca == 'fraco, raramente sou de lutar e brigar pelas coisas'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varCapazPerdoar == 'sim, muito comum'):
        pont_resil = pont_resil + 6
    elif(varCapazPerdoar == 'médio, talvez, as vezes é dificil'):
        pont_resil = pont_resil + 4
    elif(varCapazPerdoar == 'fraco, raramente eu perdoo,sou um pouco rancoroso (a)'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varPossuiForcaEsp == 'sim, tenho uma crença/ vivencia espiritual frequente'):
        pont_resil = pont_resil + 3
    elif(varPossuiForcaEsp == 'eventualmente tenho vivência na religião/atividade espiritualista'):
        pont_resil = pont_resil + 2
    elif(varPossuiForcaEsp == 'raramente tenho vivencia espiritual ou frequento alguma religião'):
        pont_resil = pont_resil + 2
    elif(varPossuiForcaEsp == 'não, nada/pouco (somente através de companheiros/parentes)'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    if(varAcredita == 'sim, tenho uma boa rede de amigos/familiares proxima'):
        pont_resil = pont_resil + 9
    elif(varAcredita == 'sim, tenho bons amigos/familiares mais nem sempre estou com eles'):
        pont_resil = pont_resil + 6
    elif(varAcredita == 'não tenho muitos amigos e quase nunca/nunca conto com eles'):
        pont_resil = pont_resil + 3
    else:
        pont_resil = pont_resil + 0

    if(varViveBem == 'sim, muito comum'):
        pont_resil = pont_resil + 6
    elif(varViveBem == 'médio, talvez, as vezes'):
        pont_resil = pont_resil + 4
    elif(varViveBem == 'fraco, raramente'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varSenteRealiza == 'sim, muito satisfeito'):
        pont_resil = pont_resil + 6
    elif(varSenteRealiza == 'médio, talvez, as vezes penso que deveria fazer outra coisa'):
        pont_resil = pont_resil + 4
    elif(varSenteRealiza == 'não, nada/pouco penso muito em fazer outra coisa'):
        pont_resil = pont_resil + 2
    else:
        pont_resil = pont_resil + 0

    if(varSabeReal == 'sim, sei para onde quero ir'):
        pont_resil = pont_resil + 3
    elif(varSabeReal == 'médio, talvez, as vezes me sinto no piloto automatico'):
        pont_resil = pont_resil + 2
    elif(varSabeReal == 'fraco, não penso muito em para onde ir, vou vivendo'):
        pont_resil = pont_resil + 1
    else:
        pont_resil = pont_resil + 0

    return pont_resil

def calc_suggestions_resili(pont_resili):
    pont_resili_str = ''
    sug_resili = ''
    if(pont_resili <= 65):
        pont_resili_str = "Resiliência baixíssima"
        sug_resili = "Resiliência Baixissima - Recomendamos urgentemente treinamento de positividade ,autocuidado e aumento de resiliência para melhorar capacidade de reagir aos desafios da vida."
    elif(pont_resili<=101):
        pont_resili_str = "Resiliência comprometida"
        sug_resili = "Resiliência Comprometida - Sugerimos ações de positividade, autocuidado e desenvolvimento humano para melhorar padrões de resposta aos desafios da vida cotidiana."
    elif(pont_resili <=143):
        pont_resili_str = "Resiliência mediana"
        sug_resili = "Resiliência Mediana/Satisfatória - Muito bem, vc tem recursos de reação e sobreivencia. Recomendamos reforçar rede de apoio,atividades sociais e práticas meditativas e de autoconhecimento para estar cada vez melhorl"
    else:
        pont_resili_str = "Resiliência alta"
        sug_resili = "Resiliência ALTA - Parabéns , você demonstra ter recursos próprios para enfrentar as interferências da vida."

    return pont_resili_str, sug_resili

def index(request):
    
    image_url = 'https://raw.githubusercontent.com/estevanrlima/bgtreinamentos/main/logo%20BG%20treinamentos.png'

    if request.method == 'POST':
        user_email = request.POST['userEmail']

        if(request.POST['formName'] == 'hadForm'):

            pont_ans, pont_dep = calc_had(request)
            pont_ans_str, pont_dep_str, sug_ans, sug_dep = cal_suggestions_had(pont_ans, pont_dep)

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

        elif(request.POST['formName'] == 'resiliForm'):
            pont_resili = calc_resili(request)
            pont_resili_str, sug_resili = calc_suggestions_resili(pont_resili)

            subject = 'Devolutiva - BG Saúde - Resiliteste'
            html_content = render_to_string('home/resili_template.html', {
                'pont_resili_str': pont_resili_str,
                'sug_resili': sug_resili,
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
        else:
            pass
        

        

    return render(request, 'home/index.html')