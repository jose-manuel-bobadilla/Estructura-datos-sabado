import psutil

def monitor_bateria():
    if hasattr(psutil, "sensors_battery"):
        bateria = psutil.sensors_battery()
        if bateria:
            print(f"Batería: {bateria.percent}%")
            if not bateria.power_plugged and bateria.percent <= 20:
                print("⚠️ Conectar el cargador, batería baja!")
        else:
            print("No se pudo obtener información de la batería.")
    else:
        print("Esta función no es compatible en este sistema.")

# Ejecutar la función
monitor_bateria()
