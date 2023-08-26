from docx import Document
from docx.shared import Pt

documento = Document("ETIQUETA.docx")

nf = input('Nota fiscal:')
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
      

documento.save("etiqueta lançada.docx")

