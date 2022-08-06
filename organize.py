from argparse import FileType
import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            ##lê cada categoria (Do dicionário) e sufixono diretorio 
            if suffix == value:
                #Se o sufixo do item for igual ao solicitado na função
                return category
                #vai retornar a categoria do dificionário
    return 'MISC'
    #Vai acontecer se a resposta for um formato que não está no SUBDIRECTORIES
print(pickDirectory('.pdf'))
#teste pra ver se encontra a categoria certa
def organizeDirectory():
    for items in os.scandir():
        #vai pegar todo objeto na pasta pela extensão
        if items.is_dir():
            continue
            #se o item for uma pasta ele não será afetado por esta função
        filePath = Path(items)
        #Vai pegar o Path (caminho) de cada item
        fileType = filePath.suffix.lower()
        #vai definit o tipo, para isso vai pegar o sufixo do path (ex .png) e vai deixar tudo minúsculo
        directory = pickDirectory(fileType)
        #vai definir as categorias de cada item, directory vai ser a categoria em questão
        directoryPath = Path(directory)
        #vai setar o path do diretoria de cada categoria
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
            #Se o path dessa categoria não existir ele será criado
        filePath.rename(directoryPath.joinpath(filePath))
        #muda o nome do path para mandar o item para a sua respectiva pasta

organizeDirectory()
#roda o programa