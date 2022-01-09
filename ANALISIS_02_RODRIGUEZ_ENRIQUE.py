import pandas as pd

path = 'C:\scripts Python\synergy_logistics_database.csv' # Cambiar ruta donde se localice la base de datos
data = pd.read_csv(path)
print(data.head())

print('El dataset esta compuesto por una cantidad de registros de los siguientes años:')
print(data.year.unique())
print('Los medios de transporte son:')
print(data.transport_mode.unique())

print('===================== Rutas de importación y exportación =====================')

'''
Para el análisis, se considera el recuento de todas las importaciones y exportaciones para las 
distintas rutas (origen->destino y medio de transporte) de todos los años registrados en el dataset.
'''

top_routes = data.groupby(by=['origin','destination','transport_mode']).agg(total=('register_id','count'),total_value=('total_value','sum')).reset_index().sort_values(by='total',ascending=False)
top_routes['route'] = top_routes.origin + '->' + top_routes.destination + ' [via ' + top_routes.transport_mode + ']'
print(top_routes.head(10))

'''
En general, se puede observar que las 10 rutas con mayor volumen de importaciones, son las 
presentadas en la tabla anterior, teniendo las rutas de South Korea->Vietnam por mar y USA->Netherlands 
por mar con un volumen total mayor a 400.
'''

top_value = data.groupby(by=['origin','destination','transport_mode']).agg(total=('register_id','count'),total_value=('total_value','sum')).reset_index().sort_values(by='total_value',ascending=False)
top_value['route'] = top_value.origin + '->' + top_value.destination + ' [via ' + top_value.transport_mode + ']'
print(top_value.head(10))

'''
Con los datos obtenidos, no se recomienda enfocarse en su totalidad en las rutas con un mayor volumen de importaciones y 
exportaciones, ya que si obtenemos el top 10 de rutas basándonos en el valor total de las importaciones y exportaciones, podemos 
observar que únicamente 3/10 rutas estan presentes en ambas tablas. Esto nos indica que existen 7 rutas que si bien el volumen 
de importaciones y exportaciones no es tan alto como otras, producen más valor que las que tienen un mayor volumen.
'''

print('===================== Medio de transporte utilizado =====================')

'''
Para el análisis, se considera la suma del valor de las importaciones y exportaciones para los distintos medios de transporte de 
todos los años registrados en el dataset.
'''

top_transport = data.groupby(by=['transport_mode']).agg(total_value=('total_value','sum')).reset_index().sort_values(by='total_value',ascending=False)
print(top_transport)

'''
Si se considera en conjunto el valor de las importaciones y exportaciones, se obtiene que los 3 medios más importantes son por mar, 
tren y aire. A continuación, se obtiene el análisis clasificando también por dirección (importación o exportación).
'''

top_transport_dir = data.groupby(by=['transport_mode','direction']).agg(total_value=('total_value','sum')).reset_index().sort_values(by='total_value',ascending=False)
top_transport_exp = top_transport_dir[top_transport_dir.direction == 'Imports']
top_transport_imp = top_transport_dir[top_transport_dir.direction == 'Exports']

print(top_transport_exp.sort_values(by='total_value',ascending=False))
print(top_transport_imp.sort_values(by='total_value',ascending=False))

'''
Los resultados obtenidos nos muestran una variación en las exportaciones, donde el tercer medio de transporte más importante es por carretera.

Basado en los datos con los que se cuenta, y que se identifica que existen únicamente 4 medios de transporte, podría reducirse el medio de 
transporte por carretera para las importaciones, ya que a diferencia contra el tercer medio más usado es lo suficientemente significativo para 
considerar reducirlo (considerando que la diferencia es de aproximadamente 6 mil millones de dólares). Por el contrario, para las exportaciones, 
los medios de transporte que se pudieran reducir son por aire y carretera, esto debido a la diferencia del total de valor en comparación al segundo 
medio de transporte más usado, el cual es por tren.

Adicionalmente, se identifica que general las importaciones y exportaciones tienen una diferencia aún más significativa contra el medio de transporte 
por mar, esto puede deberse a las bajas tarifas que tiene este medio de transporte. Por lo tanto, se sugiere evaluar si hay productos que se puedan 
cambiar a medios de transporte por mar, ya que estos representan la opción más viable para las importaciones y exportaciones. El medio de transporte por 
carretera demuestra en ambos casos que es un medio de transporte que se pudiera reducir.
'''

print('===================== Valor total de importaciones y exportaciones =====================')

'''
Para el análisis, se toma el valor total de las importaciones y exportaciones por país de origen de todos los años registrados en el dataset.
'''

total_value_country = data.groupby(by=['origin']).agg(total_value=('total_value','sum')).reset_index().sort_values(by='total_value',ascending=False).reset_index(drop=True)
print(total_value_country)

print('El valor total de las importaciones y exportaciones es de {}'.format(total_value_country.total_value.sum()))
print('El 80 porciento del valor total de las importaciones y exportaciones es de {}'.format(total_value_country.total_value.sum()*0.8))

paises = []
valor = 0
meta = total_value_country.total_value.sum()*0.8

for index, row in total_value_country.iterrows():
    valor += row.total_value
    paises.append(row.origin)
    # Consideramos que el valor este por arriba de la meta, ya que de otra forma este puede quedar mucho menor al 80 porciento, lo cual no cumpliria con el objetivo de este analisis
    if valor > meta:
        break

print('El número de países que producen aproximadamente el 80 porciento del valor de importaciones y exportaciones es {}, y son:'.format(len(paises)))
print(paises)
print('El total de valor que producen estos países es {}, correspondientes a {} porciento del valor total'.format(valor, round(valor/total_value_country.total_value.sum()*100,2)))

'''
El resultado del análisis muestra 9 de 23 países con un valor en el volumen de importaciones y exportaciones bueno, siendo que estos componen el 80% del 
total del valor de importaciones y exportaciones de todos los años. Enfocar los esfuerzos en estos países es una opción viable, ya que representan menos 
del 50% del total de países con los que se tiene alguna ruta.
'''
