import random,string
import rapid_email_validator as rv

usarios=["mati7","mati","matt"]


def agregar_numeros(n):
    dig=string.digits
    return "".join(random.choice(dig) for i in range(n))


def verifica_usuario(username):
    orig=username

    if orig not in usarios:
        return (True,orig)

    while username in usarios:
	if len(username)-len(orig) > 3:
		username=username[:-3]
        username= username+agregar_numeros(3)

    else:
        return (False,username)


def verficicacion_email():
	return True

def verificacion_email_2(email):
	if rv.verificar(email):
		return True
	else return False

# Funcion principal del modulo
def ingreso_usuario(username):
    res=verifica_usuario(username)
    if res[0]:
        print("Usuario Disponible!")
    else:
        print("Usuario No disponible, intenta con :",res[1])




