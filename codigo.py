import pandas as pd

def cargar_vehiculos_desde_txt():
    try:
        with open('ExamenFinalAlgoritmos.txt', 'r') as file:
            lines = file.readlines()
            vehiculos_data = [line.strip().split('|') for line in lines]
        return vehiculos_data
    except FileNotFoundError:
        print("El archivo ExamenFinalAlgoritmos.txt no se encuentra.")

def guardar_vehiculos_en_excel(vehiculos_data):
    df = pd.DataFrame(vehiculos_data, columns=['Código', 'Marca', 'Modelo', 'Precio', 'Kilometraje', 'CantidadFotos'])
    try:
        df.to_excel('vehículos.xlsx', sheet_name='listado', index=False)
        print("Vehículos guardados exitosamente en vehículos.xlsx.")
    except Exception as e:
        print(f"Error al guardar vehículos: {e}")

def crear_vehiculo():
   
    pass

def editar_vehiculo():

    pass

def eliminar_vehiculo():
    pass

def listar_vehiculos():
    try:
        df = pd.read_excel('vehículos.xlsx', sheet_name='listado')
        print(df)
    except FileNotFoundError:
        print("El archivo vehículos.xlsx no existe. Aún no hay vehículos registrados.")

if __name__ == "__main__":
    vehiculos_data = cargar_vehiculos_desde_txt()

    if vehiculos_data:
        guardar_vehiculos_en_excel(vehiculos_data)


