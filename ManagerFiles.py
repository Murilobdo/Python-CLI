import os
import requests as req
import uuid
import random

PATH = 'C:\\Dev\\CLI\\'
FOLDERS = ['figuras', 'icones', 'svgs']
QTD_FILES_GENERATE = 5

def clear():
    os.system('pause')
    os.system('cls')


def createFiles():
    for folder in FOLDERS:
        print(f'Baixando {folder}...')
        i = 0  
        while i < (QTD_FILES_GENERATE * random.randint(1, 5)):
            response = req.get('https://picsum.photos/200/300.jpg')
            if response.status_code == 200:
                with open(PATH + f'{folder}\\' + f'{uuid.uuid4().hex}.jpg', 'wb') as f:
                    f.write(response.content) 
            i = i + 1
    print(f'Pronto !')
    clear()


esc = 0
while esc != 5:
    print('Selecione qual diretorio deseja apagar os arquivos:')
    print('1 - Apagar Figuras')
    print('2 - Apagar Icones')
    print('3 - Apagar SVGs')
    print('4 - Criar arquivos')
    print('5 - Sair')
    esc = int(input())

    if esc == 4:
        createFiles()
    elif esc <= 3:       
        indexFolder = esc - 1
        contador = 0
        for files in os.listdir(PATH + FOLDERS[indexFolder]):
            os.remove(PATH + FOLDERS[indexFolder] + '\\' + files)
            contador = contador + 1
        os.system('cls')
        print(f'{contador} arquivos apagados com sucesso!')
        clear()

    
    
