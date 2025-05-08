# Ontology Governance Interactive Viewer

## Purpose and scope

This project provides an **interactive HTML-based viewer** for exploring and exporting a governance framework for ontologies. It is intended to support the design, evaluation, and documentation of semantic artifacts in a structured and reusable way.

The resource is especially useful for:

- **Ontology developers and maintainers**: to ensure their ontologies follow well-defined governance principles.
- **Ontology reviewers**: to evaluate artifacts based on clear criteria and best practices.
- **Project managers and stakeholders**: to understand the governance processes involved in ontology development.

The scope of the governance model includes:

- **Ten core principles** of ontology governance (e.g., availability, documentation, metadata, reuse...).
- **Associated requirements** that describe what should be fulfilled to comply with each principle.
- **Detailed guidelines** offering practical advice and implementation examples for each requirement.

The interactive viewer supports selection of relevant elements, metadata input, and export everything in  **Markdown** format, enabling easy reuse in technical reports or deliverables.

---

## Governance model

The governance model is defined in JSON format and embedded directly in the HTML viewer. It is structured hierarchically as:

![Example of structure of the framework](/images/example_structure_framework.png)

- **Principles** → **Requirements** → **Guidelines**

Each item is presented in a collapsible card layout, with checkboxes for custom selection. Users can choose which parts of the model they want to export to Markdown.

Additionally, the viewer includes a metadata form where users can specify:

- Project name
- Version of the framework
- Authors
- License
- Ontologies to which the model applies

These metadata are also included in the exported Markdown file.

---

## How to use the viewer

1. **Open** the `html_gov_framework.html` file in a web browser (no server required).
2. **Enter your metadata** in the form at the top of the page.
3. **Navigate the model** using collapsible cards for each principle, requirement, and guideline.
4. **Select** the elements you want to include in your documentation using the checkboxes.
5. **Click** the “Export to Markdown” button to download a `.md` file with:
   - The project metadata
   - Only the selected governance elements

---

## Contribute

If you wish to contribute to the improvement of the model, propose new principles, or enhance the HTML interface, feel free to open an issue or start a discussion in the repository.

We welcome feedback and collaboration from the community!

---

## Authors

- Lucía Sánchez-González  
- María Poveda-Villalón  
- Oscar Corcho   

---

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  
You are free to use, modify, and distribute the contents, provided that proper attribution is maintained and the license terms are respected.

---
## How to cite this work

