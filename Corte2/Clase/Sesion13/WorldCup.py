

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
      equipo_1=input('Seleccione le primer equipio')
      equipo_2=input('Seleccione el segundo equipo')
      contador_enfrentamientos=0
      partidos_enfrentados=[]
      for i in listado:
        home_team = i[0]
        away_team = i[1]
        if equipo_1 in home_team and equipo_2 in away_team:
            contador_enfrentamientos += 1
            partidos_enfrentados.append(i)
        elif equipo_1 in away_team and equipo_2 in home_team:
            contador_enfrentamientos += 1
            partidos_enfrentados.append(i)


                        
            # Si ambos equipos fueron encontrados en la lista actual
      if contador_enfrentamientos > 0:
        print(f'Cantidad de partidos:{contador_enfrentamientos}')
        
        contador_victorias_home=0
        contador_derrotas_home=0
        contador_empates_home=0
        contador_victorias_away=0
        contador_derrotas_away=0
        contador_empates_away=0
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
            if marcador_local > marcador_visitante:
                contador_victorias_home += 1
                contador_derrotas_away += 1
            elif marcador_local < marcador_visitante:
                contador_derrotas_home += 1
                contador_victorias_away += 1
            else:
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
        print(f'Los equipos {equipo_1} y {equipo_2} no se han enfrentado.')




def main():
      listado=lectura()
      print(listado[1][7])

      menu={'1':campeon_mundial}
      opcion=input('Seleccione una opcion')


      if opcion in menu:
            menu[opcion](listado)
      else:
            print('Opcion invalida')


if __name__=="__main__":
      enfrentamiento()
