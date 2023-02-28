import tkinter as tk
from tkinter import *
import speech_recognition as sr
import time
from num2words import num2words
def calc(Text):
    print(Text) #числа
    Cifri = {'ноль': 0,'одну': 1, 'один': 1, 'одна': 1, 'два': 2, 'две': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
             'семь': 7, 'восемь': 8, 'девять': 9,
             'десять': 10, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60,
             'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90,
             'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600,
             'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900,
             'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
             'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19}
    sorted_dict = {}
    sorted_keys = sorted(Cifri, key=Cifri.get, reverse=True)  # [1, 3, 2]
    for w in sorted_keys:
        sorted_dict[w] = Cifri[w]

    tis = ['тысяча', 'тысяч', 'тысячи']
    des = {'десятых': 0.1, 'десятые': 0.1, 'десятая': 0.1,'десятую': 0.1, 'сотых': 0.01,'сотую': 0.01, 'сотые': 0.01, 'сотая': 0.01,
           'тысячные': 0.001, 'тысячных': 0.001, 'тысячная': 0.001, 'тысячную': 0.001}
    znaki = {'плюс': '+', 'минус': '-', 'умножить': '*', 'разделить': '/'}
    B1 = ['a', 'десятая', 'сотая', 'тысячная']
    B = ['a','десятых','сотых','тысячных']
    okon = 0
    q = 0
    R2 = 0
    R1 = 0
    sk = 0
    k = 0
    k1 = 0
    Text1 = ''
    Text2 = []
    Text3 = ''
    for i in Text: #создание массива из введенных слов
        if i.isalpha():
            Text1+=i
        elif i == ' ' and Text1 !='':
            Text2.append(Text1)
            Text1 = ''
    if Text1 != '': #добавление последнего числа
        Text2.append(Text1)
    for i in Text2: #удаление лишних слов
        if i == 'на':
            Text2.remove(i)
        elif i == 'целых':
            Text2.remove(i)
        elif i == 'целая':
            Text2.remove(i)
    for i in Text2: #преобразование текстовых цифр в обычные
        k1 += 1
        if i == 'и':
            q = 1
            continue
        if i in Cifri or i in tis or i in des:
            if q == 1:
                if i in des:
                    R2 *= des[i]
                    R1 += R2
                    q = 0
                    if i == Text2[len(Text2) - 1] and k1 == len(Text2):
                        Text3 += str(R1)
                    continue
                R2 += Cifri[i]
                k += 1
                if i == Text2[len(Text2) - 1] and k1 == len(Text2):
                    Text3 += str(R1)
                continue
            elif i in tis:
                R1 *= 1000
                if i == Text2[len(Text2)-1] and k1==len(Text2):
                    Text3+=str(R1)
                continue
            k+=1
            R1 += Cifri[i]
            if i == Text2[len(Text2)-1] and k1==len(Text2):
                Text3 += str(R1)
            continue
        else:
            R2 = 0
            if k>0:
                Text3+=str(R1)
            k = 0
            R1 = 0
            if i == 'скобка':  ###скобки
                sk += 1
                continue
            elif sk == 1:
                sk = 0
                if i == 'открывается':
                    Text3 += '('
                elif i == 'закрывается':
                    Text3 += ')'
                continue
            Text3+=znaki[i]
    Otvet = round(eval(Text3),3) #ответ числом
    del(sorted_dict['одну']) #удаляем лишние склонения в словарях
    del(des['десятую'])
    del(des['сотую'])
    del(des['тысячную'])
    print(Text3)
    Text = ''
    R1 = 0
    k=0
    q = 0
    minus = 0
    if Otvet!=abs(Otvet): #если минус - запоминаем что он у нас есть, и удаляем
        minus = 1
        Text+='минус '
        Otvet = abs(Otvet)
    print(Otvet)
    Otvet1 = Otvet
    sohr_otv = int(Otvet)%10                      #преобразование текстовых цифр в обычные
    R1 = Otvet//1000%10
    del(sorted_dict['ноль'])
    for i in sorted_dict:
        if Otvet >= sorted_dict[i]*1000:
            Otvet -= sorted_dict[i]*1000
            Text = Text + i +' '
            continue
    if Text != '' and Text != 'минус ':

        if R1 == 1:
            Text+='тысяча'
        elif R1>=1 and R1<5:
            Text+='тысячи'
        else:
            Text+='тысяч'
    for i in sorted_dict:
        if Otvet >= sorted_dict[i]:
            Otvet -= sorted_dict[i]
            Text = Text + i + ' '
    for i in sorted_dict:
        if Otvet<1 and Otvet !=0:
            Otvet=Otvet1
            del(sorted_dict['один'])
            del(sorted_dict['два'])
            if minus == 0:
                Text = ''
            else:
                Text = 'минус '
            if Otvet != abs(Otvet):
                Otvet = abs(Otvet)
                Text += 'минус '
            for j in sorted_dict:
                if Otvet >= sorted_dict[j] * 1000:
                    Otvet -= sorted_dict[j] * 1000
                    Text = Text + j + ' '
                    continue
            if Text != '' and Text != 'минус ':
                if R1 == 1:
                    Text += 'тысяча '
                elif R1 >= 1 and R1 < 5:
                    Text += 'тысячи '
                else:
                    Text += 'тысяч '
            for j in sorted_dict:
                if Otvet >= sorted_dict[j]:
                    Otvet -= sorted_dict[j]
                    Text = Text + j + ' '
            q = 1
            if Text != 'минус ' and Text != '':

                if sohr_otv == 1:
                    Text+='целая и '
                else:
                    Text+='целых и '
            break
    while Otvet %1 !=0: #округление до тысячных
        Otvet =round(Otvet,3)*10
        k+=1
    Otvet = int(Otvet)
    if Otvet % 10 == 1:
        okon = 1
    for j in sorted_dict:
        if q == 0:
            break
        if Otvet >= sorted_dict[j]:
            Otvet -= sorted_dict[j]
            Text = Text + j + ' '
    if q == 1:
        if okon==1:
            Text+=B1[k]
        else:
            Text+=B[k]
    return Text
R = ''
vv = 0
k = 0
def vivod():
    if var.get() == 1:
        text=Label(text ='Результат:\n'+ calc(Text1.get()),
                   bg = '#fafafa',wraplength=300,font = 6,justify=CENTER,
                   height = 5,width=30,pady=0,anchor='n')
        text.place(rely=.2,relx = .33)
    if var.get() == 0:
        text = Label(text='Идет запись.',
                     bg='#fafafa', wraplength=300, font=6, justify=CENTER,
                     height=5, width=30, pady=0, anchor='n')
        text.place(rely=.2, relx=.33)
        window.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Идет запись.")
            audio = r.listen(source)
            text = Label(text='',
                         bg='#fafafa', wraplength=300, font=6, justify=CENTER,
                         height=5, width=30, pady=0, anchor='n')
            text.place(rely=.2, relx=.33)
        try:
            R = r.recognize_google(audio, language="ru-RU")
            print("Вы сказали: " + str(R))
            for i in range(len(R)):
                if R[i]==',':
                    R.replace(',','.')
            print(R)
            text = Label(text='Результат:\n' + num2words(eval(R), lang='ru'), bg='#fafafa', wraplength=300, font=6, justify=CENTER,
                         height=5, width=30, pady=0, anchor='n')
            text.place(rely=.2, relx=.33)
        except:
            text = Label(text='Ошибка в распознавании.',
                         bg='#fafafa', wraplength=300, font=6, justify=CENTER,
                         height=5, width=30, pady=0, anchor='n')
            text.place(rely=.2, relx=.33)
            print('Ошибка в распознавании.')

window = Tk()
window.title('Текстовый калькулятор by EremeevDI')
window.geometry('500x150')
window.resizable(width=False, height=False)
window['bg']='#fafafa'
Label(text='Введите выражение:',font=20,bg='#fafafa').grid(row=0,column=0)
Text1 = Entry(width=27,font = 10)
Text1.grid(row=0, column=1, columnspan=3)
var = IntVar()
var.set(1)
rad0 = Radiobutton(window, text="Запись",bg='#fafafa',activebackground='#fafafa', variable=var, value=0,pady=5)
rad0.place(relx=0.17,rely=0.25)
rad1 = Radiobutton(window, text="Текст",bg='#fafafa',activebackground='#fafafa', variable=var, value=1,pady=5)
rad1.place(relx=0.05,rely=0.25)
btn1 = Button(window, text="Решить",bg='#fafafa',activebackground='#fafafa',height=2,width=9,command=vivod)
btn1.place(relx=0.10,rely=0.53)
window.mainloop()
