import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r=requests.get("https://fiis.com.br/hctr11/",headers=headers)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, "html.parser")
linha_tabela = soup.find_all("div","yieldChart__table__bloco")


for linha in linha_tabela:    
    valores = linha.find_all("div")
    linha=""
    for valor in valores:
        linha+=(valor.text.replace('\r', '').replace('\n', '').replace(' ', ''))+" | "
    print(linha)

##print(len(result))