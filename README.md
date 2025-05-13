# Ontology Governance Framework Interactive Web

## Purpose and scope

This project provides an **Ontology Governance Framework HTML-based viewer** for exploring and exporting a governance framework for ontologies. It is intended to support the design and documentation of semantic artifacts in a structured and reusable way.

The resource is especially useful for:

- **Ontology developers and maintainers**: to ensure their ontologies follow well-defined governance principles.
- **Ontology reviewers**: to evaluate artifacts based on clear criteria and best practices.
- **Project managers and stakeholders**: to understand the governance processes involved in ontology development.

The scope of the governance model includes:

- **Ten core principles** of ontology governance (e.g., availability, documentation, metadata, reuse...).
- **Associated requirements** that describe what should be fulfilled to comply with each principle.
- **Detailed guidelines** offering practical advice and implementation examples for each requirement.

The interactive viewer supports selection of relevant elements, metadata input, and export everything in  **Markdown** format, enabling easy reuse. 

---

## Governance Framework

The governance model is defined in JSON format (file gov_framework.json) and embedded directly in the HTML viewer. It is structured hierarchically as:

![Example of structure of the framework](/images/example_structure_framework.png)

- **Principles** → **Requirements** → **Guidelines**

Each item is presented in a collapsible card layout, with checkboxes for custom selection. Users can choose which parts of the model they want to export to Markdown.

Additionally, at the beginning of the app, the user can add metadata such as:

- Project name
- Version of the framework
- Authors
- License
- Ontologies to which the model applies

These metadata are also included in the exported Markdown file.

---

## How to use the tool

1. You can use the app directly going to our **GitHub pages**: https://oeg-upm.github.io/Ontology-governance-framework/ or you can download the HTML file **"index.html"** and use the app locally (since the framework is already embedded in the HTML).
2. **Enter your metadata** in the form at the top of the page.
3. **Navigate the framework** using the collapsible elements for each principle, requirement, and guideline.
4. **Select** the elements you want to include in your documentation using the checkboxes.
5. **Click** the “Export to Markdown” button to download a `.md` file with:
   - The project metadata
   - Only the selected governance elements

> ⚠️ WARNING! The tool forces the hierarchy of elements in the frameworks to be followed. Therefore, if the requirements or guidelines are selected without having selected their parent elements (the corresponding principles and requirements), these elements will not be exported and will not be seen in the markdown file. For example, if Principle 1 and Guide G3.1.1 are selected, only Principle 1 will be seen in the markdown file. To see the G3.1.1, you need to select also Principle 3 and Requirement R.3.1.

---

## Contribute

If you wish to contribute to the improvement of the framework, propose new principles, or enhance the HTML interface, feel free to open an issue or start a discussion in the repository :)

We welcome feedback and collaboration from the community!

---

## Authors

- [Lucía Sánchez González](https://github.com/LuciaSG99)
- [María Poveda Villalón](https://github.com/mariapoveda)
- [Oscar Corcho](https://github.com/ocorcho)  

---

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  
You are free to use, modify, and distribute the contents, provided that proper attribution is maintained and the license terms are respected.

---
## How to cite this work

Lucia Sanchez-Gonzalez, Maria Poveda-Villalon, and Oscar Corcho. Ontology Governance Framework and Design Tool. May 2025. Available at [GitHub](https://github.com/LuciaSG99/Ontology-governance-framework).
