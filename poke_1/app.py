# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck", "Eevee", "Gengar", "Mewtwo", "Vaporeon", 'francia']
        self.lista_poder_pokemones = [80, 150, 70, 90, 60, 100, 75, 120, 180, 95, 30]
        self.lista_tipo_pokemones = ["eléctrico", "fuego", "planta", "agua", "normal", "agua", "normal", "fantasma", "psíquico", "agua", "eléctrico"]


    def btn_mostrar_informe_1(self):
        indice = 0
        for pokemon in self.lista_nombre_pokemones:
            alert('Informe 1',f'El nombre del pokemon es {pokemon} y su posicion en la lista es {indice}')
            indice +=1

        tipo_mas_comun=''
        electrico = 0
        fuego = 0
        planta = 0
        agua = 0
        psíquico = 0
        fantasma = 0
        normal = 0

        for tipo in self.lista_tipo_pokemones:
 
            if tipo == 'eléctrico':
                electrico += 1
            elif tipo == 'fuego':
                fuego += 1
            elif tipo == 'planta':
                planta += 1
            elif tipo == 'agua':
                agua += 1
            elif tipo == 'psíquico':
                psíquico += 1
            elif tipo == 'fantasma':
                fantasma += 1
            elif tipo == "normal":
                normal += 1

        if electrico > fuego and electrico > planta and electrico > agua and electrico > psíquico and electrico > fantasma and electrico > normal:
            tipo_mas_comun = 'electrico'
        elif fuego > electrico and fuego > planta and fuego > agua and fuego > psíquico and fuego > fantasma and fuego > normal:
            tipo_mas_comun = 'fuego'
        elif planta > electrico and planta > fuego and planta > agua and planta > psíquico and planta > fantasma and planta > normal:
            tipo_mas_comun = 'planta'
        elif agua > electrico and agua > fuego and agua > planta and agua > psíquico and agua >fantasma and agua > normal:
            tipo_mas_comun = 'agua'
        elif psíquico > electrico and psíquico > fuego and psíquico > planta and psíquico > agua and psíquico >fantasma and psíquico > normal:
            tipo_mas_comun = 'psíquico'
        elif fantasma > electrico and fantasma > fuego and fantasma > planta and fantasma > agua and fantasma > psíquico and fantasma > normal:
            tipo_mas_comun = 'fantasma'
        elif normal > electrico and normal > fuego and normal > planta and normal > agua and normal > psíquico and normal > fantasma:
            tipo_mas_comun = 'normal'

        alert('Informe 1',f'El tipo mas comun es {tipo_mas_comun}')
    
    def btn_mostrar_informe_2(self):
        nombre = ''
        poder = 300
        indice = 0
        
        for tipo in self.lista_tipo_pokemones:
            if tipo == 'psíquico' and self.lista_poder_pokemones[indice] < poder:
                poder = self.lista_poder_pokemones[indice]
                nombre = self.lista_nombre_pokemones[indice]

            indice += 1
        alert('Informe 2',f'El pokemon tipo psíquico mas bajo es {nombre} con un poder de {poder}')

                
    
    def btn_mostrar_informe_3(self):
        poder_total = 0
        cantidad_electricos = 0
        indice = 0
        for tipo in self.lista_tipo_pokemones:
            if tipo == 'eléctrico':
                poder_total += self.lista_poder_pokemones[indice]
                cantidad_electricos += 1
            indice += 1
        promedio_de_poder = poder_total / cantidad_electricos
        alert('Informe 3',f'El promedio de poder de los pokemon tipo eléctrico es de {promedio_de_poder}')

    def btn_cargar_pokedex_on_click(self):
    # A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
    #  Los datos que deberas pedir para los pokemones son:
    # * El nombre del pokemon
    # * El tipo de su elemento (Agua, Psiquico, Electrico)
    # * Poder de ataque (validar que sea mayor a 50 y menor a 200) 
        while True:
            nombre = prompt('Bienvenido','Por favor ingrese el nombre del pokemon')

            tipo = prompt('Bienvenido','Por favor ingrese el tipo del pokemon')
            while tipo != 'Agua' and tipo != 'Psiquico' and tipo != 'Electrico':
                tipo = prompt('Bienvenido','Por favor ingrese el tipo del pokemon')

            poder = prompt('Bienvenido','Por favor ingrese el poder del pokemon')

            while poder.isalpha():
                poder = prompt('Bienvenido','Por favor ingrese el poder del pokemon')
            while poder.isalpha()==False and int(poder) < 50 or int(poder) > 200 :
                poder = prompt('Bienvenido','Por favor ingrese el poder del pokemon')
            break

        self.lista_nombre_pokemones.append(nombre)
        self.lista_poder_pokemones.append(poder)
        self.lista_tipo_pokemones.append(tipo)

            

    
if __name__ == "__main__":
    app = App()
    app.mainloop()