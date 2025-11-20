import sys
try:
    import whois
except:
    sys.exit()

while True:
    print("Coloque o site ou digite sair para fecha a busca")
    print("=======================================")
    dominio = input("Digite o site para buscar dados Whois:")
    
    if dominio.lower() == "sair":
        print("Saindo do buscador de dados Whois...")
        break
    
    try:
        consultawhois = whois.whois(dominio)
    except Exception as e:
        print(f"Erro ao consultar WHOIS: {e}")
        continue

    print (consultawhois.email)
    # print (consultawhois["email"])

    print (consultawhois.text)
