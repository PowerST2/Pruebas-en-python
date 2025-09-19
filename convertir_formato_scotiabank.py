import csv
from bs4 import BeautifulSoup
from datetime import datetime


def main():
    # Ruta del archivo HTML
    fecha_actual = datetime.now()
    dia_actual = fecha_actual.day
    mes_actual = fecha_actual.month
    file_path = f"C:\\temp\\Reporte_F_{dia_actual}{mes_actual}2025.xls"

    # Leer el contenido del archivo HTML
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        html_content = file.read()

    # Usando BeautifulSoup para parsear el HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Buscar la tabla por su ID
    table = soup.find('table', {'id': 'ctl00_cphContenido_gvReporte'})

    # Extraer el texto de la etiqueta <caption>
    caption_text = table.find('caption').get_text()

    # Determinar el valor de la columna 'banco' en función del texto de <caption>
    if 'BCP' in caption_text:
        banco = 'BCP'
    elif 'SCOTIABANK' in caption_text:
        banco = 'SCOTIABANK'
    else:
        banco = 'Otro'

    # Lista para guardar los datos de cada fila
    data = []

    # Nombres originales y nuevos de las columnas
    original_columns = ["Ruc/Dni", "Nombres", "Partida", "Nombre Partida", "Importe", "N° Operación", "Fecha Operación",
                        "Canal Pago","N°Comprobante"]
    new_columns = ["codigo", "nombrecliente", "servicio", "descripcion", "monto", "operacion", "fecha", "recibo",
                   "banco"]

    # Diccionario para mapear el servicio al código
    servicio_a_codigo = {
       "13231208":"467",
"13151101":"475",
"13231201":"464",
"13231202":"465",
"13231203":"469",
"13231204":"470",
"13231205":"468",
"13231206":"473",
"13231207":"466",
"13231209":"474",
"13231234":"520"
    }

    # Encuentra el encabezado de la tabla para obtener los nombres de las columnas
    header_row = table.find('tr')
    headers = [header.text.strip() for header in header_row.find_all('th')]

    # Índices de las columnas originales
    column_indices = [headers.index(col) for col in original_columns]

    # Encuentra todas las filas de la tabla, excepto la primera que es el encabezado
    rows = table.find_all('tr')[1:]

    # Procesa cada fila
    for row in rows:
        cols = [td.text.strip() for td in row.find_all('td')]
        # Convierte el servicio al código equivalente
        servicio = servicio_a_codigo.get(cols[column_indices[2]], cols[column_indices[2]])

        # Verifica y reformatea la fecha si es necesario
        fecha_original = cols[column_indices[6]]
        if fecha_original:
            try:
                fecha_operacion = datetime.strptime(fecha_original, '%d/%m/%Y').strftime('%Y-%m-%d')
                # Concatena el código y el servicio para crear el recibo
                recibo = cols[column_indices[0]] + servicio + 'SCO'+cols[column_indices[5]]
                # Extrae los datos de las columnas deseadas y actualiza los campos
                row_data = {
                    new_columns[i]: (fecha_operacion if i == 6 else (servicio if i == 2 else cols[column_indices[i]]))
                    for i in range(len(new_columns) - 2)}
                row_data['recibo'] = recibo
                row_data['banco'] = banco
                # Verifica si Canal Pago no está vacío antes de agregar la fila al archivo CSV
                if cols[column_indices[7]]:
                    data.append(row_data)
            except ValueError:
                continue
        else:
            continue

    # Nombre del archivo CSV donde se guardarán los datos
    csv_file = 'C:\\Temp\\datos_scotiabank.csv'

    # Escribir los datos en un archivo CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_columns)

        # Escribir el encabezado
        writer.writeheader()

        # Escribir las filas de datos
        for row in data:
            writer.writerow(row)

    print(f"Datos filtrados sin Canal Pago guardados en el archivo '{csv_file}'")


if __name__ == "__main__":
    main()