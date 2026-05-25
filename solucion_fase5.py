# Nombre del estudiante: Brayan Steven Beltran Zuleta 
# Grupo:213022_761
# Programa:Fundamentos de Programación 
# Código Fuente: autoría propia

# --- MÓDULOS / FUNCIONES ---
def evaluar_compromiso(duracion, clics):
    """
    Función que clasifica el compromiso de una sesión
    según la duración y la cantidad de clics.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# --- PROGRAMA PRINCIPAL ---
def main():
    # Datos Iniciales: Matriz con 5 filas [ID Cliente, Duración, Clics]
    matriz_sesiones = [
        [101, 200, 10],  # Alto ( > 180 y > 8)
        [102, 45, 2],    # Bajo ( < 60 o < 3)
        [103, 120, 5],   # Medio (Otros casos)
        [104, 250, 4],   # Medio (Duración alta pero pocos clics)
        [105, 55, 12]    # Bajo (Cumple < 60)
    ]
    
    # Encabezado del informe
    print("=" * 40)
    print("INFORME DE COMPROMISO DE SESIONES")
    print("=" * 40)
    print(f"{'ID Cliente':<15}{'Clasificación':<15}")
    print("-" * 40)
    
    # Recorrido de la matriz y salida de datos
    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        # Llamado al módulo para obtener la clasificación
        clasificacion = evaluar_compromiso(duracion, clics)
        
        # Imprimir fila del informe alineada
        print(f"{id_cliente:<15}{clasificacion:<15}")
        
    print("=" * 40)

# Ejecución del programa
if __name__ == "__main__":
    main()
