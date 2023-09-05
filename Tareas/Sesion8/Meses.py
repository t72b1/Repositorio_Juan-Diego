def Elegir_mes(x):


  Meses=['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
  elem=x in Meses
  if elem is True:
    mes=Meses.index(x)
    mes_seleccionado=Meses[mes]
    if mes==0:
      print('Usted selecciono Enero:\nEnero tiene 31 dias y 2 festivos: \n1: Dia de año nuevo (1) \n'\
          '2:Día de los Reyes Magos (9)')
    elif mes == 1:
        print("Usted seleccionó Febrero:\nFebrero tiene 28/29 días y 0 dias festivos")
    elif mes == 2:
        print("Usted seleccionó Marzo:\nMarzo tiene 31 días y 1 festivo: \nDía de San José (20)")
    elif mes == 3:
        print("Usted seleccionó Abril:\nAbril tiene 30 días y 3 festivos: \n"\
            '1:Jueves Santo (6) \n2:Viernes Santo(7) \n3:Domingo de resurreccion(9)')
    elif mes == 4:
        print("Usted seleccionó Mayo:\nMayo tiene 31 días y 2 festivos:\n1: Día del trabajo (1)\n"\
            '2:Dia de la asención (22)')
    elif mes == 5:
        print("Usted seleccionó Junio:\nJunio tiene 30 días y 2 festivos: \n1: Corpus Christi (12)\n"\
            '2: Sagrado Corazon de Jesus (19)')
    elif mes == 6:
        print("Usted seleccionó Julio:\nJulio tiene 31 días y 2 festivos:\n1: Dia de San Pedro y San Pablo (3)\n"\
            '2: Dia de la independencia  (20)')
    elif mes == 7:
        print("Usted seleccionó Agosto:\nAgosto tiene 31 días y 2 festivos:\n1: Batalla de Boyaca (7)\n"\
            '2: Asunción de la virgen (15)')
    elif mes == 8:
        print("Usted seleccionó Septiembre:\nSeptiembre tiene 30 días y 0 festivos")
    elif mes == 9:
        print("Usted seleccionó Octubre:\nOctubre tiene 31 días y 1 festivo:\n1: Dia de la raza (16)")
    elif mes == 10:
        print("Usted seleccionó Noviembre:\nNoviembre tiene 30 días y 2 festivos: \n1: Dia de todos los santos (6)\n"\
            '2: Independencia de Cartagena (13)')
    elif mes == 11:
        print("Usted seleccionó Diciembre:\nDiciembre tiene 31 días y 3 festivos:\n1: Inmaculada concepción (8)\n2: Navidad (25)\n"\
           '3: Fin de Año (31)')
  else:
    print('Ingrese el nombre del mes porfavor')




if __name__ =='__main__':
  x=input('Ingrese el mes que quiere seleccionar')
  x=x.lower()
  Elegir_mes(x)