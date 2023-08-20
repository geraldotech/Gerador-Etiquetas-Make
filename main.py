from docx import Document
from docx2pdf import convert
import os

documento = Document("TEMPLATE.docx")


print('\033[1m' + '\033[92m' + "Make Gerador de Etiqueta L42  v1.0" + '\033[0m')
print('----------------------------------')
nf = input('Nota fiscal:')

# if nf.length = 0 ou spaces sets a default name for NF
if len(nf) == 0 or nf.isspace():
    nf = "notaFiscal"
   

vendacasada = input('Num venda casada:')
origem = input('Num origem:')
destino = input('Num destino:')



# Dictionaries
referencias = {
   "XXXX": nf,
   "YYYYY": vendacasada,
   "ZZZZ": origem,
   "kkkk": destino,
}


for paragrafo in documento.paragraphs:
   inline = paragrafo.runs
   for i in range(len(inline)):
      text = inline[i].text      
      for codigo in referencias.keys():
         if codigo in text:
            text=text.replace(codigo, referencias[codigo])
            inline[i].text = text

# define Desktop path
desktopPatch = os.path.join(os.environ['USERPROFILE'], "Desktop")

#set default fileName
doxc_saved = "etiqueta.docx"

#save docx
documento.save(doxc_saved)

#check files exists
check_file = os.path.isfile(doxc_saved)

if(check_file):
   print('----------------------------------')
   print("AGUARDE GERANDO ETIQUETA PARA NOTA FISCAL:"+ nf)
   
#convert to pdf and save on patch
convert(doxc_saved, desktopPatch+"\{}{}".format(nf, ".pdf"))

#if doc success show message
if(desktopPatch+"\{}{}".format(nf, ".pdf")):
   print('----------------------------------')
   print('\033[1m' + '\033[92m' + "ETIQUETA GERADA COM SUCESSO SALVO EM:" + '\033[0m', desktopPatch+"\{}{}".format(nf, ".pdf"))


a = input('Pressione ENTER para sair')
if a:
    exit(0)

