from asd import Login, Register, verificar_gmail
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
        user = Login(nombre,passw)
        user.saludar()
        user.saludar()

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

        new_usuario = Register(nombre,edad,mail,passw,id)
        almacenador = Almacenar_Datos_Registro

        datos = almacenador.zipear(new_usuario)
        id_dicc +=1
        usuarios[id_dicc] = dict(datos)
        print(usuarios)


