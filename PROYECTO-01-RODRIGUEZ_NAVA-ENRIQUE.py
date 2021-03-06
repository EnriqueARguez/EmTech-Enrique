import pandas as pd
import numpy as np
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from pprint import pprint
import os
import time

# clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

####################### Variables Globales #######################

"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

lifestore_searches_headers  = ['id_search', 'id_product']
lifestore_sales_headers     = ['id_sale', 'id_product', 'score', 'date', 'refund']
lifestore_products_headers  = ['id_product', 'name', 'price', 'category', 'stock']

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

usuarios = [['admin','777'],['enrique','1234']]
users = pd.DataFrame(usuarios,columns=['user','password'])

usuarios = [['admin','777'],['enrique','1234']]
users = pd.DataFrame(usuarios,columns=['user','password'])

#==== Obtenemos los datos con los que trabajaremos ====

sales           = pd.DataFrame(data=lifestore_sales,columns=lifestore_sales_headers) # Datos de ventas
sales['date']   = pd.to_datetime(sales['date']) # Transformamos la fecha de tipo object a datetime
sales['date']   = sales.date.apply(lambda x: x.replace(year = 2020) if x.year == 2002 else x) # Cambiamos la fecha del 2002 a 2020

products = pd.DataFrame(data=lifestore_products,columns=lifestore_products_headers) # Datos de productos

searches = pd.DataFrame(data=lifestore_searches,columns=lifestore_searches_headers) # Datos de busquedas

#======================================================

##################################################################

def top_sales(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    filtro = sales['refund'] != 1
    data = sales[filtro].copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
        # Obtenemos el total n de productos con mayores ventas
        top = sales_group.nlargest(n,columns='total').reset_index()
        print('#================= Top {} Productos con Mayores Ventas =================#'.format(n))
        pprint(top)
    else:
        print('El listado de valores con mayores ventas excede el dataset actual, prueba con otro valor...')
        error = True
    return error

def small_sales(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    filtro = sales['refund'] != 1
    data = sales[filtro].copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
        # Obtenemos el total n de productos con menores ventas
        small = sales_group.nsmallest(n,columns='total').reset_index()
        print('#================= Top {} Productos con Menores Ventas =================#'.format(n))
        pprint(small)
    else:
        print('El listado de valores con menores ventas excede el dataset actual, prueba con otro valor...')
        error = True
    return error

def top_searches(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    data = searches.copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
        # Obtenemos el total n de productos con mayores busquedas
        top = sales_group.nlargest(n,columns='total').reset_index()
        print('#================= Top {} Productos con Mayores Busquedas =================#'.format(n))
        pprint(top)
    else:
        print('El listado de valores con mayores busquedas excede el dataset actual, prueba con otro valor...')
        error = True
    return error

def small_searches(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    data = searches.copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
        # Obtenemos el total n de productos con menores busquedas
        small = sales_group.nsmallest(n,columns='total').reset_index()
        print('#================= Top {} Productos con Menores Busquedas =================#'.format(n))
        pprint(small)
    else:
        print('El listado de valores con menores busquedas excede el dataset actual, prueba con otro valor...')
        error = True
    return error

def top_sales_category(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    filtro = sales['refund'] != 1
    data = sales[filtro].copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left').groupby(by = 'category').agg(total=('total','sum'))
    if n <= sales_group.shape[0]:
        # Obtenemos el total n de categor??as con mayores ventas
        top = sales_group.nlargest(n,columns='total').reset_index()
        print('#================= Top {} Categorias con Mayores Ventas =================#'.format(n))
        pprint(top)
    else:
        print('El listado de valores con mayores ventas excede el dataset actual, prueba con otro valor...')
        error = True
    return error

def small_sales_category(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    filtro = sales['refund'] != 1
    data = sales[filtro].copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left').groupby(by = 'category').agg(total=('total','sum'))
    if n <= sales_group.shape[0]:
        # Obtenemos el total n de categor??as con menores ventas
        small = sales_group.nsmallest(n,columns='total').reset_index()
        print('#================= Top {} Categorias con Menores Ventas =================#'.format(n))
        pprint(small)
    else:
        print('El listado de valores con menores ventas excede el dataset actual, prueba con otro valor...')
        error = True
    return error

def product_searches():
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    data = searches.copy()

    # Agrupamos por id_product para nuestro analisis
    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left').groupby(by = 'category').agg(total=('total','sum'))
    
    data2 = sales_group.sort_values(by = 'total').reset_index()
    print('#================= Total de Busquedas por Catalogo de Producto =================#'.format(n))
    pprint(data2)
    
    return error

def product_reviews(n):
    data = sales.copy()
    error = False

    # Agrupamos por id_product para nuestro analisis
    reviews = data.groupby(by = ['id_product']).agg(total_score=('score','mean')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')

    # Acomodamos las columnas del dataframe a nuestra conveniencia
    cols_at_end = ['total_score']
    reviews = reviews[[c for c in reviews if c not in cols_at_end] + [c for c in cols_at_end if c in reviews]]

    if n <= reviews.shape[0]:
        # Obtenemos la cantidad n del promedio de reviews de productos con mejores scores
        top = reviews.nlargest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Productos con Mayor Score =================#'.format(n))
        pprint(top)
        # Obtenemos la cantidad n del promedio de reviews de categorias con mejores scores
        top = reviews.groupby(by = 'category').agg(total_score=('total_score','mean')).reset_index().nlargest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Categorias con Mayor Score =================#'.format(n))
        pprint(top)
    else:
        print('El listado de valores con menores busquedas excede el dataset actual, prueba con otro valor...')
        error = True
        return error

    if n <= reviews.shape[0]:
        # Obtenemos la cantidad n del promedio de reviews de productos con peores scores
        small = reviews.nsmallest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Productos con Menor Score =================#'.format(n))
        pprint(small)
        # Obtenemos la cantidad n del promedio de reviews de categorias con peores scores
        small = reviews.groupby(by = 'category').agg(total_score=('total_score','mean')).reset_index().nsmallest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Categorias con Menor Score =================#'.format(n))
        pprint(small)
    else:
        print('El listado de valores con menores busquedas excede el dataset actual, prueba con otro valor...')
        error = True
        return error

    return error

def sales_income():
    # Se descartan aquellas ventas que fueron devoluciones
    filtro = sales.refund != 1
    data = sales[filtro].copy()
    data = data.merge(products[['id_product','price']],on='id_product',how='left')

    # Agrupamos por fecha para nuestro analisis
    total_sales = data.groupby(by=[pd.Grouper(key='date', freq='M')]).agg(sold=('id_product','count'),total_income=('price','sum')).reset_index()
    # Obtenemos el mes
    total_sales['month'] = total_sales['date'].dt.strftime('%b')
    # Acomodamos las columnas del dataframe a nuestra conveniencia
    cols_at_end = ['sold','total_income']
    total_sales = total_sales[[c for c in total_sales if c not in cols_at_end] + [c for c in cols_at_end if c in total_sales]]

    print('#================= Ingresos y Ventas Totales =================#')
    pprint(total_sales)

    print('\n')

    # Obtenemos los datos anuales de ventas e ingresos
    for year in total_sales['date'].dt.year.unique():
        total_sales_year = total_sales[total_sales['date'].dt.year == year].sold.sum()
        total_income_year = total_sales[total_sales['date'].dt.year == year].total_income.sum()
        best_months = total_sales.nlargest(4,columns='sold').reset_index(drop=True).month
        print('El total de ventas para el a??o {} es de {} articulos'.format(year,total_sales_year))
        print('El total de ingresos para el a??o {} es de {} dolares\n'.format(year,total_income_year))
        print('Los meses del a??o {} con mayores ventas son: {}'.format(year,best_months.values))

def iniciar_sesion(user,password):
    if user in users.user.values:
        if password in users.password.values:
            print('Sesion Iniciada')
            return True
        else:
            print('Contrase??a Incorrecta')
            return False
    else:
        print('Usuario Incorrecto')
        return False

def menu():
    print('#================= Bienvenido =================#')
    print('Seleccione una opcion para comenzar')
    texto = '''
            1 -> Productos mas vendidos y productos rezagados (Top n catalogo de productos con mayores/menores ventas y busquedas)
            2 -> Productos por rese??a en el servicio (Top n productos con mejores/menores rese??as)
            3 -> Total de ingresos y ventas promedio mensuales, total anual y meses con mas ventas al a??o

            0 -> Salir
            '''
    print(texto)

def exit_program():
    e = False
    while(e==False):
        out = input('Desea realizar alguna otra consulta? [y/n]  ')
        if out == 'y':
            return False
        elif out == 'n':
            print('Muchas gracias por su visita!')
            return True
        else:
            print('Seleccionaste una opcion invalida, prueba nuevamente...\n')
            time.sleep(3)


if __name__ == "__main__":
    salir = False

    # Iniciamos sesion en el sistema
    username = input('Ingrese el usuario: ') # user: admin
    password = input('Ingrese la contrase??a: ') #password: 777

    sesion = iniciar_sesion(username,password)

    if not sesion:
        salir = True

    while(salir != True):

        # Imprimimos el menu de opciones
        menu()

        try:
            caso = int(input('Ingrese la opcion: '))
        except:
            print('Ha ingresado una opcion no reconocida o invalida')
            time.sleep(3)

        if caso == 1: # Productos mas vendidos y productos rezagados (Top n catalogo de productos con mayores/menores ventas y busquedas)
            try:
                n = int(input('Ingrese el numero de ventas de productos a obtener: '))
                m = int(input('Ingrese el numero de busquedas de productos a obtener: '))
            except:
                print('Ha ingresado una opcion invalida...')
            _ = top_sales(n)
            _ = top_sales_category(n)
            _ = top_searches(m)
            _ = small_sales(n)
            _ = small_sales_category(n)
            _ = small_searches(m)
            _ = product_searches()

            salir = exit_program()

        elif caso == 2: # Productos por rese??a en el servicio (Top n productos con mejores/menores rese??as)
            try:
                n = int(input('Ingrese el numero de rese??as a obtener: '))
            except:
                print('Ha ingresado una opcion invalida...')
            _ = product_reviews(n)

            salir = exit_program()

        elif caso == 3: # Total de ingresos y ventas promedio mensuales, total anual y meses con mas ventas al a??o
            _ = sales_income()

            salir = exit_program()

        elif caso == 0: # Salida
            salir = True
            print('\nMuchas gracias por su visita!')
            
        else: #En caso de opcion erronea
            print('Opcion invalida')
