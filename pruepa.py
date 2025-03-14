import psutil
import time

print("Monitoreando el uso del sistema durante la desfragmentación...\n")
print("CPU (%) | RAM (%) | Disco Lectura/Escritura (MB/s)")

for _ in range(10):  # Monitorea por 10 intervalos
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk_io = psutil.disk_io_counters()
    read_write = (disk_io.read_bytes + disk_io.write_bytes) / (1024 * 1024)  # Convertir a MB

    print(f"{cpu:6.1f} | {ram:6.1f} | {read_write:6.1f} MB/s")
    time.sleep(1)

          
          
