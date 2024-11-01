def desglosar_curp(curp):
    tokens = {
        'Inicial del primer apellido': curp[0],
        'Vocal interna del primer apellido': curp[1],
        'Inicial del segundo apellido': curp[2],
        'Inicial del nombre': curp[3],
        'Año de nacimiento': curp[4:6],
        'Mes de nacimiento': curp[6:8],
        'Día de nacimiento': curp[8:10],
        'Género': curp[10],
        'Entidad federativa': curp[11:13],
        'Consonantes internas': curp[13:16],
        'Homoclave': curp[16],
        'Dígito verificador': curp[17]
    }
    
    contador_tokens = {key: len(value) for key, value in tokens.items()}
    return tokens, contador_tokens
