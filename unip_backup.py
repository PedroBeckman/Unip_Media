import getpass
print(" *** CALCULADORA DE MÉDIA UNIP ***")
print("---PRESSIONE ENTER PARA CONTINUAR---")
getpass.getpass(prompt="")

MEDIAPROVA = int(float(input("DIGITE SUA NOTA DA PROVA: ")))
MEDIAAVA = int(float(input("DIGITE SUA NOTA AVA: ")))

calculo_nota = ((MEDIAPROVA*9) + (MEDIAAVA*1))/10
 
calcula_media_minima = (calculo_nota + 5)/2

passou = calculo_nota >= 6
reprovou = calculo_nota < 5.7 
arrendodar = calculo_nota >= 5.7 <6

if (passou):
    print("VOCÊ ESTÁ APROVADO, SUA MÉDIA É: {:.2f}".format(calculo_nota))
    exit()

elif (arrendodar):
    arrendodar = calculo_nota >= 5.7 < 6
    print("SUA NOTA FOI {:.2F}, MAS FOI ARREDONDADA PRA 6".format(calculo_nota))
    exit()
else:
    print("VOCÊ REPROVOU, SUA MÉDIA É: {:.2f}".format(calculo_nota))
    print("VOCÊ PRECISA NO MÍNIMO DE: {:.2f} PARA PASSAR".format(calcula_media_minima))
    print("PRESSIONE ENTER")
    getpass.getpass(prompt="")

MEDIAEXAME = int(float(input("DIGITE SUA NOTA DO EXAME DE REC: ")))
calcula_exame = (MEDIAEXAME + calculo_nota)/2
passou_exame = calcula_exame >= 5
reprovou_exame = calcula_exame < 4.75 
arrendodar_exame = calcula_exame >= 4.75 < 5

if (passou_exame):
    print("VOCÊ PASSOU NO EXAME DE REC, SUA MÉDIA É : {:.2F}".format(calcula_exame))
    exit()
elif(arrendodar_exame):
    arrendodar_exame = calcula_exame >= 4.75 > 5
    print("SUA NOTA FOI {:.2F}, MAS FOI ARREDONDADA PRA 5, VOCÊ FOI APROVADO".format(calcula_exame))
    exit()
else:
    print("VOCÊ REPROVOU NO EXAME DE REC, SUA MÉDIA É : {:.2F}".format(calcula_exame))

exit()