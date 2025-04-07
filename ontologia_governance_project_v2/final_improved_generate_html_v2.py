#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML Generator for Ontology Governance Framework

This script generates an interactive HTML file from an Excel file
that contains an ontology governance framework structured in three columns:
Principles, Requirements, and Guidelines.

Usage:
    python3 final_improved_generate_html.py --input path/to/file.xlsx --output path/to/output.html

Author: Manus AI
Date: April 2025
"""

import argparse
import json
import os
import pandas as pd
import re
from datetime import datetime

def clean_text(text):
    """Clean text to avoid issues with JSON and HTML."""
    if pd.isna(text):
        return ""
    # Escape quotes and special characters for JSON
    text = str(text).replace('\\', '\\\\').replace('"', '\\"')
    return text

def generate_id(text, prefix):
    """Generate a unique ID based on text."""
    if pd.isna(text):
        return f"{prefix}_unknown"
    # Create an ID based on the first words of the text
    # Extract the identifier part (e.g., "P1", "R2")
    id_match = re.search(r'([PR][0-9]+)', text)
    if id_match:
        return f"{prefix}_{id_match.group(1).lower()}"
    
    # Fallback to using the first few words
    words = re.sub(r'[^a-zA-Z0-9\s]', '', text.split('.')[0].strip())
    words = words.lower().split()[:2]
    return f"{prefix}_{'_'.join(words)}"

def process_excel(excel_path):
    """
    Process the Excel file and generate the data structure for HTML.
    
    Args:
        excel_path: Path to the Excel file
        
    Returns:
        List of dictionaries with the governance model structure
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path)
        
        # Verify that the Excel has the necessary columns
        required_columns = ['Principle', 'Requirement', 'Guidelines']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"The Excel file does not contain the column '{col}'")
        
        # Process the data
        governance_model = []
        current_principle = None
        current_principle_data = None
        
        for idx, row in df.iterrows():
            # If there's a new principle
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
            
            # Process requirement
            if not pd.isna(row['Requirement']):
                requirement_id = generate_id(row['Requirement'], 'r')
                requirement_data = {
                    'id': requirement_id,
                    'name': clean_text(row['Requirement']),
                    'guidelines': clean_text(row['Guidelines'])
                }
                
                if current_principle_data:
                    current_principle_data['requirements'].append(requirement_data)
        
        # Add the last principle
        if current_principle_data:
            governance_model.append(current_principle_data)
        
        return governance_model
    
    except Exception as e:
        print(f"Error processing the Excel file: {str(e)}")
        raise

def generate_html(excel_path, output_path):
    """
    Generate the HTML file from Excel.
    
    Args:
        excel_path: Path to the Excel file
        output_path: Path where the generated HTML will be saved
    """
    try:
        # Process the Excel
        governance_model = process_excel(excel_path)
        
        # Convert the model to JSON to insert it in the HTML
        model_json = json.dumps(governance_model, ensure_ascii=False)
        
        # Generation date
        generation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Create HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ontology Governance Framework</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }}
        
        h1 {{
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        
        .search-container {{
            margin-bottom: 30px;
            display: flex;
            justify-content: center;
        }}
        
        #search-input {{
            width: 100%;
            max-width: 500px;
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }}
        
        .governance-model {{
            margin-bottom: 30px;
        }}
        
        .principle {{
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
        }}
        
        .principle-header {{
            background-color: #2c3e50;
            color: white;
            padding: 15px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .principle-header.partially-fulfilled {{
            background-color: #f39c12;
        }}
        
        .principle-header.fulfilled {{
            background-color: #2ecc71;
        }}
        
        .principle-content {{
            padding: 15px;
            display: none;
            background-color: #f9f9f9;
        }}
        
        .requirements-list {{
            list-style: none;
            padding-left: 0;
        }}
        
        .requirement {{
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
        }}
        
        .requirement-header {{
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .requirement-content {{
            padding: 15px;
            display: none;
            background-color: white;
        }}
        
        .guidelines {{
            margin-top: 10px;
            padding: 10px;
            background-color: #f5f5f5;
            border-radius: 4px;
        }}
        
        .checkbox-container {{
            display: flex;
            align-items: center;
            margin-right: 10px;
        }}
        
        .checkbox-container input[type="checkbox"] {{
            margin-right: 5px;
            width: 18px;
            height: 18px;
        }}
        
        .export-container {{
            margin-top: 30px;
            text-align: center;
        }}
        
        .btn {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin: 0 10px;
            transition: background-color 0.3s;
        }}
        
        .btn:hover {{
            background-color: #2980b9;
        }}
        
        .btn-pdf {{
            background-color: #e74c3c;
        }}
        
        .btn-pdf:hover {{
            background-color: #c0392b;
        }}
        
        .btn-md {{
            background-color: #2c3e50;
        }}
        
        .btn-md:hover {{
            background-color: #1a252f;
        }}
        
        .arrow {{
            transition: transform 0.3s;
        }}
        
        .rotated {{
            transform: rotate(180deg);
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}
            
            .principle-header, .requirement-header {{
                padding: 10px;
            }}
            
            .export-container {{
                display: flex;
                flex-direction: column;
            }}
            
            .btn {{
                margin: 5px 0;
            }}
        }}
        
        /* Accessibility */
        .visually-hidden {{
            position: absolute;
            width: 1px;
            height: 1px;
            margin: -1px;
            padding: 0;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            border: 0;
        }}
        
        *:focus {{
            outline: 3px solid #3498db;
            outline-offset: 2px;
        }}
        
        /* Search result styles */
        .highlight {{
            background-color: yellow;
            padding: 2px;
        }}
        
        /* Footer */
        footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 14px;
            color: #777;
        }}
        
        /* Element titles */
        .element-title {{
            font-weight: bold;
            margin-bottom: 5px;
            color: #2c3e50;
        }}
        
        .principle-title {{
            font-size: 18px;
            color: white;
        }}
        
        .requirement-title {{
            font-size: 16px;
            color: white;
        }}
        
        .guideline-title {{
            font-size: 14px;
            color: #34495e;
        }}
        
        /* Fix for long text in headers */
        .principle-header .principle-title,
        .requirement-header .requirement-title {{
            flex: 1;
            margin-left: 10px;
            white-space: normal;
            word-break: break-word;
        }}
        
        /* Component name and explanation formatting */
        .component-name {{
            font-weight: bold;
            font-size: 18px;
            display: block;
            margin-bottom: 5px;
        }}
        
        .component-explanation {{
            font-size: 14px;
            color: white;
            display: block;
        }}
        
        .requirement-name {{
            font-weight: bold;
            font-size: 16px;
            display: block;
            margin-bottom: 5px;
        }}
        
        .requirement-explanation {{
            font-size: 13px;
            color: white;
            display: block;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Ontology Governance Framework</h1>
            <p>Select framework elements to create your own governance model</p>
        </header>
        
        <div class="search-container">
            <input type="text" id="search-input" placeholder="Search in the framework..." aria-label="Search in the framework">
        </div>
        
        <div class="governance-model" id="governance-model">
            <!-- Content will be dynamically generated with JavaScript -->
        </div>
        
        <div class="export-container">
            <button id="export-pdf" class="btn btn-pdf">Export selection to PDF</button>
            <button id="export-md" class="btn btn-md">Export selection to Markdown</button>
        </div>
        
        <footer>
            <p>Generated on {generation_date}</p>
        </footer>
    </div>

    <!-- Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script>
        // Model data (generated from Excel)
        const governanceModel = {model_json};

        // Function to render the model
        function renderGovernanceModel() {{
            const modelContainer = document.getElementById('governance-model');
            modelContainer.innerHTML = '';
            
            governanceModel.forEach(principle => {{
                const principleElement = document.createElement('div');
                principleElement.className = 'principle';
                principleElement.dataset.id = principle.id;
                
                // Split principle name into name and explanation
                let principleNameParts = principle.name.split('.');
                let principleName = principleNameParts[0].trim();
                let principleExplanation = principleNameParts.slice(1).join('.').trim();
                
                const principleHeader = document.createElement('div');
                principleHeader.className = 'principle-header';
                principleHeader.innerHTML = `
                    <div class="checkbox-container">
                        <input type="checkbox" id="check-${{principle.id}}" class="principle-checkbox" data-id="${{principle.id}}" aria-label="Select principle ${{principleName}}">
                    </div>
                    <span class="principle-title">
                        <span class="component-name">Principle: ${{principleName}}</span>
                        <span class="component-explanation">${{principleExplanation}}</span>
                    </span>
                    <span class="arrow">▼</span>
                `;
                
                const principleContent = document.createElement('div');
                principleContent.className = 'principle-content';
                
                const requirementsList = document.createElement('ul');
                requirementsList.className = 'requirements-list';
                
                principle.requirements.forEach(requirement => {{
                    const requirementItem = document.createElement('li');
                    requirementItem.className = 'requirement';
                    requirementItem.dataset.id = requirement.id;
                    
                    // Split requirement name into name and explanation
                    let requirementNameParts = requirement.name.split(':');
                    let requirementName = requirementNameParts[0].trim();
                    let requirementExplanation = requirementNameParts.length > 1 ? requirementNameParts.slice(1).join(':').trim() : '';
                    
                    const requirementHeader = document.createElement('div');
                    requirementHeader.className = 'requirement-header';
                    requirementHeader.innerHTML = `
                        <div class="checkbox-container">
                            <input type="checkbox" id="check-${{requirement.id}}" class="requirement-checkbox" data-principle="${{principle.id}}" data-id="${{requirement.id}}" aria-label="Select requirement ${{requirementName}}">
                        </div>
                        <span class="requirement-title">
                            <span class="requirement-name">Requirement: ${{requirementName}}</span>
                            <span class="requirement-explanation">${{requirementExplanation}}</span>
                        </span>
                        <span class="arrow">▼</span>
                    `;
                    
                    const requirementContent = document.createElement('div');
                    requirementContent.className = 'requirement-content';
                    
                    const guidelines = document.createElement('div');
                    guidelines.className = 'guidelines';
                    guidelines.innerHTML = `
                        <h4 class="guideline-title">Guidelines:</h4>
                        <p>${{requirement.guidelines.replace(/\\n/g, '<br>')}}</p>
                    `;
                    
                    requirementContent.appendChild(guidelines);
                    requirementItem.appendChild(requirementHeader);
                    requirementItem.appendChild(requirementContent);
                    requirementsList.appendChild(requirementItem);
                }});
                
                principleContent.appendChild(requirementsList);
                principleElement.appendChild(principleHeader);
                principleElement.appendChild(principleContent);
                modelContainer.appendChild(principleElement);
            }});
            
            // Add event listeners
            addEventListeners();
        }}
        
        // Function to add event listeners
        function addEventListeners() {{
            // Toggle for principles
            document.querySelectorAll('.principle-header').forEach(header => {{
                header.addEventListener('click', function(e) {{
                    if (e.target.type !== 'checkbox') {{
                        const content = this.nextElementSibling;
                        const arrow = this.querySelector('.arrow');
                        
                        content.style.display = content.style.display === 'block' ? 'none' : 'block';
                        arrow.classList.toggle('rotated');
                    }}
                }});
            }});
            
            // Toggle for requirements
            document.querySelectorAll('.requirement-header').forEach(header => {{
                header.addEventListener('click', function(e) {{
                    if (e.target.type !== 'checkbox') {{
                        const content = this.nextElementSibling;
                        const arrow = this.querySelector('.arrow');
                        
                        content.style.display = content.style.display === 'block' ? 'none' : 'block';
                        arrow.classList.toggle('rotated');
                    }}
                }});
            }});
            
            // Principle checkboxes
            document.querySelectorAll('.principle-checkbox').forEach(checkbox => {{
                checkbox.addEventListener('change', function() {{
                    const principleId = this.dataset.id;
                    const isChecked = this.checked;
                    
                    // Select/deselect all requirements for this principle
                    document.querySelectorAll(`.requirement-checkbox[data-principle="${{principleId}}"]`).forEach(reqCheckbox => {{
                        reqCheckbox.checked = isChecked;
                    }});
                    
                    updatePrincipleStatus();
                }});
            }});
            
            // Requirement checkboxes
            document.querySelectorAll('.requirement-checkbox').forEach(checkbox => {{
                checkbox.addEventListener('change', function() {{
                    updatePrincipleStatus();
                }});
            }});
            
            // Search
            document.getElementById('search-input').addEventListener('input', function() {{
                searchModel(this.value);
            }});
            
            // Export to PDF
            document.getElementById('export-pdf').addEventListener('click', function() {{
                exportToPDF();
            }});
            
            // Export to Markdown
            document.getElementById('export-md').addEventListener('click', function() {{
                exportToMarkdown();
            }});
        }}
        
        // Function to update principle status (fulfilled, partially fulfilled)
        function updatePrincipleStatus() {{
            governanceModel.forEach(principle => {{
                const principleElement = document.querySelector(`.principle[data-id="${{principle.id}}"]`);
                const principleHeader = principleElement.querySelector('.principle-header');
                const principleCheckbox = document.getElementById(`check-${{principle.id}}`);
                
                const requirementCheckboxes = document.querySelectorAll(`.requirement-checkbox[data-principle="${{principle.id}}"]`);
                const totalRequirements = requirementCheckboxes.length;
                const checkedRequirements = Array.from(requirementCheckboxes).filter(cb => cb.checked).length;
                
                principleHeader.classList.remove('fulfilled', 'partially-fulfilled');
                
                if (checkedRequirements === totalRequirements && totalRequirements > 0) {{
                    principleHeader.classList.add('fulfilled');
                    principleCheckbox.checked = true;
                }} else if (checkedRequirements > 0) {{
                    principleHeader.classList.add('partially-fulfilled');
                    principleCheckbox.checked = false;
                }} else {{
                    principleCheckbox.checked = false;
                }}
            }});
        }}
        
        // Function to search in the model
        function searchModel(query) {{
            if (!query) {{
                // Restore normal view
                document.querySelectorAll('.principle, .requirement').forEach(el => {{
                    el.style.display = '';
                }});
                document.querySelectorAll('.highlight').forEach(el => {{
                    const text = el.textContent;
                    el.outerHTML = text;
                }});
                return;
            }}
            
            query = query.toLowerCase();
            let hasResults = false;
            
            // Hide all elements first
            document.querySelectorAll('.principle, .requirement').forEach(el => {{
                el.style.display = 'none';
            }});
            
            // Remove previous highlights
            document.querySelectorAll('.highlight').forEach(el => {{
                const text = el.textContent;
                el.outerHTML = text;
            }});
            
            // Search in principles
            governanceModel.forEach(principle => {{
                const principleElement = document.querySelector(`.principle[data-id="${{principle.id}}"]`);
                const principleText = principle.name.toLowerCase();
                let principleMatch = principleText.includes(query);
                
                // Search in requirements
                principle.requirements.forEach(requirement => {{
                    const requirementElement = document.querySelector(`.requirement[data-id="${{requirement.id}}"]`);
                    const requirementText = requirement.name.toLowerCase();
                    const guidelinesText = requirement.guidelines.toLowerCase();
                    
                    const requirementMatch = requirementText.includes(query) || guidelinesText.includes(query);
                    
                    if (requirementMatch) {{
                        requirementElement.style.display = '';
                        principleElement.style.display = '';
                        principleElement.querySelector('.principle-content').style.display = 'block';
                        requirementElement.querySelector('.requirement-content').style.display = 'block';
                        hasResults = true;
                        
                        // Highlight matching text
                        highlightText(requirementElement, query);
                    }}
                }});
                
                if (principleMatch) {{
                    principleElement.style.display = '';
                    principleElement.querySelector('.principle-content').style.display = 'block';
                    hasResults = true;
                    
                    // Highlight matching text
                    highlightText(principleElement, query);
                }}
            }});
            
            if (!hasResults) {{
                alert('No results found for your search.');
                // Restore normal view
                document.querySelectorAll('.principle, .requirement').forEach(el => {{
                    el.style.display = '';
                }});
            }}
        }}
        
        // Function to highlight text
        function highlightText(element, query) {{
            const textNodes = getTextNodes(element);
            
            textNodes.forEach(node => {{
                const text = node.nodeValue;
                const lowerText = text.toLowerCase();
                let position = lowerText.indexOf(query);
                
                if (position !== -1) {{
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
                }}
            }});
        }}
        
        // Function to get text nodes
        function getTextNodes(element) {{
            const textNodes = [];
            const walk = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
            let node;
            
            while (node = walk.nextNode()) {{
                if (node.nodeValue.trim() !== '') {{
                    textNodes.push(node);
                }}
            }}
            
            return textNodes;
        }}
        
        // Function to format text for Markdown
        function formatTextForMarkdown(text) {{
            // Replace multiple newlines with double newlines for proper paragraph breaks
            return text.replace(/\\n+/g, '\\n\\n').trim();
        }}
        
        // Function to export to Markdown
        function exportToMarkdown() {{
            let markdown = "# Ontology Governance Framework - Selection\\n\\n";
            let hasContent = false;
            
            governanceModel.forEach(principle => {{
                const principleCheckbox = document.getElementById(`check-${{principle.id}}`);
                const isPrincipleSelected = principleCheckbox.checked;
                
                // Split principle name into name and explanation
                let principleNameParts = principle.name.split('.');
                let principleName = principleNameParts[0].trim();
                let principleExplanation = principleNameParts.slice(1).join('.').trim();
                
                let hasSelectedRequirements = false;
                let requirementsMarkdown = "";
                
                principle.requirements.forEach(requirement => {{
                    const requirementCheckbox = document.getElementById(`check-${{requirement.id}}`);
                    const isRequirementSelected = requirementCheckbox && requirementCheckbox.checked;
                    
                    if (isRequirementSelected) {{
                        hasSelectedRequirements = true;
                        hasContent = true;
                        
                        // Split requirement name into name and explanation
                        let requirementNameParts = requirement.name.split(':');
                        let requirementName = requirementNameParts[0].trim();
                        let requirementExplanation = requirementNameParts.length > 1 ? requirementNameParts.slice(1).join(':').trim() : '';
                        
                        requirementsMarkdown += `## Requirement: ${{requirementName}}\\n\\n`;
                        if (requirementExplanation) {{
                            requirementsMarkdown += `${{requirementExplanation}}\\n\\n`;
                        }}
                        
                        // Format guidelines text with proper paragraph breaks
                        const formattedGuidelines = formatTextForMarkdown(requirement.guidelines);
                        requirementsMarkdown += `### Guidelines:\\n${{formattedGuidelines}}\\n\\n`;
                    }}
                }});
                
                if (isPrincipleSelected || hasSelectedRequirements) {{
                    hasContent = true;
                    markdown += `# Principle: ${{principleName}}\\n\\n`;
                    if (principleExplanation) {{
                        markdown += `${{principleExplanation}}\\n\\n`;
                    }}
                    markdown += requirementsMarkdown;
                }}
            }});
            
            // If no content selected
            if (!hasContent) {{
                markdown += "No principles or requirements have been selected.\\n";
            }}
            
            // Create a blob and download
            const blob = new Blob([markdown], {{ type: 'text/markdown' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'ontology_governance_framework.md';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}
        
        // Function to export to PDF
        function exportToPDF() {{
            // Create a new PDF document
            const {{ jsPDF }} = window.jspdf;
            const doc = new jsPDF('p', 'mm', 'a4');
            
            // Style configuration
            const pageWidth = 210;
            const margin = 20;
            const contentWidth = pageWidth - (margin * 2);
            let yPosition = 20;
            
            // Helper functions for PDF
            const addHeading = (text, level) => {{
                let fontSize = 16;
                if (level === 2) fontSize = 14;
                if (level === 3) fontSize = 12;
                
                doc.setFont('helvetica', 'bold');
                doc.setFontSize(fontSize);
                
                // Check if we need a new page
                if (yPosition > 270) {{
                    doc.addPage();
                    yPosition = 20;
                }}
                
                // Split long headings into multiple lines if needed
                const lines = doc.splitTextToSize(text, contentWidth);
                doc.text(lines, margin, yPosition);
                
                // Reduced spacing after headings
                if (level === 1) {{
                    yPosition += (lines.length * 7) + 2;
                    // Line under main title
                    doc.setDrawColor(0, 0, 0);
                    doc.line(margin, yPosition - 2, margin + contentWidth, yPosition - 2);
                    yPosition += 3;
                }} else if (level === 2) {{
                    yPosition += (lines.length * 6) + 1;
                }} else {{
                    yPosition += (lines.length * 5) + 1;
                }}
            }};
            
            const addParagraph = (text) => {{
                doc.setFont('helvetica', 'normal');
                doc.setFontSize(11);
                
                // Process text to ensure proper paragraph breaks
                const processedText = text.replace(/\\n+/g, '\\n\\n').trim();
                
                // Split text into lines that fit content width
                const lines = doc.splitTextToSize(processedText, contentWidth);
                
                // Check if we need a new page
                if (yPosition + (lines.length * 6) > 280) {{
                    doc.addPage();
                    yPosition = 20;
                }}
                
                doc.text(lines, margin, yPosition);
                
                // Calculate space needed based on actual text height with reduced spacing
                const textHeight = lines.length * 5;
                yPosition += textHeight + 5; // Reduced space after paragraphs
            }};
            
            // Document title
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(20);
            doc.text('Ontology Governance Framework', pageWidth / 2, yPosition, {{ align: 'center' }});
            yPosition += 12; // Reduced spacing
            
            // Generation date
            doc.setFont('helvetica', 'italic');
            doc.setFontSize(10);
            const today = new Date();
            const dateStr = today.toLocaleDateString();
            doc.text(`Document generated on ${{dateStr}}`, pageWidth / 2, yPosition, {{ align: 'center' }});
            yPosition += 15; // Reduced spacing
            
            // Selected Principles and Requirements section
            addHeading('Selected Principles and Requirements', 1);
            
            let principleCounter = 1;
            let hasContent = false;
            
            governanceModel.forEach(principle => {{
                const principleCheckbox = document.getElementById(`check-${{principle.id}}`);
                const isPrincipleSelected = principleCheckbox.checked;
                
                // Split principle name into name and explanation
                let principleNameParts = principle.name.split('.');
                let principleName = principleNameParts[0].trim();
                let principleExplanation = principleNameParts.slice(1).join('.').trim();
                
                // Check if there are selected requirements for this principle
                const hasSelectedRequirements = principle.requirements.some(req => {{
                    const reqCheckbox = document.getElementById(`check-${{req.id}}`);
                    return reqCheckbox && reqCheckbox.checked;
                }});
                
                if (isPrincipleSelected || hasSelectedRequirements) {{
                    hasContent = true;
                    
                    // Add principle
                    addHeading(`${{principleCounter}}. ${{principleName}}`, 2);
                    
                    // Add principle explanation if available
                    if (principleExplanation) {{
                        addParagraph(principleExplanation);
                    }}
                    
                    principleCounter++;
                    
                    let requirementCounter = 1;
                    
                    // Add selected requirements
                    principle.requirements.forEach(requirement => {{
                        const requirementCheckbox = document.getElementById(`check-${{requirement.id}}`);
                        const isRequirementSelected = requirementCheckbox && requirementCheckbox.checked;
                        
                        if (isRequirementSelected) {{
                            // Split requirement name into name and explanation
                            let requirementNameParts = requirement.name.split(':');
                            let requirementName = requirementNameParts[0].trim();
                            let requirementExplanation = requirementNameParts.length > 1 ? requirementNameParts.slice(1).join(':').trim() : '';
                            
                            addHeading(`${{principleCounter-1}}.${{requirementCounter}}. ${{requirementName}}`, 3);
                            
                            // Add requirement explanation if available
                            if (requirementExplanation) {{
                                addParagraph(requirementExplanation);
                            }}
                            
                            requirementCounter++;
                            
                            // Add guidelines with proper formatting
                            addParagraph(`Guidelines: ${{requirement.guidelines}}`);
                        }}
                    }});
                }}
            }});
            
            // If no elements selected
            if (!hasContent) {{
                addParagraph('No principles or requirements have been selected for this governance framework.');
            }}
            
            // Footer on all pages
            const totalPages = doc.internal.getNumberOfPages();
            for (let i = 1; i <= totalPages; i++) {{
                doc.setPage(i);
                doc.setFont('helvetica', 'italic');
                doc.setFontSize(8);
                doc.text(`Ontology Governance Framework - Page ${{i}} of ${{totalPages}}`, pageWidth / 2, 290, {{ align: 'center' }});
            }}
            
            // Save the PDF
            doc.save('ontology_governance_framework.pdf');
        }}
        
        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {{
            renderGovernanceModel();
        }});
    </script>
</body>
</html>
"""
        
        # Save the HTML file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"HTML successfully generated at: {output_path}")
        return True
    
    except Exception as e:
        print(f"Error generating the HTML: {str(e)}")
        return False

def main():
    """Main script function."""
    parser = argparse.ArgumentParser(description='HTML Generator for Ontology Governance Framework')
    parser.add_argument('--input', '-i', required=True, help='Path to the Excel file')
    parser.add_argument('--output', '-o', default='index.html', help='Path where the generated HTML will be saved (default: index.html)')
    
    args = parser.parse_args()
    
    # Verify that the Excel file exists
    if not os.path.isfile(args.input):
        print(f"Error: The file {args.input} does not exist")
        return 1
    
    # Generate the HTML
    success = generate_html(args.input, args.output)
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
