import re

def parse_line(line):
    """
    La estructura de la gran mayoría de las líneas es:
    
    <cedula> <nombre>\s{2,}<relacion_laboral>\s{2,}<monto> <concepto>\s{2,}<dependencia>\s{2,}[cargo]\s{2,}[anho_ingreso]
    
    donde:
    <campo> representa un campo obligatorio
    [campo] es un campo opcional
    
    existen irregularidades, aunque afortunadamente es en [cargo] (a veces el cargo en sí tiene separaciones de más de un espacio)
    
    """
    cedula = nombre = relacion_laboral = monto = concepto = dependencia = cargo = anho_ingreso = None
    line = line.strip()

    campos_2e = re.split("\s{2,}", line)
    if len(campos_2e) > 5:
        cedula, nombre = campos_2e[0].split(maxsplit=1)
        relacion_laboral = campos_2e[1]
        monto, concepto = campos_2e[2].split(maxsplit=1)
        dependencia = campos_2e[3]
        cargo = " ".join(campos_2e[4:-1])
        anho_ingreso = campos_2e[-1]

        try:
            monto = int(monto)
        except ValueError:
            print("Linea con error")
            print(line)

    return cedula, nombre, relacion_laboral, monto, concepto, dependencia, cargo, anho_ingreso

def parse_file_municipalidad(file):
    data = {k:[] for k in ["cedula", "nombre", "relacion laboral", "monto", "concepto", "dependencia", "cargo", "anho ingreso"]}
    for line in open(file, encoding="Latin-1"):
        cedula, nombre, relacion_laboral, monto, concepto, dependencia, cargo, anho_ingreso = parse_line(line)
        if cedula:
            data["cedula"].append(cedula)
            data["nombre"].append(nombre)
            data["relacion laboral"].append(relacion_laboral)
            data["monto"].append(monto)
            data["concepto"].append(concepto)
            data["dependencia"].append(dependencia)
            data["cargo"].append(cargo)
            data["anho ingreso"].append(anho_ingreso)
    return data
