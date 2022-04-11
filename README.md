# Parser para HESAKA

Parser para extraer datos de https://www.asuncion.gov.py/hesaka

Este código es un parser para páginas escaneadas con [tesseract](https://github.com/tesseract-ocr/tesseract), aunque es probablemente compatible con otras aplicaciones de OCR que respeten el espacio blanco relativo entre las palabras detectadas.

# Cómo usar el parser

Símplemente ejecutar el script `crear_tabla.py`

```bash
python crear_tabla.py --input texto.txt --output output.xlsx --fmt excel
```

El script soporta los siguientes formatos:

* `excel` (el argumento `--output` debe tener la extensión `.xlsx`)
* `csv`
* `tsv` (por default)

Las instrucciones que incluyen como transformar el PDF de Hesaka a texto antes de usar el parser están en [este link](https://blog.torresmateo.com/manual-hesaka/).

# ¿Porqué es necesario esto?

En Paraguay existen leyes de [transparencia y acceso a la información pública](https://www.pj.gov.py/contenido/1298-acceso-a-la-informacion-publica-y-transparencia-gubernamental/1298), y en gran medida esta ley resulta en datos gubernamentales abiertos en sitios como https://datos.sfp.gov.py/data/funcionarios que se supone lista las nómina de funcionarios públicos del Paraguay. En ese caso en particular, los datos se proveed de una forma en que son filtrables y buscables con relativa facilidad. Sin embargo, algunos organismos del estado (y notablemente, la [Municipalidad de Asunción](https://www.asuncion.gov.py/)) decice crear un escenario donde la información se presenta de forma fragmentada e inconveniente. 

La Municipalidad de Asunción publica los datos de su nómina de funcionarios en el URL https://www.asuncion.gov.py/hesaka de donde se pueden descargar PDF cada mes con el detalle de las compensaciones a sus funcionarios. Lastimosamente, al menos hasta Abril del 2022, el formato de estos archivos esta deliberadamente ofuscado, pues la persona encargada de exportar esta información (posiblemente a instrucción de dirigentes municipales) lo hace codificando cada letra del PDF como un vector. Es decir, el PDF es perfectamente legible, pero no se puede interactuar con el texto de forma conveniente.
