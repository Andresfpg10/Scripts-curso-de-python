# Variable que simula la respuesta de un servidor
codigo_estado = 501

# Árbol de decisiones lógicas
if codigo_estado == 200:
    print("El sistema opera correctamente.")
elif codigo_estado == 404:
    print("Alerta: Enlace roto o página no encontrada.")
elif codigo_estado == 500:
    print("Crítico: El servidor ha colapsado.")
else:
    print("Error: Estado desconocido.")


# Patrón: Event Loop (Bucle de eventos)
print("Iniciando Agente de Monitoreo...")

# 1. Definimos una "bandera" (flag) lógica.
# Mientras esta variable sea True, el agente seguirá vivo.
agente_activo = True

while agente_activo:
    # 2. input() pausa el ciclo. El agente se queda congelado aquí esperando tu orden.
    comando = input("\n[Agente] Ingresa un comando (estado / apagar): ")

    # 3. Árbol de decisiones (Lo que ya dominas)
    if comando == "estado":
        print(">> Ejecutando diagnóstico: Todos los sistemas operativos.")
    elif comando == "apagar":
        print(">> Apagando procesos. ¡Hasta luego!")
        # 4. Cambiamos la bandera a False. En la siguiente vuelta, el while se rompe.
        agente_activo = False
    else:
        print(">> Error: Comando no reconocido. Intenta de nuevo.")