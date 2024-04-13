from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
#from reportlab.pdfbase import 



cnv = canvas.Canvas("Dia_10/TestePDF.pdf",pagesize=A4)
# ponto 0,0 é na parte inferior esquerda do pdf
cnv.setFont('Helvetica',14)
cnv.drawString(0,0,"Teste(0,0)",)
cnv.drawString(250,450,"Teste(250,450)")

cnv.save()

# Função que converte de milimetros para pontos
def mm2p(millimeters):
    return millimeters / 0.352777

#Simulação de tamanho de string
""" 
from reportlab.pdfbase.pdfmetrics import stringWidth
width = stringWidth(text, font_name, font_size)
"""

# Todo Criar uma classse que automatize o trabalho para criação de pdf A4