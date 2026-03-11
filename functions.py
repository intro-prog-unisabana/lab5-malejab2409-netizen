def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    total_suma = sum(calificaciones)
    cantidad = len (calificaciones)
    promedio = total_suma/cantidad
    return float(promedio)
calificaciones = [85, 92, 78]
promedio = promedio_estudiante(calificaciones)
print(f"El promedio es:{promedio}") 