from asd import Login, Register, verificar_gmail, Verificador
from Usuarios import usuarios, id, Almacenar_Datos_Registro, id_dicc
from libros import rellenar_datos_nueva_obra, anadir_obra_al_catalogo, ver_catalogo, Libro, Revista, Articulo

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
while True:
    try:
        print("A que desea acceder?: \n1.Libros \n2.Revistas \n3.Articulos")
        tipo_obra_acceso = int(input("----> "))

    except:
        print("Debe introducir un numero")
        continue

    while True:
        try:
            print("1.Leer Obras \n2.Crear Obra \n3.Salir")
            leer_crear = int(input("----> "))
        except:
            print("Debe introducir un numero")
            continue

        if tipo_obra_acceso == 1:
            if leer_crear == 1: # Leer libros
                ver_catalogo()

            if leer_crear == 2: # Crear libros

                datos = rellenar_datos_nueva_obra(1)

                libro = Libro(nombre = datos[0],fecha=datos[1],autor=datos[2])
                libro = libro.obtener_datos()
                anadir_obra_al_catalogo(libro)

            elif leer_crear == 3:
                break

        elif tipo_obra_acceso == 2:
            if leer_crear == 1: # Leer Revistas
                ver_catalogo()
            if leer_crear == 2: # Crear Revistas

                datos = rellenar_datos_nueva_obra(2)

                revista = Revista(nombre = datos[0],fecha=datos[1])
                revista = revista.obtener_datos()
                anadir_obra_al_catalogo(revista)
            elif leer_crear == 3:
                break
        elif tipo_obra_acceso == 3:
            if leer_crear == 1: # Leer Articulos
                ver_catalogo()
            if leer_crear == 2: # Crear Articulos

                datos = rellenar_datos_nueva_obra(2)

                articulo = Articulo(nombre = datos[0],autor = datos[1])
                articulo = articulo.obtener_datos()
                anadir_obra_al_catalogo(articulo)
            elif leer_crear == 3:
                break
        else:
            break


