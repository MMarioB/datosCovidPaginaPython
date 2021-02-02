import requests
from bs4 import BeautifulSoup

url = "https://www.elmundo.es/espana/2020/10/09/5f7f9b71fc6c83bf318b4690.html"
req = requests.get(url)
source = req.text
soup = BeautifulSoup(source, "html.parser")
titulos = soup.find_all('ul', {'class': 'ue-c-article_list ue-c-article_list--unordered'})
for titulo in titulos:
    datos = titulo.text
    fin = datos.split(")", 20)
    lista = []
    for a in fin:
        lista.append(a)

print(lista[0].split(";")[0].split(": ")[1] + ":")
print(lista[0].split(";")[0].split(": ")[2])
print(" - " + lista[0].split(";")[1].split("e.")[1] + ")")
print(" - " + lista[1] + ")")
print(" - " + lista[2] + " muertos)")
print(" - " + lista[3] + ")")
print(" - " + lista[4].strip() + ")")
print(" - " + lista[5] + ")")
print(" - " + lista[6] + ")")
print(" - " + lista[7].strip() + ")")
print(" - " + lista[8] + ")")
print(" - " + lista[9] + ")")
print(" - " + lista[10] + ")")
print(" - " + lista[11].split("s ")[0] + "s" + " (" + lista[11].split("s ")[1] + " muertos)")
print(" - " + lista[12].strip() + ")")
print(" - " + lista[13] + ")")
print(" - " + lista[14] + ")")
print(" - " + lista[15] + ")")
print(" - " + lista[16] + ")")
print(" - " + lista[17] + ")")
print(" - " + lista[18] + ")")
