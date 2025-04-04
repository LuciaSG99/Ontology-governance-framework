#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de HTML para Modelo de Gobernanza de Ontologías

Este script genera un archivo HTML interactivo a partir de un archivo Excel
que contiene un modelo de gobernanza de ontologías estructurado en tres columnas:
Principios, Requisitos y Guías.

Uso:
    python3 generate_html.py --input ruta/al/archivo.xlsx --output ruta/al/output.html

Autor: Manus AI
Fecha: Abril 2025
"""

import argparse
import json
import os
import pandas as pd
import re
from datetime import datetime

# Función de exportación a PDF mejorada (documento formal)
PDF_EXPORT_FUNCTION = """
function exportToPDF() {
    // Crear un nuevo documento PDF
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF('p', 'mm', 'a4');
    
    // Configuración de estilos
    const pageWidth = 210;
    const margin = 20;
    const contentWidth = pageWidth - (margin * 2);
    let yPosition = 20;
    
    // Funciones auxiliares para el PDF
    const addHeading = (text, level) => {
        let fontSize = 16;
        if (level === 2) fontSize = 14;
        if (level === 3) fontSize = 12;
        
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(fontSize);
        
        // Comprobar si necesitamos una nueva página
        if (yPosition > 270) {
            doc.addPage();
            yPosition = 20;
        }
        
        doc.text(text, margin, yPosition);
        yPosition += 10;
        
        // Línea debajo del título principal
        if (level === 1) {
            doc.setDrawColor(0, 0, 0);
            doc.line(margin, yPosition - 5, margin + contentWidth, yPosition - 5);
            yPosition += 5;
        }
    };
    
    const addParagraph = (text) => {
        doc.setFont('helvetica', 'normal');
        doc.setFontSize(11);
        
        // Dividir el texto en líneas que quepan en el ancho del contenido
        const lines = doc.splitTextToSize(text, contentWidth);
        
        // Comprobar si necesitamos una nueva página
        if (yPosition + (lines.length * 6) > 280) {
            doc.addPage();
            yPosition = 20;
        }
        
        doc.text(lines, margin, yPosition);
        yPosition += (lines.length * 6) + 5;
    };
    
    // Título del documento
    doc.setFont('helvetica', 'bold');
    doc.setFontSize(20);
    doc.text('Modelo de Gobernanza de Ontologías', pageWidth / 2, yPosition, { align: 'center' });
    yPosition += 15;
    
    // Fecha de generación
    doc.setFont('helvetica', 'italic');
    doc.setFontSize(10);
    const today = new Date();
    const dateStr = today.toLocaleDateString();
    doc.text(`Documento generado el ${dateStr}`, pageWidth / 2, yPosition, { align: 'center' });
    yPosition += 20;
    
    // Introducción
    addHeading('1. Introducción', 1);
    addParagraph('Este documento presenta un modelo de gobernanza para ontologías, diseñado para establecer principios, requisitos y guías que aseguren la calidad, disponibilidad y mantenimiento de recursos ontológicos. El modelo está estructurado jerárquicamente, permitiendo a las organizaciones seleccionar los elementos más relevantes para sus necesidades específicas.');
    
    // Recopilar elementos seleccionados
    const selectedPrinciples = [];
    const selectedRequirements = [];
    
    document.querySelectorAll('.principle-checkbox:checked').forEach(checkbox => {
        selectedPrinciples.push(checkbox.dataset.id);
    });
    
    document.querySelectorAll('.requirement-checkbox:checked').forEach(checkbox => {
        selectedRequirements.push(checkbox.dataset.id);
    });
    
    // Sección de principios y requisitos
    addHeading('2. Principios y Requisitos Seleccionados', 1);
    
    let principleCounter = 1;
    
    governanceModel.forEach(principle => {
        const principleCheckbox = document.getElementById(`check-${principle.id}`);
        const isPrincipleSelected = principleCheckbox.checked;
        
        // Verificar si hay requisitos seleccionados para este principio
        const hasSelectedRequirements = principle.requirements.some(req => {
            const reqCheckbox = document.getElementById(`check-${req.id}`);
            return reqCheckbox && reqCheckbox.checked;
        });
        
        if (isPrincipleSelected || hasSelectedRequirements) {
            // Añadir principio
            addHeading(`2.${principleCounter}. ${principle.name}`, 2);
            principleCounter++;
            
            let requirementCounter = 1;
            
            // Añadir requisitos seleccionados
            principle.requirements.forEach(requirement => {
                const requirementCheckbox = document.getElementById(`check-${requirement.id}`);
                const isRequirementSelected = requirementCheckbox && requirementCheckbox.checked;
                
                if (isRequirementSelected) {
                    addHeading(`2.${principleCounter-1}.${requirementCounter}. ${requirement.name}`, 3);
                    requirementCounter++;
                    
                    // Añadir guías
                    addParagraph(`Guías: ${requirement.guidelines}`);
                }
            });
        }
    });
    
    // Si no hay elementos seleccionados
    if (principleCounter === 1) {
        addParagraph('No se han seleccionado principios o requisitos para este modelo de gobernanza.');
    }
    
    // Sección de implementación
    addHeading('3. Recomendaciones de Implementación', 1);
    addParagraph('Para implementar efectivamente este modelo de gobernanza de ontologías, se recomienda:');
    yPosition += 5;
    
    // Lista de recomendaciones
    const recommendations = [
        'Establecer un equipo responsable de la gobernanza de ontologías',
        'Definir procesos claros para la revisión y aprobación de cambios',
        'Implementar herramientas de validación automática',
        'Realizar revisiones periódicas del cumplimiento',
        'Documentar decisiones y excepciones'
    ];
    
    doc.setFont('helvetica', 'normal');
    doc.setFontSize(11);
    
    recommendations.forEach(rec => {
        // Comprobar si necesitamos una nueva página
        if (yPosition > 270) {
            doc.addPage();
            yPosition = 20;
        }
        
        doc.text(`• ${rec}`, margin + 5, yPosition);
        yPosition += 8;
    });
    
    // Conclusión
    addHeading('4. Conclusión', 1);
    addParagraph('Este modelo de gobernanza de ontologías proporciona un marco flexible que puede adaptarse a diferentes contextos organizacionales y dominios de conocimiento. La implementación efectiva de estos principios y requisitos contribuirá a mejorar la calidad, interoperabilidad y mantenibilidad de los recursos ontológicos.');
    
    // Pie de página en todas las páginas
    const totalPages = doc.internal.getNumberOfPages();
    for (let i = 1; i <= totalPages; i++) {
        doc.setPage(i);
        doc.setFont('helvetica', 'italic');
        doc.setFontSize(8);
        doc.text(`Modelo de Gobernanza de Ontologías - Página ${i} de ${totalPages}`, pageWidth / 2, 290, { align: 'center' });
    }
    
    // Guardar el PDF
    doc.save('modelo_gobernanza_ontologias.pdf');
}
"""

# Plantilla HTML base
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo de Gobernanza de Ontologías</title>
    <style>
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
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: var(--font-main);
            line-height: 1.6;
            color: var(--dark-color);
            background-color: var(--light-color);
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        
        h1 {
            color: var(--secondary-color);
            margin-bottom: 10px;
        }
        
        .search-container {
            margin-bottom: 30px;
            display: flex;
            justify-content: center;
        }
        
        #search-input {
            width: 100%;
            max-width: 500px;
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        .governance-model {
            margin-bottom: 30px;
        }
        
        .principle {
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .principle-header {
            background-color: var(--secondary-color);
            color: white;
            padding: 15px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .principle-header.partially-fulfilled {
            background-color: var(--warning-color);
        }
        
        .principle-header.fulfilled {
            background-color: var(--success-color);
        }
        
        .principle-content {
            padding: 15px;
            display: none;
            background-color: #f9f9f9;
        }
        
        .principle-description {
            margin-bottom: 15px;
        }
        
        .requirements-list {
            list-style: none;
        }
        
        .requirement {
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .requirement-header {
            background-color: var(--primary-color);
            color: white;
            padding: 10px 15px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .requirement-content {
            padding: 15px;
            display: none;
            background-color: white;
        }
        
        .guidelines {
            margin-top: 10px;
            padding: 10px;
            background-color: #f5f5f5;
            border-radius: 4px;
        }
        
        .checkbox-container {
            display: flex;
            align-items: center;
            margin-right: 10px;
        }
        
        .checkbox-container input[type="checkbox"] {
            margin-right: 5px;
            width: 18px;
            height: 18px;
        }
        
        .export-container {
            margin-top: 30px;
            text-align: center;
        }
        
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin: 0 10px;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: #2980b9;
        }
        
        .btn-pdf {
            background-color: var(--accent-color);
        }
        
        .btn-pdf:hover {
            background-color: #c0392b;
        }
        
        .btn-md {
            background-color: var(--secondary-color);
        }
        
        .btn-md:hover {
            background-color: #1a252f;
        }
        
        .arrow {
            transition: transform 0.3s;
        }
        
        .rotated {
            transform: rotate(180deg);
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .principle-header, .requirement-header {
                padding: 10px;
            }
            
            .export-container {
                display: flex;
                flex-direction: column;
            }
            
            .btn {
                margin: 5px 0;
            }
        }
        
        /* Accesibilidad */
        .visually-hidden {
            position: absolute;
            width: 1px;
            height: 1px;
            margin: -1px;
            padding: 0;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            border: 0;
        }
        
        *:focus {
            outline: 3px solid var(--primary-color);
            outline-offset: 2px;
        }
        
        /* Estilos para resultados de búsqueda */
        .highlight {
            background-color: yellow;
            padding: 2px;
        }
        
        /* Footer */
        footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 14px;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Modelo de Gobernanza de Ontologías</h1>
            <p>Seleccione los elementos del modelo para crear su propio marco de gobernanza</p>
        </header>
        
        <div class="search-container">
            <input type="text" id="search-input" placeholder="Buscar en el modelo..." aria-label="Buscar en el modelo">
        </div>
        
        <div class="governance-model" id="governance-model">
            <!-- El contenido se generará dinámicamente con JavaScript -->
        </div>
        
        <div class="export-container">
            <button id="export-pdf" class="btn btn-pdf">Exportar selección a PDF</button>
            <button id="export-md" class="btn btn-md">Exportar selección a Markdown</button>
        </div>
        
        <footer>
            <p>Generado el {generation_date}</p>
        </footer>
    </div>

    <!-- Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script>
        // Datos del modelo (generados a partir del Excel)
        const governanceModel = {model_data};

        // Función para renderizar el modelo
        function renderGovernanceModel() {
            const modelContainer = document.getElementById('governance-model');
            modelContainer.innerHTML = '';
            
            governanceModel.forEach(principle => {
                const principleElement = document.createElement('div');
                principleElement.className = 'principle';
                principleElement.dataset.id = principle.id;
                
                const principleHeader = document.createElement('div');
                principleHeader.className = 'principle-header';
                principleHeader.innerHTML = `
                    <div class="checkbox-container">
                        <input type="checkbox" id="check-${{principle.id}}" class="principle-checkbox" data-id="${{principle.id}}" aria-label="Seleccionar principio ${{principle.name}}">
                        <span>${{principle.name}}</span>
                    </div>
                    <span class="arrow">▼</span>
                `;
                
                const principleContent = document.createElement('div');
                principleContent.className = 'principle-content';
                
                const requirementsList = document.createElement('ul');
                requirementsList.className = 'requirements-list';
                
                principle.requirements.forEach(requirement => {
                    const requirementItem = document.createElement('li');
                    requirementItem.className = 'requirement';
                    requirementItem.dataset.id = requirement.id;
                    
                    const requirementHeader = document.createElement('div');
                    requirementHeader.className = 'requirement-header';
                    requirementHeader.innerHTML = `
                        <div class="checkbox-container">
                            <input type="checkbox" id="check-${{requirement.id}}" class="requirement-checkbox" data-principle="${{principle.id}}" data-id="${{requirement.id}}" aria-label="Seleccionar requisito ${{requirement.name}}">
                            <span>${{requirement.name}}</span>
                        </div>
                        <span class="arrow">▼</span>
                    `;
                    
                    const requirementContent = document.createElement('div');
                    requirementContent.className = 'requirement-content';
                    
                    const guidelines = document.createElement('div');
                    guidelines.className = 'guidelines';
                    guidelines.innerHTML = `
                        <h4>Guías:</h4>
                        <p>${{requirement.guidelines.replace(/\\n/g, '<br>')}}</p>
                    `;
                    
                    requirementContent.appendChild(guidelines);
                    requirementItem.appendChild(requirementHeader);
                    requirementItem.appendChild(requirementContent);
                    requirementsList.appendChild(requirementItem);
                });
                
                principleContent.appendChild(requirementsList);
                principleElement.appendChild(principleHeader);
                principleElement.appendChild(principleContent);
                modelContainer.appendChild(principleElement);
            });
            
            // Añadir event listeners
            addEventListeners();
        }
        
        // Función para añadir event listeners
        function addEventListeners() {
            // Toggle para principios
            document.querySelectorAll('.principle-header').forEach(header => {
                header.addEventListener('click', function(e) {
                    if (e.target.type !== 'checkbox') {
                        const content = this.nextElementSibling;
                        const arrow = this.querySelector('.arrow');
                        
                        content.style.display = content.style.display === 'block' ? 'none' : 'block';
                        arrow.classList.toggle('rotated');
                    }
                });
            });
            
            // Toggle para requisitos
            document.querySelectorAll('.requirement-header').forEach(header => {
                header.addEventListener('click', function(e) {
                    if (e.target.type !== 'checkbox') {
                        const content = this.nextElementSibling;
                        const arrow = this.querySelector('.arrow');
                        
                        content.style.display = content.style.display === 'block' ? 'none' : 'block';
                        arrow.classList.toggle('rotated');
                    }
                });
            });
            
            // Checkboxes de principios
            document.querySelectorAll('.principle-checkbox').forEach(checkbox => {
                checkbox.addEventListener('change', function() {
                    const principleId = this.dataset.id;
                    const isChecked = this.checked;
                    
                    // Seleccionar/deseleccionar todos los requisitos del principio
                    document.querySelectorAll(`.requirement-checkbox[data-principle="${{principleId}}"]`).forEach(reqCheckbox => {
                        reqCheckbox.checked = isChecked;
                    });
                    
                    updatePrincipleStatus();
                });
            });
            
            // Checkboxes de requisitos
            document.querySelectorAll('.requirement-checkbox').forEach(checkbox => {
                checkbox.addEventListener('change', function() {
                    updatePrincipleStatus();
                });
            });
            
            // Búsqueda
            document.getElementById('search-input').addEventListener('input', function() {
                searchModel(this.value);
            });
            
            // Exportar a PDF
            document.getElementById('export-pdf').addEventListener('click', function() {
                exportToPDF();
            });
            
            // Exportar a Markdown
            document.getElementById('export-md').addEventListener('click', function() {
                exportToMarkdown();
            });
        }
        
        // Función para actualizar el estado de los principios (cumplido, parcialmente cumplido)
        function updatePrincipleStatus() {
            governanceModel.forEach(principle => {
                const principleElement = document.querySelector(`.principle[data-id="${{principle.id}}"]`);
                const principleHeader = principleElement.querySelector('.principle-header');
                const principleCheckbox = document.getElementById(`check-${{principle.id}}`);
                
                const requirementCheckboxes = document.querySelectorAll(`.requirement-checkbox[data-principle="${{principle.id}}"]`);
                const totalRequirements = requirementCheckboxes.length;
                const checkedRequirements = Array.from(requirementCheckboxes).filter(cb => cb.checked).length;
                
                principleHeader.classList.remove('fulfilled', 'partially-fulfilled');
                
                if (checkedRequirements === totalRequirements && totalRequirements > 0) {
                    principleHeader.classList.add('fulfilled');
                    principleCheckbox.checked = true;
                } else if (checkedRequirements > 0) {
                    principleHeader.classList.add('partially-fulfilled');
                    principleCheckbox.checked = false;
                } else {
                    principleCheckbox.checked = false;
                }
            });
        }
        
        // Función para buscar en el modelo
        function searchModel(query) {
            if (!query) {
                // Restaurar vista normal
                document.querySelectorAll('.principle, .requirement').forEach(el => {
                    el.style.display = '';
                });
                document.querySelectorAll('.highlight').forEach(el => {
                    const text = el.textContent;
                    el.outerHTML = text;
                });
                return;
            }
            
            query = query.toLowerCase();
            let hasResults = false;
            
            // Ocultar todos los elementos primero
            document.querySelectorAll('.principle, .requirement').forEach(el => {
                el.style.display = 'none';
            });
            
            // Eliminar resaltados anteriores
            document.querySelectorAll('.highlight').forEach(el => {
                const text = el.textContent;
                el.outerHTML = text;
            });
            
            // Buscar en principios
            governanceModel.forEach(principle => {
                const principleElement = document.querySelector(`.principle[data-id="${{principle.id}}"]`);
                const principleText = principle.name.toLowerCase();
                let principleMatch = principleText.includes(query);
                
                // Buscar en requisitos
                principle.requirements.forEach(requirement => {
                    const requirementElement = document.querySelector(`.requirement[data-id="${{requirement.id}}"]`);
                    const requirementText = requirement.name.toLowerCase();
                    const guidelinesText = requirement.guidelines.toLowerCase();
                    
                    const requirementMatch = requirementText.includes(query) || guidelinesText.includes(query);
                    
                    if (requirementMatch) {
                        requirementElement.style.display = '';
                        principleElement.style.display = '';
                        principleElement.querySelector('.principle-content').style.display = 'block';
                        requirementElement.querySelector('.requirement-content').style.display = 'block';
                        hasResults = true;
                        
                        // Resaltar texto coincidente
                        highlightText(requirementElement, query);
                    }
                });
                
                if (principleMatch) {
                    principleElement.style.display = '';
                    principleElement.querySelector('.principle-content').style.display = 'block';
                    hasResults = true;
                    
                    // Resaltar texto coincidente
                    highlightText(principleElement, query);
                }
            });
            
            if (!hasResults) {
                alert('No se encontraron resultados para la búsqueda.');
                // Restaurar vista normal
                document.querySelectorAll('.principle, .requirement').forEach(el => {
                    el.style.display = '';
                });
            }
        }
        
        // Función para resaltar texto
        function highlightText(element, query) {
            const textNodes = getTextNodes(element);
            
            textNodes.forEach(node => {
                const text = node.nodeValue;
                const lowerText = text.toLowerCase();
                let position = lowerText.indexOf(query);
                
                if (position !== -1) {
                    const span = document.createElement('span');
                    span.className = 'highlight';
                    
                    const before = document.createTextNode(text.substring(0, position));
                    const match = document.createTextNode(text.substring(position, position + query.length));
                    const after = document.createTextNode(text.substring(position + query.length));
                    
                    span.appendChild(match);
                    
                    const parent = node.parentNode;
                    parent.insertBefore(before, node);
                    parent.insertBefore(span, node);
                    parent.insertBefore(after, node);
                    parent.removeChild(node);
                }
            });
        }
        
        // Función para obtener nodos de texto
        function getTextNodes(element) {
            const textNodes = [];
            const walk = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
            let node;
            
            while (node = walk.nextNode()) {
                if (node.nodeValue.trim() !== '') {
                    textNodes.push(node);
                }
            }
            
            return textNodes;
        }
        
        // Función para exportar a Markdown
        function exportToMarkdown() {{
            let markdown = "# Modelo de Gobernanza de Ontologías - Selección\\n\\n";
            
            governanceModel.forEach(principle => {{
                const principleCheckbox = document.getElementById(`check-${{principle.id}}`);
                const isPrincipleSelected = principleCheckbox.checked;
                
                let hasSelectedRequirements = false;
                let requirementsMarkdown = "";
                
                principle.requirements.forEach(requirement => {{
                    const requirementCheckbox = document.getElementById(`check-${{requirement.id}}`);
                    const isRequirementSelected = requirementCheckbox.checked;
                    
                    if (isRequirementSelected) {{
                        hasSelectedRequirements = true;
                        requirementsMarkdown += `## ${{requirement.name}}\\n\\n`;
                        requirementsMarkdown += `### Guías:\\n${{requirement.guidelines}}\\n\\n`;
                    }}
                }});
                
                if (isPrincipleSelected || hasSelectedRequirements) {{
                    markdown += `# ${{principle.name}}\\n\\n`;
                    markdown += requirementsMarkdown;
                }}
            }});
            
            // Crear un blob y descargar
            const blob = new Blob([markdown], {{ type: 'text/markdown' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'modelo_gobernanza_ontologias.md';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}
        
        {pdf_export_function}
        
        // Inicializar la aplicación
        document.addEventListener('DOMContentLoaded', function() {{
            renderGovernanceModel();
        }});
    </script>
</body>
</html>
"""

def clean_text(text):
    """Limpia el texto para evitar problemas con JSON y HTML."""
    if pd.isna(text):
        return ""
    # Escapar comillas y caracteres especiales para JSON
    text = str(text).replace('\\', '\\\\').replace('"', '\\"')
    return text

def generate_id(text, prefix):
    """Genera un ID único basado en el texto."""
    if pd.isna(text):
        return f"{prefix}_unknown"
    # Crear un ID basado en las primeras palabras del texto
    words = re.sub(r'[^a-zA-Z0-9\s]', '', text.split(':')[0].strip())
    words = words.lower().split()[:2]
    return f"{prefix}_{'_'.join(words)}"

def process_excel(excel_path):
    """
    Procesa el archivo Excel y genera la estructura de datos para el HTML.
    
    Args:
        excel_path: Ruta al archivo Excel
        
    Returns:
        Lista de diccionarios con la estructura del modelo de gobernanza
    """
    try:
        # Leer el archivo Excel
        df = pd.read_excel(excel_path)
        
        # Verificar que el Excel tiene las columnas necesarias
        required_columns = ['Principle', 'Requirement', 'Guidelines']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"El archivo Excel no contiene la columna '{col}'")
        
        # Procesar los datos
        governance_model = []
        current_principle = None
        current_principle_data = None
        
        for idx, row in df.iterrows():
            # Si hay un nuevo principio
            if not pd.isna(row['Principle']):
                if current_principle_data:
                    governance_model.append(current_principle_data)
                
                principle_id = generate_id(row['Principle'], 'p')
                current_principle = row['Principle']
                current_principle_data = {
                    'id': principle_id,
                    'name': clean_text(current_principle),
                    'requirements': []
                }
            
            # Procesar requisito
            if not pd.isna(row['Requirement']):
                requirement_id = generate_id(row['Requirement'], 'r')
                requirement_data = {
                    'id': requirement_id,
                    'name': clean_text(row['Requirement']),
                    'guidelines': clean_text(row['Guidelines'])
                }
                
                if current_principle_data:
                    current_principle_data['requirements'].append(requirement_data)
        
        # Añadir el último principio
        if current_principle_data:
            governance_model.append(current_principle_data)
        
        return governance_model
    
    except Exception as e:
        print(f"Error al procesar el archivo Excel: {str(e)}")
        raise

def generate_html(excel_path, output_path):
    """
    Genera el archivo HTML a partir del Excel.
    
    Args:
        excel_path: Ruta al archivo Excel
        output_path: Ruta donde se guardará el HTML generado
    """
    try:
        # Procesar el Excel
        governance_model = process_excel(excel_path)
        
        # Convertir el modelo a JSON para insertarlo en el HTML
        model_json = json.dumps(governance_model, ensure_ascii=False)
        
        # Fecha de generación
        generation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Generar el HTML
        html_content = HTML_TEMPLATE.format(
            model_data=model_json,
            generation_date=generation_date,
            pdf_export_function=PDF_EXPORT_FUNCTION
        )
        
        # Guardar el archivo HTML
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"HTML generado correctamente en: {output_path}")
        return True
    
    except Exception as e:
        print(f"Error al generar el HTML: {str(e)}")
        return False

def main():
    """Función principal del script."""
    parser = argparse.ArgumentParser(description='Generador de HTML para Modelo de Gobernanza de Ontologías')
    parser.add_argument('--input', '-i', required=True, help='Ruta al archivo Excel')
    parser.add_argument('--output', '-o', default='index.html', help='Ruta donde se guardará el HTML generado (por defecto: index.html)')
    
    args = parser.parse_args()
    
    # Verificar que el archivo Excel existe
    if not os.path.isfile(args.input):
        print(f"Error: El archivo {args.input} no existe")
        return 1
    
    # Generar el HTML
    success = generate_html(args.input, args.output)
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
