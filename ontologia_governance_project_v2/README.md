# Modelo de Gobernanza de Ontologías

Este proyecto proporciona herramientas para crear y personalizar un modelo de gobernanza de ontologías mediante una interfaz web interactiva.

## Características

- Interfaz web interactiva con listas desplegables jerárquicas
- Selección individual de principios y requisitos
- Búsqueda de elementos con resaltado de resultados
- Exportación de selecciones a PDF formal y Markdown
- Indicadores visuales de cumplimiento parcial/total
- Diseño responsivo y accesible
- Script Python para generar el HTML a partir de archivos Excel

## Requisitos

Para ejecutar el script Python, necesitas:

```
Python 3.6+
pandas
openpyxl
argparse
```

Puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

### Generación del HTML

Para generar el HTML a partir de un archivo Excel:

```bash
python generate_html.py --input ruta/al/archivo.xlsx --output ruta/al/salida.html
```

Parámetros:
- `--input`, `-i`: Ruta al archivo Excel (obligatorio)
- `--output`, `-o`: Ruta donde se guardará el HTML generado (opcional, por defecto: index.html)

### Estructura del Excel

El archivo Excel debe contener las siguientes columnas:
- `Principle`: Principios del modelo de gobernanza
- `Requirement`: Requisitos asociados a cada principio
- `Guidelines`: Guías asociadas a cada requisito

Cada principio puede tener múltiples requisitos. Si un requisito pertenece al mismo principio que el anterior, la celda de `Principle` puede dejarse vacía.

### Uso de la Interfaz Web

1. Abre el archivo HTML generado en un navegador web
2. Haz clic en los principios para expandir/contraer sus requisitos
3. Selecciona los elementos deseados mediante las casillas de verificación
4. Utiliza el buscador para encontrar elementos específicos
5. Exporta tu selección a PDF o Markdown mediante los botones correspondientes

## Despliegue en GitHub Pages

Para desplegar la aplicación en GitHub Pages:

1. Crea un repositorio en GitHub
2. Sube los archivos generados (HTML, CSS, JS) al repositorio
3. Ve a la configuración del repositorio (Settings)
4. En la sección "GitHub Pages", selecciona la rama principal como fuente
5. La aplicación estará disponible en `https://[tu-usuario].github.io/[nombre-repositorio]/`

## Personalización

Puedes personalizar la apariencia de la interfaz modificando las variables CSS en el archivo HTML:

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --accent-color: #e74c3c;
    --light-color: #ecf0f1;
    --dark-color: #34495e;
    --success-color: #2ecc71;
    --warning-color: #f39c12;
    --font-main: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
```

## Licencia

Este proyecto está disponible bajo la licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos antes de enviar un pull request.
