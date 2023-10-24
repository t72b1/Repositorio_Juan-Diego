

def lectura():
      datos=[]
      f=open('wcm.csv','r',encoding="utf8")
      lines=f.readlines()
      f.close()
      for line in lines:
        partido = line.rstrip('\n').split(',')
        datos.append(partido)


        #home_team = f[0]
        #away_team = f[1]
        #home_score = f[2]
        #home_penalty = f[3]
        #away_score = f[4]
        #away_penalty = f[5]
        #home_manager = f[6]
        #home_captain = f[7]
        #away_manager = f[8]
        #away_captain = f[9]
        #attendance = f[10]
        #venue = f[11]
       #round = f[12]
        #date = f[13]
        #referee = f[14]
        #host = f[15]
        #year = f[16] #Dejo  esto para guiarme
      return datos


  
def enfrentamiento():
      listado=lectura()
      print (lectura)
      equipo_1=input('Seleccione el primer equipo')
      equipo_2=input('Seleccione el segundo equipo')
      contador_enfrentamientos=0
      partidos_enfrentados=[]
      for i in listado:
        home_team = i[0] #Define cual posicion es el equipo local y el visitante
        away_team = i[1]
        if equipo_1 in home_team and equipo_2 in away_team:
            contador_enfrentamientos += 1
            partidos_enfrentados.append(i)
        elif equipo_1 in away_team and equipo_2 in home_team:
            contador_enfrentamientos += 1
            partidos_enfrentados.append(i)
            # Pregunta si ambos equipos fueron encontrados en cualquiera de las 2 posciones y agrega a la lista de partidos si es asi
            
            
      if contador_enfrentamientos > 0: #Si la cantidad de partidos es mayor que 0 imprime la cantidad de partidos
        print(f'Cantidad de partidos:{contador_enfrentamientos}')
    
        contador_victorias_home=0
        contador_derrotas_home=0
        contador_empates_home=0
        contador_victorias_away=0
        contador_derrotas_away=0
        contador_empates_away=0 #Contadores
        for partido in partidos_enfrentados:
            if equipo_1 in partido[0]:  # Equipo 1 es el local
                equipo_local = partido[0]
                equipo_visitante = partido[1]
                marcador_local = int(partido[2])
                marcador_visitante = int(partido[4])
            else:  # Equipo 2 es el local
                equipo_local = partido[1]
                equipo_visitante = partido[0]
                marcador_local = int(partido[4])
                marcador_visitante = int(partido[2])
            #Esto de arriba determina cual equipo es local y cual es visitante
            if marcador_local > marcador_visitante: #Si el marcador local es mayor al de los visitantes añade una victoria a local y una derrota a visitante
                contador_victorias_home += 1
                contador_derrotas_away += 1
            elif marcador_local < marcador_visitante: #Vicebersa de lo de arriba
                contador_derrotas_home += 1
                contador_victorias_away += 1
            else: #Si es empate
                contador_empates_home += 1
                contador_empates_away += 1



        print(f'Historial: {equipo_1} => {contador_victorias_home} victorias, {contador_empates_home} empates, {contador_derrotas_home} derrotas')
        print(f'           {equipo_2} => {contador_victorias_away} victorias, {contador_empates_away} empates, {contador_derrotas_away} derrotas')
        for partido in partidos_enfrentados:
            print('-------------------------------------------')
            print(f'                  -{partido[15]} {partido[16]}-')
            print(f'{partido[0]} |{partido[2]} vs {partido[4]}| {partido[1]} - Ronda:{partido[12]}')
            print('-------------------------------------------')
            print('')
      else:
        print('')
        print(f'Los equipos {equipo_1} y {equipo_2} no se han enfrentado.')
        print('')
        print('') #Espacios


def promedioGoles():
    listado=lectura()
    equipo=input('¿Cual pais desea consultar? ----->')
    partidos_enfrentados=[]
    for i in listado:
        home_team = i[0] #Define cual posicion es el equipo local y el visitante
        away_team = i[1]
        if equipo in home_team or equipo in away_team: #Pregunta si el equipo esta en cualquiera de las 2 posiciones
            partidos_enfrentados.append(i)         
    
    mundiales=clasificaciones(listado,equipo)
    numero_goles=0       
    for partido in partidos_enfrentados:
        if equipo in partido[0]:  # Equipo es el local
            goles=int(partido[2])
            numero_goles+=goles
        else:  # Equipo  es el visitante
            goles=int(partido[4])
            numero_goles+=goles
            
    promedio=numero_goles/mundiales #Operacion de promedio
    
        
    print(round(promedio,2))
    print('')
    print('')


def finales():
    listado=lectura()
    final='Final'
    lista_finales=[]
    for i in listado:
        ronda=i[12] #Define la ronda como la posicion 12 de la lista
        if final == ronda: #Si la palabra 'Final' esta en la lista lo agrega a la lista de finales
            lista_finales.append(i)
            #Si final esta en en el espacio 12 lo agrega a la lista de finales
            
    for partido in lista_finales:
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])
        #Da los datos de goles de las finales
        
   
        if goles_local==goles_visitante:   # Si los goles estan empatados significa que si o si se tuvieron que ir a penalties
                print('-------------------------------------------')
                print(f'          -{partido[15]} ({partido[16]})-')
                print(f'{partido[0]} - {partido[1]} | Marcador:{partido[2]}-{partido[4]}| Penales {partido[3]}-{partido[5]}')
                print('-------------------------------------------')
                print('')
print('')
print('')

def clasificaciones(listado, equipo):
    mundial = set() #Set es un "conjunto" basicamente funciona parecido que una lista pero no acepta mas de una misma variable, por eso la utilizo, para que solo se almacene un partido por mundial
    for partido in listado:
        if partido[0] == equipo or partido[1] == equipo: #Si equipo esta en la posicion local o visitante
            mundial.add(partido[16]) #Se añade al conjunto mundial
    return len(mundial) #Devuelve el numero de mundiales que el equipo clasifico




            
def main():
    while 1:
        print("Selecciona una opción: (Seleccione el numero)")
        print("1. Conocer cuantas veces se han enfrentado 2 equipos en los mundiales")
        print("2. Conocer el promedio de goles de un equipo en mundiales")
        print("3. Conocer el número de finales disputadas por penales")
        print("4. Salir")
        
        opcion = input("Ingresa el número de la opción deseada: ")
        
        if opcion == "1":
            enfrentamiento()
        elif opcion == "2":
            promedioGoles()
        elif opcion == "3":
            finales()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print('')
            
            print("Opción no válida. Por favor, selecciona una opción válida.")
            print('')
            print('')



if __name__=="__main__":
  main()