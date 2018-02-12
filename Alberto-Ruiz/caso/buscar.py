import caso
import caso.datos
import datos

def search(srchItem):
    for collection in datos.alumnos:
        #print(type(datos.alumnos))#tipo list
        for key, value in collection.items():
            if srchItem in str(value):
                print("Got it")#Lo encontramos!
                print("This is the item that matches with the parameter: ")
                print(collection.items())#Este es el registro que coincide con srchItem

