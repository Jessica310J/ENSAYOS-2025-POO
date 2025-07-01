import calendar
from datetime import datetime

# Obtener la fecha actual
hoy = datetime.now()
fecha_actual = hoy.strftime("%d/%m/%Y")

# Definir el año y mes
yy = 2080  # año
mm = 8     # mes

# Calcular la edad en la fecha especificada
nacimiento = datetime(2004, 8, 24)  # Cambia esto a la fecha de nacimiento deseada
edad_en_2080 = (datetime(yy, mm, 1) - nacimiento).days // 365



# Mostrar el calendario y la información
print(f"Fecha actual: {fecha_actual}")
print(f"Calendario de {calendar.month_name[mm]} {yy}:")
print(calendar.month(yy, mm))
print(f"Edad en {calendar.month_name[mm]} {yy}: {edad_en_2080} años")
