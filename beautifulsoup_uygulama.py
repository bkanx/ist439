import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from coloroma import  init, Fore, Style
init(autoreset=True)



#https://dergipark.org.tr/tr/pub/sdufenbed/aarticle/1073504

headers =
"User-Agent" : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
url1 ="https://dergipark.org.tr/tr/pub/sdufenbed/article/107354"
url2 ="https://akademik.eskisehir.edu.tr/bkan/makaleler"


#print("İçerik Özeti:" , response.text)
def get_data(url1):
    r=requests.get(url1, headers=headers)
    soup_obj=BeautifulSoup(r.content, "lxml")
    return soup_obj
#başlık çekme
soup =get_data(url1)
baslik= soup.find("h3").text.strip()
#print("Article Title:" , baslik)

#künye bilgisi
alt_bilgi=soup.find("span" , class_ = "article-subtitle").text.strip()
#print("---Künye Bilgisi---" , alt_bilgi)

#pdf linki
pdf_butonu=soup.find("a" , class_="pdf")
pdf_linki =pdf_butonu.get("href")
if pdf_linki.startswith("/"):
    pdf_linki="https://dergipark.org.tr"+pdf_linki
#print("PDF Linki" , pdf_linki)

#Renklendirme
print(Fore.CYAN + "="*50)
print(Fore.GREEN +"MAKALE ADI :" +Style.RESET_ALL + baslik)
print(Fore.YELLOW + "BİLGİLER :" alt_bilgi)
print(Fore.MAGENTA + "PDF LİNKİ:" +Style.BRIGHT + pdf_linki )
print(Fore.CYAN + "="*50)

#Kaynakça
kaynakca_alani=soup.find("div" , class_= "article-citations")
if kaynakca_alani:
    kaynaklar= (
         kaynakca_alani.find.all("li"))

    for i, kaynak in enumerate(kaynaklar , 1):

        print(Fore.WHITE +f"{i}".{kaynak.text.strip()}")
else:
        print(Fore.RED +"Kaynakça bulunamadı.")
 print(Fore.CYAN + "="*50)

import  pandas as pd
from datetime import datetime
#Verilerin liste haline getirilmesi
makale_verisi =[{
    "Makale Başlığı": baslik,
    "Künye": alt_bilgi,
    "PDF Adresi":pdf_linki
    "İşlem Tarihi":datetime.now().strftime("%d-%m-%Y %H:%M")
}]
#tablo oluşturulması
df =pd.DataFrame(makale_verisi)

#Excel olarak kaydetme
df.to_excel("Makale_Listesi.xlsx" , index=False)
print(Fore.LIGHTGREEN_EX +"\n BAŞARILI: Veriler Excel dosyasına kaydedildi.")