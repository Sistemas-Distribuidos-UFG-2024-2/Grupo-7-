#Problemas de Programação 2
#Questão 2 - Crwaler(robot)
#Grupo 7
#-------------------------
#Crawler com profundidade 2, podendo ser alterada mudando a variável "profundidade_maxima"
#O crawler irá começar por uma URL inicial "url_inicial", podendo ser alterada para qualquer site
#e colherá todos os links dentro desse site. Após, irá entrar em cada um, aumentando em +1 o nível de profundidade
#Ao chegar no máximo de profundidade ou acabar os links na página, o programa se encerra

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def crawler(url_inicial, profundidade_maxima=2):
    visitados = set()  
    fila = [(url_inicial, 0)]  #urls já visitadas

    while fila:
        url_atual, profundidade = fila.pop(0)

        if url_atual in visitados or profundidade > profundidade_maxima:
            continue

        print(f"Visitando: {url_atual} (Profundidade: {profundidade})")
        visitados.add(url_atual)

        try:        # faz a reuqisição htt´
            resposta = requests.get(url_atual, timeout=5)#=
            if resposta.status_code != 200:
                print(f"Erro ao acessar {url_atual}: {resposta.status_code}")
                continue

            soup = BeautifulSoup(resposta.text, 'html.parser') # analisa a pagina

            # pega os links
            for tag in soup.find_all('a', href=True):
                link = urljoin(url_atual, tag['href'])  
                if link not in visitados:
                    fila.append((link, profundidade + 1))
            
            time.sleep(0.5)  

        except Exception as e:
            print(f"Erro ao processar {url_atual}: {e}")

if __name__ == "__main__":
    url_inicial = "https://turing.inf.ufg.br" # url inicial
    crawler(url_inicial, profundidade_maxima=2)
