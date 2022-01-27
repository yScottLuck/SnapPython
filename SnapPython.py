import os
def cls():
    os.system('clear')
cls()
from pytube import YouTube
#cores

preto = ('\033[1;30m')
vermelho = ('\033[1;31m')
verde = ('\033[1;32m')
amarelo = ('\033[1;33m')
azul = ('\033[1;36m')
magenta = ('\033[1;35m')
ciano = ('\033[1;90m')
reset = ('\033[0;0m')
branco = ('\033[1;97m')

###
def ln(txt=''):
	l = len(txt) + 4
	print(f'{preto}='*l)
	print(f'{txt:^{l}}')
	print(f'{magenta}='*l)
    
###
ln('snap.py')
while True:
    url = str(input(f'{ciano}Insira a url do video: {azul}'))
    yt = YouTube(url)
    txt = (yt.title)
    dsc = (yt.description)
    views = (yt.views)
    cnl = (yt.author)
    print(f'''

{branco}CANAL: {ciano}{cnl}
{branco}TÍTULO DO VÍDEO: {ciano}{txt}
{branco}NÚMERO DE VISUALIZAÇÕES: {ciano}{views}
{branco}DESCRIÇÃO: 
{ciano}{dsc}

''')
    print(f'''
1 = Sim
2 = Não''')
    pg = int(input('Deseja baixar o vídeo?: '))
    if pg == (1):
            print('baixando...')
            audio = yt.streams.       get_highest_resolution()
            audio.download()
            try:
                print('instalação concluída!!')
                cwd = os.getcwd()
                print(f'O arquivo foi baixado em: {cwd}')
                print('''
1 - Sim 
2 - Não''')
                pg2 = int(input('Deseja baixar outro vídeo?: '))
                if pg2 == (1):
                    continue
                elif pg2 == (2):
                    break
            except:
                print('Ocorreu um erro no download. Tente novamente, script sendo fechada.')
                cls()
                exit()
    elif pg == (2):
        print('''
1 - Baixar outro vídeo
2 - Fechar a Script''')
        pg1 = int(input('Deseja baixar outro vídeo ou fechar a script?: '))
        if pg1 == (1):
            continue
        elif pg1 == (2):
            break