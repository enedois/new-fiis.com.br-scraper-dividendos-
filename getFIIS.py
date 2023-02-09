import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def getpapel(papel_):
    try:
                    url = "https://fiis.com.br/"                    
                    r=requests.get("https://fiis.com.br/hctr11/",headers=headers)                    
                    ##print(html)
                    soup = BeautifulSoup(r.content, "html.parser")
                    linha_tabela = soup.find_all("div","yieldChart__table__bloco")
                    for linha in linha_tabela:    
                        valores = linha.find_all("div")
                        linha=""
                        linha+=papel_+" | "
                        for valor in valores:
                            linha+=(valor.text.replace('\r', '').replace('\n', '').replace(' ', ''))+" | "
                        print(linha)                      
                                                                
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO:",papel_, str(e))
        papeis.remove(papel_)   

papeis = []

with open("fiinfra.csv", "r") as file:
    for line in file:
        ##print(line)
        line_data = line.strip().split(";")
        for tick in line_data:
              papeis.append(tick)

for papel in papeis:
      getpapel(papel)





        
