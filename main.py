from asd import Login, Register, verificar_gmail, Verificador
from Usuarios import usuarios, id, Almacenar_Datos_Registro, id_dicc
while True:

    try:
        lr = int(input("\n1.Loguearse\n2.Registrarse\n---> "))
    except:
        print("Opcion invalida, Elija 1 o 2")
        continue
    if lr == 1:

        nombre = input("Nombre de usuario: ")
        passw = input("Contraseña: ")
        verificador_login = Verificador(nombre,passw)

        if verificador_login.verificar_user():
            print("Te has logueado exitosamente")
            user = Login(nombre,passw)
            break

        else:
            print("Usuario o contraseña Incorrectos")
            continue



    elif lr == 2:
        nombre = input("Nombre de usuario: ")


        while True:
            try:
                edad = int(input("Edad: "))
                break
            except:
                print("Debe introducir un numero!")



        while True:
            try:
                mail = input("Direccion de correo electronico: ")
                if verificar_gmail(mail):
                    break
                else:
                    print("\nDireción invalida, Introduzca una correcta!")
            except:
                pass



        passw = input("Contraseña: ")
        id+=1
        id_dicc +=1
        new_usuario = Register(nombre,edad,mail,passw,id,"Lector")
        almacenador = Almacenar_Datos_Registro
        datos = almacenador.zipear(new_usuario)
        usuarios[id_dicc] = dict(datos)
        print(usuarios)

#Aqui empieza el menu despues de intentar loguearse y/o Registrarse


