# Ontology governance framework


EXPLANATION OF HOW THE FRAMEWORK WORKS: Categories, subcategories, definitions, elements.

[PRINCIPLE 1](#principle-1-availability)

[PRINCIPLE 2](#principle-2-scope-of-the-ontology)

###  PRINCIPLES

#### Principle 1: Availability

>  The ontology and its components (such as code and documentation) are accessible to the intended users, both humans and machines.

**Sources**:
- BASF.P2, BASF.P3, OBO.P1, IOF.P4, EFSA.4.5

###  REQUIREMENTS

<details>
<summary><strong>Requirement 1: Location of the resources</strong></summary>

There MUST be defined the location where the users target will have the resources available. This location can be:
- Ontology portal or catalogue (e.g. LOV, Bioportal)
- Project specific web page (SAREF) 
- Git repository (FIBO)

<details><summary><strong>GUIDELINES</strong></summary>
Publication of ontology in Git repository: Indicate in the ontology with metadata the repository in ehich the ontology is maintained with schema:codeRepositor. </details></details>

<details>

<summary><strong>Requirement 2: Access and (re)use policies/agreements</strong></summary>
There MUST be indicated what are the terms and conditions to access the ontology resources and how to (re)use them.
<details><summary><strong>GUIDELINES</strong></summary>
It is recommended to indicate the access and (re)use conditions can be indicated at two levels: 
A) At the repository, or other location level, by adding for example a LICENSE document where the indications are written in a human-readable manner. For example: LINCENSE document in FIBO. 
B) At the resource level, adding it in a machine-readble manner. The most common practice is to choose a licence with an URI that is resolvable and supports content negotation. Some of the most common annotations to indicate the license are:

- dct:license
- dcterms:rights
- schema:license
- cc:license </details></details>

</details>


#### Principle 2: Scope of the ontology
> The ontology has a clearly defined scope with content that aligns with that scope to avoid overlapping with other ontologies and to facilitate discovery and selection by users. It should be specific enough to cover its intended domain while still allowing for extension and specialization.

**Sources**:

###  REQUIREMENTS

<details>
<summary><strong>Requirement 1: Modularity</strong></summary>

The scope of the ontology should be narrow and small enough to support modularity. 
</details>

<details><summary><strong>Requirement 2: Statement of the scope</strong></summary>
This scope has to be clearly and briefly stated, in any "manifestation" of the ontology. 

<details><summary><strong>GUIDELINES</strong></summary>
This scope should be clearly stated. A good practice is to use the annotation dcterms:abstract or rdfs:comment, where a brief and formal description of the scope and context can be added to the ontology.  </details></details>

</details>

<details><summary><strong>Requirement 3: Ontology name</strong></summary>
The title/name of the ontology must be aligned with the defined scope. 
</details>

#### Principle 2: Documentation

>  To promote transparency, traceability, and understandability, human-readable documentation of the ontology is provided. This documentation enables different users to understand all elements and procedures of the ontology lifecycle.

**Sources**:


[esta es una captura](imagen.png)
