import re

# Expresiones regulares para cada sección de la CURP
SECCIONES_REGEX = {
    'Inicial del primer apellido': r'^[A-Z]$',
    'Vocal interna del primer apellido': r'^[AEIOU]$',
    'Inicial del segundo apellido': r'^[A-Z]$',
    'Inicial del nombre': r'^[A-Z]$',
    'Año de nacimiento': r'^\d{2}$',
    'Mes de nacimiento': r'^(0[1-9]|1[0-2])$',
    'Día de nacimiento': r'^(0[1-9]|[12]\d|3[01])$',
    'Género': r'^[HM]$',
    'Entidad federativa': r'^(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)$',
    'Consonantes internas': r'^[B-DF-HJ-NP-TV-Z]{3}$',
    'Homoclave': r'^[0-9A-Z]$',
    'Dígito verificador': r'^\d$'
}

def es_anio_bisiesto(anio):
    """Verifica si un año es bisiesto."""
    anio = int(anio)
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def analizar_curp(curp):
    if len(curp) != 18:
        return f"Error: La CURP '{curp}' debe tener exactamente 18 caracteres."
    
    errores = []
    
    # Análisis de cada sección
    if not re.match(SECCIONES_REGEX['Inicial del primer apellido'], curp[0]):
        errores.append(f"Error en la sección 1 (Inicial del primer apellido): '{curp[0]}' debe ser una letra mayúscula.")
    if not re.match(SECCIONES_REGEX['Vocal interna del primer apellido'], curp[1]):
        errores.append(f"Error en la sección 2 (Vocal interna del primer apellido): '{curp[1]}' debe ser una vocal mayúscula.")
    if not re.match(SECCIONES_REGEX['Inicial del segundo apellido'], curp[2]):
        errores.append(f"Error en la sección 3 (Inicial del segundo apellido): '{curp[2]}' debe ser una letra mayúscula.")
    if not re.match(SECCIONES_REGEX['Inicial del nombre'], curp[3]):
        errores.append(f"Error en la sección 4 (Inicial del nombre): '{curp[3]}' debe ser una letra mayúscula.")
    if not re.match(SECCIONES_REGEX['Año de nacimiento'], curp[4:6]):
        errores.append(f"Error en la sección 5 (Año de nacimiento): '{curp[4:6]}' debe ser un año válido (dos dígitos).")
    
    # Validación del año, mes y día
    anio_nacimiento = int(curp[4:6]) + 2000  # Asumimos que todos los años son del 2000 en adelante
    mes_nacimiento = int(curp[6:8])
    dia_nacimiento = int(curp[8:10])

    if not re.match(SECCIONES_REGEX['Mes de nacimiento'], curp[6:8]):
        errores.append(f"Error en la sección 6 (Mes de nacimiento): '{curp[6:8]}' debe ser un mes válido (01-12).")
    
    if mes_nacimiento == 2:  # Febrero
        if dia_nacimiento == 29 and not es_anio_bisiesto(anio_nacimiento):
            errores.append("Error en la sección 7 (Día de nacimiento): El día 29 de febrero solo es válido en años bisiestos.")
        elif dia_nacimiento > 29:
            errores.append("Error en la sección 7 (Día de nacimiento): Febrero solo tiene 28 o 29 días.")
    elif dia_nacimiento > 31:  # Validar días para otros meses
        errores.append(f"Error en la sección 7 (Día de nacimiento): '{curp[8:10]}' no es un día válido.")

    if not re.match(SECCIONES_REGEX['Género'], curp[10]):
        errores.append(f"Error en la sección 8 (Género): '{curp[10]}' debe ser 'H' o 'M'.")
    if not re.match(SECCIONES_REGEX['Entidad federativa'], curp[11:13]):
        errores.append(f"Error en la sección 9 (Entidad federativa): '{curp[11:13]}' no corresponde a una entidad válida.")
    if not re.match(SECCIONES_REGEX['Consonantes internas'], curp[13:16]):
        errores.append(f"Error en la sección 10 (Consonantes internas): '{curp[13:16]}' debe contener 3 consonantes mayúsculas.")
    if not re.match(SECCIONES_REGEX['Homoclave'], curp[16]):
        errores.append(f"Error en la sección 11 (Homoclave): '{curp[16]}' debe ser un carácter alfanumérico.")
    if not re.match(SECCIONES_REGEX['Dígito verificador'], curp[17]):
        errores.append(f"Error en la sección 12 (Dígito verificador): '{curp[17]}' debe ser un dígito.")

    if errores:
        return "\n".join(errores)
    
    return "La CURP es válida."
