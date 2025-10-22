"""
EJEMPLO COMPLETO DE PYTHON - CURSO DE IA
Archivo que demuestra todos los conceptos fundamentales de Python
mencionados en el curso: tipos de datos, estructuras, control de flujo,
funciones, POO, manejo de errores, list comprehensions y archivos.
"""

import math
from typing import List, Dict

# ============================================================================
# 1. TIPOS DE DATOS PRIMITIVOS Y OPERADORES
# ============================================================================

# Variables con tipos primitivos
edad = 30  # int
altura = 1.82  # float
nombre = "Ana García"  # str
es_ingeniera = True  # bool

# Operadores aritméticos
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 3
potencia = 2 ** 8

# Operadores de comparación
es_mayor = edad > 21
es_igual = nombre == "Ana García"

# Operadores lógicos
puede_ingresar = es_mayor and es_ingeniera

print("=" * 60)
print("1. TIPOS DE DATOS Y OPERADORES")
print("=" * 60)
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}m")
print(f"¿Es ingeniera?: {es_ingeniera}")
print(f"Operación: 2^8 = {potencia}")
print(f"¿Puede ingresar?: {puede_ingresar}")


# ============================================================================
# 2. ESTRUCTURAS DE DATOS
# ============================================================================

# Lista (mutable)
temperaturas = [20.5, 22.0, 19.8, 23.5, 21.0]
temperaturas.append(24.0)  # Añadir elemento
ultima_temp = temperaturas.pop()  # Quitar último

# Tupla (inmutable)
coordenadas = (10.5, 20.3, 5.0)  # x, y, z
color_rgb = (255, 128, 0)

# Diccionario (pares clave-valor)
persona = {
    'nombre': 'Carlos',
    'edad': 28,
    'profesion': 'Ingeniero',
    'ciudad': 'Madrid'
}

# Conjunto (sin duplicados)
ids_procesados = {101, 102, 103, 104}
ids_procesados.add(105)
ids_procesados.add(101)  # No se añade, ya existe

print("\n" + "=" * 60)
print("2. ESTRUCTURAS DE DATOS")
print("=" * 60)
print(f"Temperaturas: {temperaturas}")
print(f"Coordenadas (inmutable): {coordenadas}")
print(f"Persona: {persona}")
print(f"IDs únicos: {ids_procesados}")


# ============================================================================
# 3. ESTRUCTURAS DE CONTROL DE FLUJO
# ============================================================================

def evaluar_temperatura(temp: float) -> str:
    """Evalúa una temperatura y retorna un mensaje."""
    if temp < 15:
        return "Hace frío"
    elif temp < 25:
        return "Temperatura agradable"
    elif temp < 35:
        return "Hace calor"
    else:
        return "Hace mucho calor"


# Bucle for
print("\n" + "=" * 60)
print("3. CONTROL DE FLUJO - CONDICIONALES Y BUCLES")
print("=" * 60)
print("Evaluación de temperaturas:")
for temp in temperaturas:
    evaluacion = evaluar_temperatura(temp)
    print(f"  {temp}°C -> {evaluacion}")

# Bucle while con break y continue
print("\nContando hasta encontrar múltiplo de 7:")
contador = 1
while contador <= 20:
    if contador % 2 == 0:  # Saltar números pares
        contador += 1
        continue
    if contador % 7 == 0:  # Romper si es múltiplo de 7
        print(f"  ¡Encontrado! {contador} es múltiplo de 7")
        break
    print(f"  Revisando: {contador}")
    contador += 1


# ============================================================================
# 4. FUNCIONES AVANZADAS
# ============================================================================

def calcular_estadisticas(valores: List[float]) -> Dict[str, float]:
    """
    Calcula estadísticas básicas de una lista de valores.
    Demuestra: parámetros, return, y operaciones.
    """
    if not valores:
        return {'promedio': 0, 'maximo': 0, 'minimo': 0}
    
    promedio = sum(valores) / len(valores)
    return {
        'promedio': promedio,
        'maximo': max(valores),
        'minimo': min(valores),
        'cantidad': len(valores)
    }


def saludar_personas(*nombres, prefijo="Hola"):
    """
    Demuestra *args para número variable de argumentos.
    """
    for nombre in nombres:
        print(f"  {prefijo}, {nombre}!")


def crear_perfil(**datos):
    """
    Demuestra **kwargs para argumentos con nombre variable.
    """
    print("  Perfil creado con:")
    for clave, valor in datos.items():
        print(f"    - {clave}: {valor}")


print("\n" + "=" * 60)
print("4. FUNCIONES AVANZADAS")
print("=" * 60)

# Uso de función con return
stats = calcular_estadisticas(temperaturas)
print(f"Estadísticas: {stats}")

# Uso de *args
print("\nSaludos con *args:")
saludar_personas("Ana", "Carlos", "María", prefijo="Buenos días")

# Uso de **kwargs
print("\nPerfil con **kwargs:")
crear_perfil(nombre="Laura", edad=32, ciudad="Barcelona", profesion="Data Scientist")


# ============================================================================
# 5. PROGRAMACIÓN ORIENTADA A OBJETOS
# ============================================================================

class Vehiculo:
    """Clase base que representa un vehículo genérico."""
    
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self._velocidad_actual = 0  # Atributo privado (encapsulamiento)
        self._encendido = False
    
    def arrancar(self):
        """Método para arrancar el vehículo."""
        if not self._encendido:
            self._encendido = True
            return f"{self.marca} {self.modelo} arrancado"
        return "Ya está encendido"
    
    def acelerar(self, incremento: int):
        """Método para acelerar."""
        if self._encendido:
            self._velocidad_actual += incremento
            return f"Acelerando... Velocidad: {self._velocidad_actual} km/h"
        return "Primero debes arrancar el vehículo"
    
    def frenar(self):
        """Método para frenar."""
        self._velocidad_actual = 0
        return "Vehículo detenido"
    
    def moverse(self):
        """Método para polimorfismo."""
        return "El vehículo se mueve sobre ruedas"
    
    def __str__(self):
        """Representación en string del objeto."""
        return f"{self.marca} {self.modelo} ({self.año})"


class CocheDeportivo(Vehiculo):
    """Clase que hereda de Vehiculo y añade funcionalidad turbo."""
    
    def __init__(self, marca: str, modelo: str, año: int, potencia_turbo: int):
        super().__init__(marca, modelo, año)  # Llamar al constructor padre
        self.potencia_turbo = potencia_turbo
        self._turbo_activo = False
    
    def activar_turbo(self):
        """Método adicional específico de CocheDeportivo."""
        if self._encendido and self._velocidad_actual > 50:
            self._turbo_activo = True
            self._velocidad_actual += self.potencia_turbo
            return f"¡TURBO ACTIVADO! +{self.potencia_turbo} km/h. Velocidad: {self._velocidad_actual} km/h"
        return "Necesitas ir a más de 50 km/h con el motor encendido"


class Barco:
    """Clase diferente para demostrar polimorfismo."""
    
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def moverse(self):
        """Mismo método que Vehiculo, pero comportamiento diferente."""
        return "El barco navega sobre el agua"


print("\n" + "=" * 60)
print("5. PROGRAMACIÓN ORIENTADA A OBJETOS")
print("=" * 60)

# Crear objetos
coche_normal = Vehiculo("Toyota", "Corolla", 2020)
coche_deportivo = CocheDeportivo("Ferrari", "F8 Tributo", 2023, 50)
barco = Barco("Nautilus")

# Usar objetos
print(f"\nCoche normal: {coche_normal}")
print(coche_normal.arrancar())
print(coche_normal.acelerar(60))

print(f"\nCoche deportivo: {coche_deportivo}")
print(coche_deportivo.arrancar())
print(coche_deportivo.acelerar(60))
print(coche_deportivo.activar_turbo())

# Demostrar polimorfismo
print("\nPolimorfismo (mismo método, diferente comportamiento):")
vehiculos = [coche_normal, barco]
for v in vehiculos:
    print(f"  {v.moverse()}")


# ============================================================================
# 6. MANEJO DE ERRORES Y EXCEPCIONES
# ============================================================================

def dividir_seguro(a: float, b: float) -> float:
    """Demuestra manejo de excepciones con try/except/finally."""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("  ⚠️ Error: No se puede dividir entre cero")
        return 0.0
    except TypeError:
        print("  ⚠️ Error: Los valores deben ser números")
        return 0.0
    finally:
        print(f"  ℹ️ Operación de división finalizada")


def leer_temperatura_usuario():
    """Demuestra manejo de errores con input del usuario."""
    try:
        # Nota: input() comentado para no requerir interacción
        # En un uso real, descomentarías esta línea:
        # temp = float(input("Ingresa temperatura: "))
        
        # Para el ejemplo, simulamos un valor
        temp = 25.5
        print(f"  Temperatura ingresada: {temp}°C")
        return temp
    except ValueError:
        print("  ⚠️ Error: Debes ingresar un número válido")
        return None
    except Exception as e:
        print(f"  ⚠️ Error inesperado: {e}")
        return None


print("\n" + "=" * 60)
print("6. MANEJO DE ERRORES Y EXCEPCIONES")
print("=" * 60)

print("\nDivisión segura 10 / 2:")
resultado1 = dividir_seguro(10, 2)
print(f"  Resultado: {resultado1}")

print("\nDivisión segura 10 / 0:")
resultado2 = dividir_seguro(10, 0)

print("\nLectura de temperatura con validación:")
temp_usuario = leer_temperatura_usuario()


# ============================================================================
# 7. LIST COMPREHENSIONS
# ============================================================================

print("\n" + "=" * 60)
print("7. LIST COMPREHENSIONS (COMPRENSIÓN DE LISTAS)")
print("=" * 60)

# Forma tradicional vs comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cuadrados de todos los números
cuadrados = [n ** 2 for n in numeros]
print(f"\nCuadrados: {cuadrados}")

# Solo números pares
pares = [n for n in numeros if n % 2 == 0]
print(f"Números pares: {pares}")

# Cuadrados de números impares mayores que 3
cuadrados_impares = [n ** 2 for n in numeros if n % 2 != 0 and n > 3]
print(f"Cuadrados de impares > 3: {cuadrados_impares}")

# Dictionary comprehension
cuadrados_dict = {n: n ** 2 for n in numeros if n <= 5}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# Set comprehension
multiplos_3 = {n * 3 for n in range(1, 8)}
print(f"Múltiplos de 3: {multiplos_3}")


# ============================================================================
# 8. MANEJO DE ARCHIVOS
# ============================================================================

def guardar_datos_en_archivo(nombre_archivo: str, datos: List[Dict]):
    """Escribe datos en un archivo de texto."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("REPORTE DE DATOS\n")
            archivo.write("=" * 40 + "\n\n")
            
            for i, dato in enumerate(datos, 1):
                archivo.write(f"Registro {i}:\n")
                for clave, valor in dato.items():
                    archivo.write(f"  {clave}: {valor}\n")
                archivo.write("\n")
        
        return f"✓ Archivo '{nombre_archivo}' guardado correctamente"
    
    except IOError as e:
        return f"✗ Error al guardar archivo: {e}"
    
    except Exception as e:
        return f"✗ Error inesperado: {e}"


def leer_archivo(nombre_archivo: str) -> str:
    """Lee y retorna el contenido de un archivo."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    
    except FileNotFoundError:
        return f"✗ El archivo '{nombre_archivo}' no existe"
    
    except Exception as e:
        return f"✗ Error al leer archivo: {e}"


print("\n" + "=" * 60)
print("8. MANEJO DE ARCHIVOS")
print("=" * 60)

# Preparar datos para guardar
datos_experimento = [
    {'sensor': 'A1', 'temperatura': 22.5, 'humedad': 65},
    {'sensor': 'B2', 'temperatura': 23.1, 'humedad': 62},
    {'sensor': 'C3', 'temperatura': 21.8, 'humedad': 68}
]

# Escribir archivo
nombre_archivo = 'datos_ejemplo.txt'
resultado_escritura = guardar_datos_en_archivo(nombre_archivo, datos_experimento)
print(f"\n{resultado_escritura}")

# Leer archivo
print(f"\nContenido del archivo '{nombre_archivo}':")
print("-" * 40)
contenido = leer_archivo(nombre_archivo)
print(contenido)


# ============================================================================
# 9. EJEMPLO INTEGRADOR COMPLETO
# ============================================================================

class SistemaMonitoreoTemperatura:
    """
    Clase que integra múltiples conceptos:
    - POO (clase con atributos y métodos)
    - Estructuras de datos (listas, diccionarios)
    - Manejo de excepciones
    - List comprehensions
    - Manejo de archivos
    """
    
    def __init__(self, nombre_sistema: str, umbral_critico: float = 30.0):
        self.nombre = nombre_sistema
        self.umbral_critico = umbral_critico
        self.lecturas = []
        self._ids_alertas = set()
    
    def agregar_lectura(self, sensor_id: str, temperatura: float, ubicacion: str):
        """Agrega una lectura de temperatura al sistema."""
        try:
            lectura = {
                'id': sensor_id,
                'temperatura': temperatura,
                'ubicacion': ubicacion,
                'alerta': temperatura > self.umbral_critico
            }
            
            self.lecturas.append(lectura)
            
            if lectura['alerta']:
                self._ids_alertas.add(sensor_id)
            
            return True
        
        except Exception as e:
            print(f"Error al agregar lectura: {e}")
            return False
    
    def obtener_lecturas_criticas(self) -> List[Dict]:
        """Usa list comprehension para filtrar lecturas críticas."""
        return [l for l in self.lecturas if l['alerta']]
    
    def calcular_promedio(self) -> float:
        """Calcula el promedio de temperaturas con manejo de errores."""
        try:
            if not self.lecturas:
                return 0.0
            
            temperaturas = [l['temperatura'] for l in self.lecturas]
            return sum(temperaturas) / len(temperaturas)
        
        except Exception as e:
            print(f"Error al calcular promedio: {e}")
            return 0.0
    
    def generar_reporte(self, nombre_archivo: str = 'reporte_temperaturas.txt'):
        """Genera un reporte y lo guarda en archivo."""
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write(f"REPORTE DEL SISTEMA: {self.nombre}\n")
                f.write("=" * 50 + "\n\n")
                
                f.write(f"Total de lecturas: {len(self.lecturas)}\n")
                f.write(f"Temperatura promedio: {self.calcular_promedio():.2f}°C\n")
                f.write(f"Umbral crítico: {self.umbral_critico}°C\n")
                f.write(f"Sensores con alerta: {len(self._ids_alertas)}\n\n")
                
                criticas = self.obtener_lecturas_criticas()
                if criticas:
                    f.write("LECTURAS CRÍTICAS:\n")
                    f.write("-" * 50 + "\n")
                    for lectura in criticas:
                        f.write(f"  Sensor {lectura['id']} en {lectura['ubicacion']}: ")
                        f.write(f"{lectura['temperatura']}°C ⚠️\n")
                else:
                    f.write("No hay lecturas críticas.\n")
                
                f.write("\n" + "=" * 50 + "\n")
            
            return f"✓ Reporte generado: {nombre_archivo}"
        
        except Exception as e:
            return f"✗ Error al generar reporte: {e}"
    
    def __str__(self):
        return f"Sistema '{self.nombre}' - {len(self.lecturas)} lecturas, {len(self._ids_alertas)} alertas"


print("\n" + "=" * 60)
print("9. EJEMPLO INTEGRADOR COMPLETO")
print("=" * 60)

# Crear sistema de monitoreo
sistema = SistemaMonitoreoTemperatura("Planta Industrial", umbral_critico=28.0)

# Agregar lecturas de diferentes sensores
lecturas_sensores = [
    ('S001', 22.5, 'Almacén A'),
    ('S002', 26.3, 'Sala de Servidores'),
    ('S003', 31.2, 'Zona de Producción'),
    ('S004', 24.8, 'Oficinas'),
    ('S005', 29.5, 'Calderas'),
    ('S006', 23.1, 'Almacén B')
]

print(f"\n{sistema}")
print("\nAgregando lecturas al sistema...")
for sensor_id, temp, ubicacion in lecturas_sensores:
    sistema.agregar_lectura(sensor_id, temp, ubicacion)
    print(f"  ✓ Sensor {sensor_id}: {temp}°C en {ubicacion}")

# Obtener estadísticas
print(f"\nTemperatura promedio: {sistema.calcular_promedio():.2f}°C")

# Obtener lecturas críticas
criticas = sistema.obtener_lecturas_criticas()
print(f"\nLecturas críticas (>{sistema.umbral_critico}°C): {len(criticas)}")
for lectura in criticas:
    print(f"  ⚠️ {lectura['id']} - {lectura['temperatura']}°C en {lectura['ubicacion']}")

# Generar reporte
resultado_reporte = sistema.generar_reporte()
print(f"\n{resultado_reporte}")


# ============================================================================
# CONCLUSIÓN
# ============================================================================

print("\n" + "=" * 60)
print("RESUMEN DE CONCEPTOS DEMOSTRADOS")
print("=" * 60)
print("""
✓ Tipos de datos primitivos: int, float, str, bool
✓ Operadores: aritméticos, comparación, lógicos
✓ Estructuras de datos: listas, tuplas, diccionarios, conjuntos
✓ Control de flujo: if/elif/else
✓ Bucles: for, while, break, continue
✓ Funciones: def, return, *args, **kwargs
✓ Programación Orientada a Objetos: clases, herencia, encapsulamiento
✓ Manejo de excepciones: try/except/finally
✓ List comprehensions
✓ Manejo de archivos: with open()
✓ Integración de conceptos en un sistema completo

Este código demuestra todos los conceptos fundamentales de Python
necesarios para comenzar con Inteligencia Artificial.
""")

print("=" * 60)
print("Fin del ejemplo - El Próximo Framework en Ingeniería")
print("=" * 60)

