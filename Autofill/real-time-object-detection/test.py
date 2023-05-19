import os.path
import cv2
import easyocr
from fuzzywuzzy import fuzz
from PIL import Image


# ввод данных и выбор библиотеки для распознавания
def main():
    Eto_ID = False
    path_img = r'C:\Users\abdul\Documents\.Prog\Coursework\images\test1.jpg'
    # распознавание с помощью easyocr, параметры: отключена детализация вывода,
    # включены параграфы и установлена точность текста
    # text = easyocr.Reader(["ru", "en"]).readtext(path_img, detail=0, paragraph=False, text_threshold=0.8)
    text = ['КЫРГЫЗ РЕСПУБЛИКАСЫ', 'КЫРГЫЗСКАЯ РЕСПУБЛИКА', 'THE KI2?GVZ RECUSLIC', 'ИДЕНТИФИКАЦИЯЛЫК КАРТА', 'ИДЕНТИФИКАЦИОННАЯ КАРТА', '[DENTITY CARD', 'Фамилиясы', 'Фамилия / Surname', 'ГАЙНАЗАРОВ', 'GAINAZAROV', 'Аты', 'Имя', 'Name', 'АБДУЛАЗИЗБЕК', 'ABDULAZIZBEK', 'Атасынын аты', 'Отчество', 'Patronyn €', 'МАМАНАЗАРОВИЧ', 'Жынысы', 'Пол', 'Sex', 'Э/M', 'Жесандыгы' '/ Гражданство', 'Natimna)', 'КЫРГЫЗ РЕСПУБЛИКАСЫ', 'Туулgsdfsdfгэн куsу', 'Дага рожденяя', 'Dзte с- 3rnc', 'Дскументия N', '28.06.2005', '~учечта', 'Ужuле ', 'Подпись / Sigrature', '1D2543559', 'Коrzc-ty чээтэту', 'Ск дсистани', 'Эзiе % ехcку', '22.12.2031', 'Колу']

    ID_CARD = ['ИДЕНТИФИКАЦИЯЛЫК КАРТА', 'ИДЕНТИФИКАЦИОННАЯ КАРТА', 'IDENTITY CARD']

    # Check if it is ID Card
    for i in ID_CARD:
        for s in text:
            if fuzz.ratio(i, s) > 50 or i == s:
                Eto_ID = True
    if Eto_ID:
        print(text)
    ncount = 0
    bcount = 0
    Surname = ['Фамилиясы /', '/ Фамилия /', '/ Surname']
    Name = ['Аты /', '/ Имя /', '/ Name']
    Patronymic = ['Атасынын аты /', '/ Отчество /', '/ Patronymic']
    Sex = ['Жынысы /', '/ Пол /', '/ Sex']
    Nationality = ['Жарандыгы', '/ Гражданство /', '/ Nationality']
    Birthdate = ['Туулган куну /', '/ Дата рождения /', '/ Date of birth']
    Document = ['Документтин /', '/ документа /', '/ Document']
    Expirition = ['Колдонуу мооноту', 'Срок действия', '/ Date of expiry']
    
  
    for i in Surname:
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Eng_Surname_id = text.index(s) + 2
                Rus_Surname_id = text.index(s) + 1
                Surname = [text[Eng_Surname_id], text[Rus_Surname_id]]
                break
            
    for i in Name:
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Eng_Name_id = text.index(s) + 2
                Rus_Name_id = text.index(s) + 1
                Name = [text[Eng_Name_id], text[Rus_Name_id]]
            
    for i in Patronymic:
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Rus_Patronymic_id = text.index(s) + 1
                Patronymic = text[Rus_Patronymic_id]
            
    for i in Sex:
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Sex_id = text.index(s) + 2
                preSex = text[Sex_id]
                if preSex == 'M':
                    Sex = 'Э/М'
                else:
                    Sex = 'К/Ж'
            
    for i in Nationality:
        ncount += 1
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Nationality_id = text.index(s) + 4 - ncount
                Nationality = text[Nationality_id]
            
    for i in Birthdate:
        bcount += 1
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Birthdate_id = text.index(s) + 5 - bcount
                Birthdate = text[Birthdate_id]
            
    for i in Document:
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Document_id = text.index(s) + 1
                Document = text[Document_id]
    
    for i in Expirition:    
        for s in text:
            if fuzz.ratio(i, s) > 60:
                Expirition_id = text.index(s) + 1
                Expirition = text[Expirition_id]


    print('Surname: ', Surname) 
    print('Name:', Name)   
    print('Patronymic: ',Patronymic)
    print('Sex: ', Sex)
    print('Nationality: ', Nationality)
    print('Birthdate: ', Birthdate)
    print('Document: ', Document)
    print('Expirition: ', Expirition)
main()