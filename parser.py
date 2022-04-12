import re


def test_int_field(line, field, splits, field_name):
    try:
        field = int(field)
    except ValueError:
        try:
            ind = field.find("/")
            subst_bar = "7"
            if ind != -1:
                if ind != 0:
                    if field[ind-1] == "7":
                        subst_bar = ""
                if ind < len(field) - 1:
                    if field[ind+1] == "7":
                        subst_bar = ""
            field = int(field.replace("/", subst_bar).replace(".",""))
        except ValueError:
            print(f"Linea con error en {field_name}")
            print(line)
            print(field)
            print(splits)
    return field


def unmerge_concepto(concepto):
    if "DIR" in concepto:
        unmerge = concepto.replace("DIR", "       DIR")
    elif "INTENDENCIA" in concepto:
        unmerge = concepto.replace("INTENDENCIA", "      INTENDENCIA")
    elif "SECRETARIA" in concepto:
        unmerge = concepto.replace("SECRETARIA", "      SECRETARIA")
    else:
        print(line)
        print(f"[{concepto}], {dependencia}, {anho_ingreso}")
    return re.split("\s{2,}", unmerge)


def parse_line(line):
    """
    La estructura de la gran mayoría de las líneas es:
    
    <cedula> <nombre>\s{2,}<relacion_laboral>\s{2,}<monto> <concepto>\s{2,}<dependencia>\s{2,}[cargo]\s{2,}[anho_ingreso]
    
    donde:
    <campo> representa un campo obligatorio
    [campo] es un campo opcional
    
    existen irregularidades, que se explican en los comentarios
    
    """
    cedula = nombre = relacion_laboral = monto = concepto = dependencia = cargo = anho_ingreso = None
    line = line.strip()

    campos_2e = re.split("\s{2,}", line)
    if len(campos_2e) >= 4:
        index_concepto = 2
        cedula, nombre = campos_2e[0].split(maxsplit=1)
        relacion_laboral = campos_2e[1]
        try:
            monto, concepto = campos_2e[2].split(maxsplit=1)
        except ValueError:
            nombre = f"{nombre} {campos_2e[1]}"
            relacion_laboral = campos_2e[2]
            monto, concepto = campos_2e[3].split(maxsplit=1)
            index_concepto = 3
        # a veces el concepto y la dependencia 
        dependencia = campos_2e[index_concepto+1]
        cargo = " ".join(campos_2e[index_concepto+2:-1])
        anho_ingreso = campos_2e[-1]

        # TODO: hacer un refactor de esto con un mejor autómata.
        if len(campos_2e) == 4: # este caso se da si no hay separación entre el concepto y la dependencia.
            concepto, dependencia = unmerge_concepto(concepto)
        # esta solución no es muy general, pero captura los casos que encontré en las imágenes hasta ahora
        if dependencia in ["AUXILIAR", "ABOGADO", "ANALISTA DE CONTRATOS", "COORDINADOR", "DIRECTOR","SECRETARIO",
                                            "TECNICO", "CAJERO", "JEFE UNIDAD", "CONTADOR PUBLICO",
                                            "RECEPCIONISTA", 'ASISTENTE', 'JEFE DEPARTAMENTO',
                                            "LIQUIDADOR","OPERADOR DE COMPUTADORA","CHOFER" ]:
            cargo = dependencia
            concepto, dependencia = unmerge_concepto(concepto)
            
        # intento de convertir las cedulas, montos y años en enteros
        monto = test_int_field(line, monto, campos_2e, "monto")
        cedula = test_int_field(line, cedula, campos_2e, "cedula")
        anho_ingreso = test_int_field(line, anho_ingreso, campos_2e, "anho_ingreso")

    return cedula, nombre, relacion_laboral, monto, concepto, dependencia, cargo, anho_ingreso


def parse_file_municipalidad(file, call=parse_line):
    data = {k:[] for k in ["cedula", "nombre", "relacion laboral", "monto", "concepto", "dependencia", "cargo", "anho ingreso"]}
    skipped_lines = []
    for line in open(file, encoding="Latin-1"):
        cedula, nombre, relacion_laboral, monto, concepto, dependencia, cargo, anho_ingreso = call(line)
        if cedula:
            data["cedula"].append(cedula)
            data["nombre"].append(nombre)
            data["relacion laboral"].append(relacion_laboral)
            data["monto"].append(monto)
            data["concepto"].append(concepto)
            data["dependencia"].append(dependencia)
            data["cargo"].append(cargo)
            data["anho ingreso"].append(anho_ingreso)
        else:
            skipped_lines.append(line)
    return data, skipped_lines
