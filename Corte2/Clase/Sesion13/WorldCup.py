

def lectura():
      datos=[]
      f=open('wcm.csv','r',encoding="utf8")
      lines=f.readlines()
      f.close()
      for i in lines:
             a=i.rstrip('\n').split('\n')
             datos.append(a)
             for i in datos:
                  a=i.split(',')#Elimina los indicadores de salto de linea y divide la lista apartir de estos mismos
                  home_team=a[0]
                  away_team=a[1]
                  home_score=a[2]
                  home_penalty=a[3]
                  away_score=a[4]
                  away_penalty=a[5]
                  home_manager=a[6]
                  home_captain=a[7]
                  away_manager=a[8]
                  away_captain=a[9]
                  attendace=a[10]
                  veneau=a[11]
                  round=a[12]
                  date=a[13]
                  referee=a[14]
                  host=a[15]
                  year=a[16]
                  print(host)



            
            
def campeon_mundial():
      pass


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
      lectura()
