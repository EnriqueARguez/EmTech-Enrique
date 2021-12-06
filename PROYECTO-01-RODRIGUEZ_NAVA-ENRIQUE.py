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

sales           = pd.DataFrame(data=lifestore_sales,columns=lifestore_sales_headers)
sales['date']   = pd.to_datetime(sales['date']) # Transformamos la fecha de tipo object a datetime
sales['date']   = sales.date.apply(lambda x: x.replace(year = 2020) if x.year == 2002 else x) # Cambiamos la fecha del 2002 a 2020
sales.head()

products = pd.DataFrame(data=lifestore_products,columns=lifestore_products_headers)

searches = pd.DataFrame(data=lifestore_searches,columns=lifestore_searches_headers)

#======================================================

##################################################################

def top_sales(n):
    # En caso de que no ocurra un error, la funcion nos devuelve False
    error = False

    # Se descartan aquellas ventas que fueron devoluciones
    filtro = sales['refund'] != 1
    data = sales[filtro].copy()

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
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

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
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

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
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

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')
    if n <= sales_group.shape[0]:
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

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left').groupby(by = 'category').agg(total=('total','sum'))
    if n <= sales_group.shape[0]:
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

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left').groupby(by = 'category').agg(total=('total','sum'))
    if n <= sales_group.shape[0]:
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

    sales_group = data.groupby(by = 'id_product').agg(total=('id_product','count')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left').groupby(by = 'category').agg(total=('total','sum'))
    
    data2 = sales_group.sort_values(by = 'total').reset_index()
    print('#================= Total de Busquedas por Catalogo de Producto =================#'.format(n))
    pprint(data2)
    
    return error

def product_reviews(n):
    data = sales.copy()
    error = False

    reviews = data.groupby(by = ['id_product']).agg(total_score=('score','mean')).reset_index().merge(products[['id_product','name','category']],on='id_product',how='left')

    cols_at_end = ['total_score']
    reviews = reviews[[c for c in reviews if c not in cols_at_end] + [c for c in cols_at_end if c in reviews]]

    if n <= reviews.shape[0]:
        top = reviews.nlargest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Productos con Mayor Score =================#'.format(n))
        pprint(top)
        top = reviews.groupby(by = 'category').agg(total_score=('total_score','mean')).reset_index().nlargest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Categorias con Mayor Score =================#'.format(n))
        pprint(top)
    else:
        print('El listado de valores con menores busquedas excede el dataset actual, prueba con otro valor...')
        error = True
        return error

    if n <= reviews.shape[0]:
        small = reviews.nsmallest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Productos con Menor Score =================#'.format(n))
        pprint(small)
        small = reviews.groupby(by = 'category').agg(total_score=('total_score','mean')).reset_index().nsmallest(n,columns=['total_score']).reset_index(drop=True)
        print('#================= Top {} Categorias con Menor Score =================#'.format(n))
        pprint(small)
    else:
        print('El listado de valores con menores busquedas excede el dataset actual, prueba con otro valor...')
        error = True
        return error

    return error

def sales_income():
    filtro = sales.refund != 1
    data = sales[filtro].copy()
    data = data.merge(products[['id_product','price']],on='id_product',how='left')

    total_sales = data.groupby(by=[pd.Grouper(key='date', freq='M')]).agg(sold=('id_product','count'),total_income=('price','sum')).reset_index()
    total_sales['month'] = total_sales['date'].dt.strftime('%b')
    cols_at_end = ['sold','total_income']
    total_sales = total_sales[[c for c in total_sales if c not in cols_at_end] + [c for c in cols_at_end if c in total_sales]]

    print('#================= Ingresos y Ventas Totales =================#')
    pprint(total_sales)

    print('\n')

    for year in total_sales['date'].dt.year.unique():
        total_sales_year = total_sales[total_sales['date'].dt.year == year].sold.sum()
        total_income_year = total_sales[total_sales['date'].dt.year == year].total_income.sum()
        best_months = total_sales.nlargest(4,columns='sold').reset_index(drop=True).month
        print('El total de ventas para el año {} es de {} articulos'.format(year,total_sales_year))
        print('El total de ingresos para el año {} es de {} dolares\n'.format(year,total_income_year))
        print('Los meses del año {} con mayores ventas son: {}'.format(year,best_months.values))

def iniciar_sesion(user,password):
    if user in users.user.values:
        if password in users.password.values:
            print('Sesion Iniciada')
            return True
        else:
            print('Contraseña Incorrecta')
            return False
    else:
        print('Usuario Incorrecto')
        return False

def menu():
    print('#================= Bienvenido =================#')
    print('Seleccione una opcion para comenzar')
    texto = '''
            1 -> Productos mas vendidos y productos rezagados (Top n catalogo de productos con mayores/menores ventas y busquedas)
            2 -> Productos por reseña en el servicio (Top n productos con mejores/menores reseñas)
            3 -> Total de ingresos y ventas promedio mensuales, total anual y meses con mas ventas al año

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
    username = input('Ingrese el usuario: ')
    password = input('Ingrese la contraseña: ')

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

        if caso == 1:
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

        elif caso == 2:
            try:
                n = int(input('Ingrese el numero de reseñas a obtener: '))
            except:
                print('Ha ingresado una opcion invalida...')
            _ = product_reviews(n)

            salir = exit_program()

        elif caso == 3:
            _ = sales_income()

            salir = exit_program()

        elif caso == 0:
            salir = True
            print('\nMuchas gracias por su visita!')
            
        else:
            print('Opcion invalida')
