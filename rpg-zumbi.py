from time import sleep

def typewriter(frase):
  for letra in frase:
    print(letra, end="")
    sleep(0.025)
  print()
  sleep(2)

def comeco():
  typewriter('Você acorda de um coma e percebe que todos a sua volta são zumbis, oque você deve fazer?')
  typewriter('1- Procurar ajuda no hospital')
  typewriter('2- Sair do hospital')
  resp = input('R: ')

  if resp == '1':
    typewriter('Procurando por ajuda no hospital, você vai para a saída de emergência e encontra um helicóptero')
    typewriter('Ao ver o helicóptero você se lembra que nunca pilotou um, você se arrisca a tentar?')
    typewriter ('1- Sim')
    typewriter ('2- Não')
    resp = input('R: ')

    if resp == '1':
      fuga()
    elif resp == '2':
      typewriter('Como você nunca pilotou um helicóptero na vida, você acha uma perda de tempo tentar agora')
      saida()

  elif resp == '2':
    saida()

def fuga():
  typewriter('Você entra no helicóptero, consegue ligar porém não consegue pilotar pois não tem conhecimento. O barulho da hélice acaba atraindo alguns zumbis para as escadas da saída de emergência e agora você está cercado. Ao olhar para a parte de trás do helicóptero você vê uma pistola e algumas munições, o que você decide fazer?')
  typewriter('1- Sair do helicóptero e atirar nos zumbis')
  typewriter('2- Continuar tentando pilotar o helicóptero')
  resp = input('R: ')
        
  if resp == '1':
    typewriter('Você pega as munições, recarrega a pistola, sai do helícoptero e atira em todos os zumbis que estão ali, acabando com todos eles. E agora?')
    typewriter('1- Você volta para o helicóptero para tentar pilotá-lo novamente')
    typewriter('2- Desiste de tentar fugir com o helicóptero e sai correndo para fora do hospital')
    resp = input('R: ')

    if resp == '1':
      helicoptero()

    elif resp == '2':
      saida()
    
  elif resp == '2':
    helicoptero()

def helicoptero():
  typewriter('Depois de um bom tempo tentando pilotar o helicóptero você consegue fazer ele sair do chão. Depois de pegar o jeito com o helicóptero e ir pilotando por aí enquanto pensa no que fazer, você consegue ver, mesmo que seja de longe, uma área bem grande com casas, carros e aviões com pintura estilo "camuflado", o que aparenta ser uma base militar. Acha uma boa idéia ir até lá?')
  typewriter('1- Sim')
  typewriter('2- Não')
  resp = input('R: ')

  if resp == '1':
    typewriter('Você decide ir até a tal base militar, tentando chamar atenção das pessoas que estão ali para poder ter autorização para pousar. Num curto período de tempo, muitas pessoas aparecem ali em baixo com um uniforme de estampa com tons de verde e marrom, o que confirma sua teoria de que ali é mesmo uma base militar. Ao pousar você é recebido por dois homens que lhe perguntam algumas coisas relacionadas a você e como veio parar aqui. Depois de contar sua história aos dois homens eles lhe oferecem duas propostas:')
    typewriter('A primeira é recomeçar sua vida ali no exército com eles, ajudando tanto nas vida de outras pessoas como em futuras guerras, ou a segunda que é aceitar o carro que eles lhe ofereceram e também um pouco de gasolina para você continuar dirigindo por aí. E aí? O que você prefere?')
    typewriter('1- A primeira proposta')
    typewriter('2- A segunda proposta')
    resp = input('R: ')
        
    if resp == '1':
      typewriter('Você perebe que não tem muito o que fazer a não ser ficar pilotando por aí sem rumo, então decide se juntar aos militares e ajudando outras pessoas que precisam de ajuda e as que vão precisar futuramente. Fim')
      
    elif resp == '2':
      typewriter('Você pega o carro e a gasolina necessária para a viagem e decide ir até a sua casa tentar rever sua família')
      casa()
    
  elif resp == '2':
    typewriter('Você acha arriscado ir até a tal base militar e desvia o caminho. Após um bom tempo pilotando e sem encontrar nada, o helicóptero começa a fazer uns barulhos estranhos e uma luz vermelha começa a piscar no painel. Você prefere pousar o helicóptero ou ignorar os barulhos e a luz e continuar pilotando?')
    typewriter('1- Pousar o helicóptero')
    typewriter('2- Ignorar e continuar pilotando')
    resp = input('R: ')
              
    if resp == '1':
      typewriter('Por mais que você não seja experiente em pilotar helicópteros, você sabe que esses barulhos e essa luz vermelha piscando não significa boa coisa, entâo decide fazer um pouso de emergência. Ao abandonar o helicóptero e andar alguns metros você vê uma casa. Você corre até lá, bate na porta mas ninguém atende, entâo você decide entrar mesmo assim. Entrando na casa você percebe que ela está vazia e um barulho estranho começa a vim de uma das portas da casa. O que fazer agora?')
      typewriter('1- Ir até a tal porta e ver o que é')
      typewriter('2- Sair da casa o mais rápido possível')
      resp = input('R: ')
                  
      if resp == '1':
        typewriter('Ao abrir a porta na esperança de ser alguém, você é surpreendido por vários zumbis. Você até tenta fugir mas nâo consegue e é devorado por eles. Fim')
                  
      elif resp == '2':
        typewriter('Assustado com o barulho, você sai correndo daquela casa e sem rumo. Correndo sem prestar muita atenção nos lugares, você acabar entrando numa floresta e dando de cara com um zumbi. Você tenta correr mas seus passos chamam a atenção de outros zumbis que acabam te cercando e te devorando. Fim')

    elif resp == '2':
      typewriter('Você decide ignorar a luz e os barulhos porém 5 minutos depois ele para de fazer barulho, a luz apaga e o helicoptero começa a cair. Com a forte batida do helicoptero ao chão, ele pega fogo e você acaba morrendo dentro dele. Fim')
     
def saida():
  typewriter ('Você decide sair desesperado do hospital e acaba encontrando um carro')              
  typewriter('Ao entrar no carro você percebe que ele está sem gasolina, você faz o que?')
  typewriter('1- Você vai até o posto de gasolina')
  typewriter('2- Você sai a procura de outro veículo')
  resp = input('R: ')
  
  if resp == '1':
    typewriter('Ao chegar no posto de gasolina você consegue abastecer o veículo, agora o que você decide fazer?')
    typewriter('1- Ir na sua casa para tentar rever sua família')
    typewriter('2- Dirigir por aí até encontrar outras pessoas')
    resp = input('R: ')
        
    if resp == '1':
      casa()
    
    elif resp == '2':
      typewriter('Após pegar o carro, você encontra um grande muro com vários prédios bem altos, deseja ir até lá?')
      typewriter('1- Sim')
      typewriter('2- Não')
      resp = input('R: ')
      
      if resp == '1':
        typewriter('Você sai do carro, caminha um pouco até o lugar e bate no portão, uma moça atende você mas te puxa para dentro do lugar, segundo ela, aí fora é muito perigoso. Ao entrar no lugar você vê muitas outras pessoas, tanto crianças, adultos e idosos, a moça te explica que aqui se tornou um alojamento para a segurança de todos os humanos que ainda existem na cidade. Você chega a conclusão que a melhor opção para você é ficar aqui, mas antes de qualquer coisa, o que você pretende fazer?')
        typewriter('1- Perguntar para a moça se sua família está aqui')
        typewriter('2- Explorar o local')
        resp = input('R: ')
        
        if resp == '1':
          typewriter('Você fala da sua família para a moça e ela te leva até a "recepção" do lugar para ver se sua família está aqui. Depois de um tempo procurando, você é chamado para ser levado a um quarto do alojamento onde, ao abrir a porta, encontra sua esposa e seus filhos. Fim')
        
        elif resp == '2':
          typewriter('Depois de tanto andar pelo local, a moça finaliza a "exploração" do local lhe mostrando o prédio onde fica os quartos, ao entrarem num corredor você ouve uma voz familiar e decide bater na porta do tal quarto, onde sai de lá uma mulher com duas crianças. Ao olhar para o rosto da mulher e das crianças reconhece que é a sua família. Fim')
      
      elif resp == '2':
        typewriter('Você pensa um pouco e decide não ir no tal lugar. Depois de dirigir muito e não encontrar nada além de árvores, estradas e zumbis, a gasolina acaba. O que fazer agora?')
        typewriter('1- Largar o carro e andar por aí até achar algum lugar')
        typewriter('2- Ficar no carro na esperança e encontrar alguém')
        resp = input('R: ')
        
        if resp == '1':
          typewriter('Você caminha bastante pela área na esperança de encontrar algum lugar porém sem sucesso. Quanto mais você anda mais fraco fica, porque você não come e bebe nada a um bom tempo, você entra na floresta tentando encontrar algo pra comer mas acaba encontrando zumbis, que atacam você. Fim')
        
        elif resp == '2':
          typewriter('Depois de tanto tempo ficando dentro do carro, sem ninguém passar pelas ruas, você vai ficando cada vez mais fraco e morrendo de fome. Fim')
    
  elif resp == '2':
    typewriter('Você vai procurar outro veículo mas acaba sendo cercado pelos zumbis e devorado por eles. FIM')

def casa():
  typewriter('Ao chegar na sua casa você vê que não tem ninguém e que a casa está bem empoeirada e suja, e acaba chegando a conclusão que sua família já não está mais aqui a um bom tempo ou que estão mortos')
  typewriter('O que fazer agora?')
  typewriter('1- Ficar em casa')
  typewriter('2- Pegar o carro e dirigir por aí até encontrar outras pessoas')
  resp = input('R: ')
    
  if resp == '1':
    typewriter('Você optou por ficar na sua casa mesmo e continuar sua vida por ali, na esperança de tudo isso acabar e você recomeçar sua vida. FIM')
    
  elif resp == '2':
    typewriter('Após pegar o carro, você encontra um grande muro com vários prédios bem altos, deseja ir até lá?')
    typewriter('1- Sim')
    typewriter('2- Não') 
    resp = input('R: ')
    
    if resp == '1':
      typewriter('Você sai do carro, caminha um pouco até o lugar e bate no portão, uma moça atende você mas te puxa para dentro do lugar, segundo ela, aí fora é muito perigoso. Ao entrar no lugar você vê muitas outras pessoas, tanto crianças, adultos e idosos, a moça te explica que aqui se tornou um alojamento para a segurança de todos os humanos que ainda existem na cidade. Você chega a conclusão que a melhor opção para você é ficar aqui, mas antes de qualquer coisa, o que você pretende fazer?')
      typewriter('1- Perguntar para a moça se sua família está aqui')
      typewriter('2- Explorar o local')
      resp = input('R: ')
      
      if resp == '1':
        typewriter('Você fala da sua família para a moça e ela te leva até a "recepção" do lugar para ver se sua família está aqui. Depois de um tempo procurando, você é chamado para ser levado a um quarto do alojamento onde, ao abrir a porta, encontra sua esposa e seus filhos. Fim')
      
      elif resp == '2':
        typewriter('Depois de tanto andar pelo local, a moça finaliza a "exploração" do local lhe mostrando o prédio onde fica os quartos, ao entrarem num corredor você ouve uma voz familiar e decide bater na porta do tal quarto, onde sai de lá uma mulher com duas crianças. Ao olhar para o rosto da mulher e das crianças reconhece que é a sua família. Fim')
        
    elif resp == '2':
      typewriter('Você pensa um pouco e decide não ir no tal lugar. Depois de dirigir muito e não encontrar nada além de árvores, estradas e zumbis, a gasolina acaba. O que fazer agora?')
      typewriter('1- Largar o carro e andar por aí até achar algum lugar')
      typewriter('2- Ficar no carro na esperança e encontrar alguém')
      resp = input('R: ')
      
      if resp == '1':
        typewriter('Você caminha bastante pela área na esperança de encontrar algum lugar porém sem sucesso. Quanto mais você anda mais fraco fica, porque você não come e bebe nada a um bom tempo, você entra na floresta tentando encontrar algo pra comer mas acaba encontrando zumbis, que atacam você. Fim')
      
      elif resp == '2':
        typewriter('Depois de tanto tempo ficando dentro do carro, sem ninguém passar pelas ruas, você vai ficando cada vez mais fraco e morrendo de fome. Fim')

comeco()