

def lectura():
      datos=[]
      f=open('wcm.csv','r',encoding="utf8")
      lines=f.readlines()
      f.close()
      for i in lines:
             a=i.rstrip('\n').split(',')#Elimina los indicadores de salto de linea y divide la lista apartir de estos mismos
             datos.append(a)

             for f in datos:
                  home_team=f[0]
                  away_team=f[1]
                  home_score=f[2]
                  home_penalty=f[3]
                  away_score=f[4]
                  away_penalty=f[5]
                  home_manager=f[6]
                  home_captain=f[7]
                  away_manager=f[8]
                  away_captain=f[9]
                  attendace=f[10]
                  veneau=f[11]
                  round=f[12]
                  date=f[13]
                  referee=f[14]
                  host=f[15]
                  year=f[16]
             if round=='Final' and year=='2022':
                  print(home_team, away_team)

      return datos



            
            
def enfrentamiento():
      listado=lectura()
      equipo_1=input('Seleccione le primer equipio')
      equipo_2=input('Seleccione el segundo equipo')
      for
      if equipo_1 in listado and equipo_2 in listado:
           print('shit working')
      else:
            print('Ingrese 2 equipos validos')

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
