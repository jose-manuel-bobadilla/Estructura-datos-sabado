import psutil
import time

while True:
    uso_cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_io_counters()

    print(f"CPU: {uso_cpu}% | Memoria: {memoria}% | Lectura: {disco.read_bytes / (1024 * 1024):.2f} MB | Escritura: {disco.write_bytes / (1024 * 1024):.2f} MB")
    
    time.sleep(2)  # Ajustar el intervalo según sea necesario
