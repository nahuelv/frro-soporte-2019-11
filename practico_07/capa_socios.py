from practico_06.capa_negocio import NegocioSocio

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from practico_05.ejercicio_01 import Socio

from practico_06.capa_negocio import NegocioSocio



def main():

    root = Tk()
    app = Ventana1(root)

class Ventana1:

    def __init__(self, master):

        self.master = master
        self.master.title('ABM Socios')
        self.master.geometry('500x400+0+0')
        self.cdNegocio = NegocioSocio()

        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.master)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two","three","four")

        vsb = ttk.Scrollbar(self.tv, orient="vertical", command=self.tv.yview)
        vsb.place(x=30+355+2, y=0, height=200+20)

        #====================================TVColums==============================================================
        self.tv.column("one", width=100 )
        self.tv.column("two", width=100 )
        self.tv.column("three", width=100)
        self.tv.column("four", width=100)

        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="ID")
        self.tv.heading("two", text="Nombre")
        self.tv.heading("three", text="Apellido")
        self.tv.heading("four", text="DNI")

        #===============================Prueba de insertar datos================================================

        '''
        cdNegocio = NegocioSocio()
        socios = cdNegocio.todos()
        print('Prueba')
        for s in socios:
            self.tv.insert("" , 0, values=(s.id,s.nombre,s.apellido,s.dni))
        self.tv.pack()
        '''
        self.listar()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        self.tv.bind('<ButtonRelease-1>', self.selectItem)

        #====================================Variables===========================================================


        #=====================================Frames================================================================

        self.listado = Frame(self.frame, width= 195, height= 50)
        self.listado.grid(row=2, column=1)

        self.botones = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=5, column=1)


        #===========================================Botones============================================================

        self.btnAlta = Button(self.botones, text='Agregar', command = lambda: self.alta())
        self.btnAlta.grid(row=1, column=1)

        self.btnBaja = Button(self.botones, text='Borrar', command = lambda: self.baja())
        self.btnBaja.grid(row=1, column= 2)

        self.btnModificaciones = Button(self.botones, text='Modificar', command = lambda: self.modificar())
        self.btnModificaciones.grid(row=1,column=3)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 4)


        self.master.mainloop()

    def listar(self):

        self.tv.delete(*self.tv.get_children())


        socios = self.cdNegocio.todos()

        for s in socios:
            self.tv.insert("" , 0, values=(s.id_socio,s.nombre,s.apellido,s.dni))

        self.tv.pack()

    def baja(self):
        print('El id del Socio a borrar es:', self.itemAc[0])
        r = self.deleteme(self.itemAc[1],self.itemAc[2])
        if r == 1:
            self.cdNegocio.baja(self.itemAc[0])
            self.listar()
        else:
            pass


        pass

    def modificar(self):
        self.new_window(1)

    def alta(self):
        self.new_window(2)

    def new_window(self, t):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        if t == 2:
            self.itemAc = None
        self.app = Ventana2(self.newWindow, self, self.itemAc, t)

    def selectItem(self, a):
        curItem = self.tv.focus()
        item = self.tv.item(curItem)
        self.itemAc = item['values']

    def deleteme(self, n, a):
        ressult = messagebox.askquestion("Borrar Socio", "Borrar al socio: " + n +' '+ a + " ?", icon='warning')
        if ressult == 'yes':
            return 1
        else:
            return 0





class Ventana2:

    def __init__(self,master, v1, item, t):
        self.master = master
        if t == 1:
            self.master.title('Modificar Socio')
            self.item = item
        else:
            self.master.title('Agregar Socio')
        self.master.geometry('350x200')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.v1 = v1


        #====================================Variables===========================================================
        self.enombre = StringVar()
        self.eapellido = StringVar()
        self.edni = StringVar()
        self.id_socio = StringVar()

        #=====================================Frames================================================================
        self.cargaDatos = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.cargaDatos.grid(row= 2, column=0)

        self.etiquetas = Frame(self.cargaDatos, width= 100, height = 50,)
        self.etiquetas.grid(row= 1, column=1)

        self.entradas = Frame(self.cargaDatos, width= 100, height = 50,)
        self.entradas.grid(row= 1, column=2)

        self.etId = Frame(self.etiquetas, width= 100, height = 50)
        self.etId.grid(row= 3, column=0)

        self.eId = Frame(self.entradas, width= 100, height = 50)
        self.eId.grid(row= 3, column=0)

        self.etNombre = Frame(self.etiquetas, width= 100, height = 50)
        self.etNombre.grid(row= 0, column=0)

        self.eNombre = Frame(self.entradas, width= 100, height = 50)
        self.eNombre.grid(row= 0, column=0)

        self.etApellido = Frame(self.etiquetas, width= 100, height = 50)
        self.etApellido.grid(row= 1, column=0)

        self.eApellido = Frame(self.entradas, width= 100, height = 50)
        self.eApellido.grid(row= 1, column=0)

        self.etDni = Frame(self.etiquetas, width= 100, height = 50)
        self.etDni.grid(row= 2, column=0)

        self.eDni = Frame(self.entradas, width= 100, height = 50)
        self.eDni.grid(row= 2, column=0)

        self.botones = Frame(self.frame, width= 100, height = 50)
        self.botones.grid(row= 12, column=0)

        #=======================================Botones================================================================

        if t == 2:
            self.btnCargar = Button(self.botones, text='Cargar', command= lambda: self.cargarSocio())
            self.btnCargar.grid(row=0, column= 0)
        else:
            self.btnCargar = Button(self.botones, text='Modificar', command= lambda: self.modificarSocio())
            self.btnCargar.grid(row=0, column= 0)

        self.btnSalir = Button(self.botones, text='Cancelar', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

        #=====================================Etiquetas==========================================================
        if t == 1:
            self.etId = Label(self.etId, text= 'ID:', )
            self.etId.grid(row=0, column= 0)

            self.id_socio = StringVar(self.eId, value= self.item[0])
            self.eId = Entry(self.eId, textvariable= self.id_socio, width=20)
            self.eId.grid(row=0, column=1)


            self.enombre = StringVar(self.eNombre, value= self.item[1])
            self.eapellido = StringVar(self.eApellido, value= self.item[2])
            self.edni = StringVar(self.eDni, value= self.item[3])

        else:
            pass

        self.etNombre = Label(self.etNombre, text= 'Nombre:', )
        self.etNombre.grid(row=0, column= 0)

        self.eN = Entry(self.eNombre, textvariable= self.enombre, width=20)
        self.eN.grid(row=0, column=1)

        #=================================================================================================

        self.etApellido = Label(self.etApellido, text= 'Apellido:',)
        self.etApellido.grid(row=0, column=0)

        self.eA = Entry(self.eApellido, textvariable= self.eapellido, width=20)
        self.eA.grid(row=0, column=1)

        #================================================================================================

        self.etDni = Label(self.etDni, text= 'Dni:', )
        self.etDni.grid(row=0, column= 0)

        self.eDni = Entry(self.eDni, textvariable= self.edni, width=20)
        self.eDni.grid(row=0, column=1)

    def cargarSocio(self):
        nombre = self.enombre.get()
        apellido = self.eapellido.get()
        dni = self.edni.get()

        socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
        ns = NegocioSocio()
        ns.alta(socio)

        #cdNegocio.alta(nombre,apellido,dni)
        self.v1.listar()
        self.master.destroy()

    def modificarSocio(self):
        print('El socio a modificar es:', self.item)
        nombre = self.enombre.get()
        apellido = self.eapellido.get()
        dni = self.edni.get()
        id_socio = self.id_socio.get()


        socio = Socio(id_socio=id_socio, dni=dni, nombre=nombre, apellido=apellido)
        ns = NegocioSocio()
        ns.modificacion(socio)

        self.v1.listar()
        self.master.destroy()


main()