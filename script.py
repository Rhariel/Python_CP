# Grupo: Nivellus
# Alunos: Rhariel 1 (566310), Bruna Sadi Duarte (561870), Sara Marangon de Macedo (563807)

# Função que garante que o valor inserido é um número positivo válido
def obter_valor(texto):
    while True:
        entrada = input(texto)
        valido = True
        ponto = 0

        for caractere in entrada:
            if caractere == ".":
                ponto += 1
                if ponto > 1:
                    valido = False
                    break
            elif caractere not in "0123456789":
                valido = False
                break

        if not valido or entrada == "":
            print("Entrada inválida. Digite apenas números (ex: 2.5).")
            continue

        numero = float(entrada)
        if numero < 0:
            print("Digite um número positivo.")
            continue

        return numero

# Verifica e exibe alertas por medição individual
def verificar_medição(valor):
    if valor >= 4.0:
        print("🚨 ALERTA: medição em nível crítico!")
    elif valor >= 3.5:
        print("⚠️ Atenção: medição próxima de enchente!")

# Determina o status do dia com base na média e na última medição
def verificar_status_dia(media, ultima_medida):
    global dias_com_risco
    global dias_nivel_baixo

    if ultima_medida >= 4.0:
        print("🚨 ALERTA: Última medição do dia em nível crítico!")
        dias_com_risco += 1
    elif ultima_medida >= 3.5:
        print("⚠️ Última medição do dia próxima de enchente!")

    if media > 4.0:
        print("🚨 Status: ENCHENTE em andamento!\n")
        dias_com_risco += 1
    elif media >= 3.5:
        print("⚠️ Status: Nível MUITO ALTO – risco iminente de enchente!\n")
        dias_com_risco += 1
    elif media >= 2.0:
        print("Status: Nível normal\n")
    else:
        print("Status: Rio muito baixo – risco de seca\n")
        dias_nivel_baixo += 1

# Função que executa o monitoramento de 1 dia (3 medições)
def monitorar_dia(numero_do_dia):
    global maior_nivel
    medições_dia = []

    print(f"\n🗓️ Dia {numero_do_dia} – Insira 3 medições:")
    medida = 1

    while medida <= 3:
        valor = obter_valor(f"  📏 Medição {medida}: ")

        if valor > maior_nivel:
            maior_nivel = valor

        verificar_medição(valor)
        medições_dia.append(valor)
        medida += 1

    media = sum(medições_dia) / 3
    medias_dias.append(media)

    print(f"\n📊 Média do Dia {numero_do_dia}: {media:.2f}m")
    verificar_status_dia(media, medições_dia[2])

# Executa um período (10 dias)
def executar_periodo(numero_periodo):
    global dias_com_risco
    global dias_nivel_baixo
    global maior_nivel
    global medias_dias

    dias_com_risco = 0
    dias_nivel_baixo = 0
    maior_nivel = 0
    medias_dias = []

    print("\n" + "="*50)
    print(f"🌦️ INÍCIO DO PERÍODO {numero_periodo}".center(50))
    print("="*50)

    for dia in range(1, 11):
        print("\n" + "-"*50)
        monitorar_dia(dia)
        print("-"*50)

    titulo = "📋 RELATÓRIO DO PERÍODO"
    print("\n" + "=" * ((60 - len(titulo)) // 2) + f" {titulo} " + "=" * ((60 - len(titulo)) // 2))
    print(f"🔴 Dias com risco de enchente: {dias_com_risco}")
    print(f"🔵 Dias com nível muito baixo: {dias_nivel_baixo}")
    print(f"📈 Maior nível registrado: {maior_nivel:.2f}m")
    print("\n📅 Médias dos 10 dias:")
    for i in range(10):
        print(f"  Dia {i+1}: {medias_dias[i]:.2f}m")
    print("="*50)

    return dias_com_risco, dias_nivel_baixo, maior_nivel, sum(medias_dias) / 10

# Mostra o relatório geral acumulado a cada 3 períodos
def mostrar_relatorio_geral(risco_total, baixo_total, pico_total, medias_gerais):
    print("\n" + "="*60)
    print("📊 RELATÓRIO GERAL DOS 3 PERÍODOS".center(60))
    print("="*60)
    print(f"🔴 Total de dias com risco: {risco_total}")
    print(f"🔵 Total de dias com nível muito baixo: {baixo_total}")
    print(f"📈 Maior nível registrado no período total: {pico_total:.2f}m")
    print(f"\n📌 Média geral por período:")
    for i in range(3):
        print(f"  Período {i+1}: {medias_gerais[i]:.2f}m")
    print("="*60)

# Pergunta se o usuário quer iniciar mais 3 períodos
def menu_repeticao():
    while True:
        repetir = input("🔁 Deseja monitorar mais 3 períodos? (s/n): ")
        if repetir == "s":
            return True
        elif repetir == "n":
            print("👋 Encerrando o sistema. Até a próxima!")
            return False
        else:
            print("❌ Resposta inválida. Digite 's' ou 'n'.")

# Execução principal
while True:
    risco_total = 0
    baixo_total = 0
    pico_total = 0
    medias_gerais = []

    for periodo in range(1, 4):
        risco, baixo, pico, media = executar_periodo(periodo)
        risco_total += risco
        baixo_total += baixo
        if pico > pico_total:
            pico_total = pico
        medias_gerais.append(media)

    mostrar_relatorio_geral(risco_total, baixo_total, pico_total, medias_gerais)

    if not menu_repeticao():
        break
