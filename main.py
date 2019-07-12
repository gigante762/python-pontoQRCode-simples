#qpy:3
#qpy:console

'''
Criado por Kevin
e-mail: igantekevin@hotmail.com
'''
## parte do app no cell
from androidhelper import Android
from time import ctime
dr = Android()
voluntarios = []
##

class Voluntario:
    def __init__(self,num):
        self.numero = num
        self.entrada = ctime()
        self.saida = 0
    def baterSaida(self):
        self.saida = ctime()



##def funcçao que atribui o valor lido do barcode para delattr

def loadData():
    arq=open(NomeDoArquivo)
    a=arq.readlines()
    arq.close()
    for i in range(1,len(a)):
        b=a[i].split(',')
        print(b)
        c=Voluntario(b[0])
        c.entrada=b[1]
        c.saida=b[2].replace('\n','')
        voluntarios.append(c)
        #print(c)


#loadData()
def antesLoad():
    try:
        f=open(NomeDoArquivo)
        f.close()
        #input("tem o arquivo")
        loadData()
    except FileNotFoundError:
       #input('nao tem ')
       pass
def getCode():
    a=dr.scanBarcode()
    data = a.result['extras']['SCAN_RESULT']
    return data
##

def getNomeDoArquivo():
    nome = input('Coloque o nome do arquivo: \n> ')
    nome = nome+'.csv'
    return nome
def saveData():
    arq = open(NomeDoArquivo,'w')
    arq.write('Numero de Voluntario, Entrada,Saida\n')
    for i in voluntarios:
        arq.write(str(i.numero)+',')
        arq.write(str(i.entrada)+',')
        arq.write(str(i.saida)+'\n')
    arq.close()


def check():
#chamar o scan
    data = getCode()#scan()#result
    if data == 'save':
        saveData()
    if data == 'exit':
        saveData()
        quit()
#verificar se ja esta cadastrado
    find = False
    for obj in voluntarios:
        if data == obj.numero:
            find = True
            dr.makeToast('Saida de {} para {}'.format(obj.numero,ctime()))
            obj.baterSaida()
            saveData()
            break

#reagindo ao find
    if not find:
        voluntarios.append(Voluntario(data))
        saveData()
        dr.makeToast('Entrada de {} para {}'.format(data,ctime()))
##main
 # lista para guardar voluntarios
NomeDoArquivo = getNomeDoArquivo()
antesLoad()
while True:
    check()
#for i in voluntarios:
#    print(i)
#print('save')
#saveData()
#for i in voluntarios:
#   print(i)



