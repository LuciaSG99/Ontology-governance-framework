# Ontology governance framework

*A Structured Approach to Ontology Governance:
Harmonizing Existing Practices*

EXPLANATION OF HOW THE FRAMEWORK WORKS: Categories, subcategories, definitions, elements.

[CONTEXTUALIZATION](#contextualization)

[PRINCIPLE 1 - AVAILABILITY](#principle-1-availability)

[PRINCIPLE 2 - SCOPE OF THE ONTOLOGY](#principle-2-scope-of-the-ontology)

[PRINCIPLE 3 - DOCUMENTATION](#principle-3-documentation)

[PRINCIPLE 4 - METADATA](#principle-4-metadata)

[TECHNICAL](#technical)

[PRINCIPLE 5 - IDENTIFIERS](#principle-5-identifiers)

[PRINCIPLE 6 - (RE)USABILITY](#principle-6-reusability)

[PRINCIPLE 7 - MODULARITY](#principle-7-modularity)

[PRINCIPLE 8 - FORMAT](#principle-8-format)



## CONTEXTUALIZATION

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
<details><summary><strong> GUIDELINES </strong></summary>
It is recommended to indicate the access and (re)use conditions can be indicated at two levels: 

1) At the repository, or other location level, by adding for example a LICENSE document where the indications are written in a human-readable manner. For example: LINCENSE document in FIBO. 

2) At the resource level, adding it in a machine-readble manner. The most common practice is to choose a licence with an URI that is resolvable and supports content negotation. Some of the most common annotations to indicate the license are:

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

#### Principle 3: Documentation

>  To promote transparency, traceability, and understandability, human-readable documentation of the ontology is provided. This documentation enables different users to understand all elements and procedures of the ontology lifecycle.

**Sources**:

###  REQUIREMENTS

<details>
<summary><strong>Requirement 1: Documentation embedded in the ontology</strong></summary>
 This is information is indicated in the code of the ontology using annotation properties and metadata. Here there must be detailed documentation at two levels:

1) **Ontology level**: It provides information, as metadata, for the whole ontology. It should be indicated:
* Ontology creator(s)
* Ontology maintainer(s)
* Licence
* Version
* Scope and description
2) **Term level**: It involves documentation for the individual representations. For each entity and property it should be added:
* Labels: A descriptive and unique label must be added to each term (see Identifiers)
* Textual definition: Natural language definition that facilitates the understanding of the notion. These must be unique within the ontology, and they should be avoid ambiguousity. The individual name of each element must not be used in the definition itself.
* Source of the definition: there should be noted in annotations which is the source of the textual definition.
<details><summary><strong>GUIDELINES</strong></summary>

- For guidelines on what metadata add, see Metadata section. 
- The textual definitions can be added using skos:definition or rdfs:comment
- If there is an adoption of a term from another ontology, there should be indicated using the annotation rdfs:isDefinedBy

  </details></details>

</details>

<details><summary><strong>Requirement 2: External documentation</strong></summary>

Additional information, provided in external files and documents. 
* Use cases/user stories
* Requirements (CQs)
* Diagrams: A common notation should be used to represent the different elements of the ontology. 
* SPARQL queries
* Instructions for change request
* Documentation on how to acces and use the resources 
* Documentation on deprecation policy
  
<details><summary><strong>GUIDELINES</strong></summary>

Regarding the external documentation, it can be published as static documents (e.g. a PDF document) or interactive HTML pages. Nowadays, there are tools that support the development and publication automatically of the ontology documentation using its serialization such as: 
- Ontoology: 
- WIDOCO
- LODE
- Protégé OWLDoc
- DOWL
- SpecGen
  </details></details>

</details>

#### Principle 4: Metadata
> The ontology is findable, tracked and understood by other users through its metadata

**Sources**:

## TECHNICAL

#### Principle 5: Identifiers
>

**Sources**:

#### Principle 6: (Re)usability
> To ensure interoperability and avoid duplication, it is important to commit to (re)usability. This involves two key aspects:
- **Reuse**: Whenever possible, the ontology should incorporate existing ontologies.
- **Reusability**: The ontology should be designed to facilitate its reuse by other users and stakeholders.

**Sources**:

###  REQUIREMENTS

<details>
<summary><strong>Requirement 1: Reuse specification </strong></summary>

Whenever applicable, a search should be conducted for well-known ontologies to identify any existing elements that may be useful to reuse. 

>[!note] While it is always advisable to reuse standard well-known ontologies, vocabularies, and/or terminologies, the priority must be to select those that best align with the established requirements of your ontology and meet a minimum quality standard.

<details><summary><strong>GUIDELINES</strong></summary>
It is recommended to add in an external document a brief explanation describing which and how other ontologies are reused. 
 </details></details>

<details>
<summary><strong>Requirement 2: Instructions for reuse </strong></summary>


<details><summary><strong>GUIDELINES</strong></summary>

 </details></details>

 #### Principle 7: Modularity
> 

**Sources**:

###  REQUIREMENTS

<details>
<summary><strong>Requirement 1: Reuse specification </strong></summary>

Whenever applicable, a search should be conducted for well-known ontologies to identify any existing elements that may be useful to reuse. 

>[!note] While it is always advisable to reuse standard well-known ontologies, vocabularies, and/or terminologies, the priority must be to select those that best align with the established requirements of your ontology and meet a minimum quality standard.

<details><summary><strong>GUIDELINES</strong></summary>
It is recommended to add in an external document a brief explanation describing which and how other ontologies are reused. 
 </details></details>

<details>
<summary><strong>Requirement 2: Instructions for reuse </strong></summary>


<details><summary><strong>GUIDELINES</strong></summary>

 </details></details>

#### Principle 8: Format
> The ontology is available in at least one standard knowledge representation language. 

**Sources**:

###  REQUIREMENTS

<details>
<summary><strong>Requirement 1: Ontology representation language </strong></summary>

The ontology MUST be encoded and available in one or multiple representation common formal languages.

<details><summary><strong>GUIDELINES</strong></summary>
In order to decide which representation language you are going to use, it is important to establish what your requirements are regarding the level of expressiveness of the language needed, and the use that you will give to the ontology.  The most common knowledge representation language used for ontologies are:

1) OWL¿2?
2) RDF(S)
3) Common logic
4) SKOS?

>[!note] For ontologies of belonging to the biomedical domain, it is also common to use the OBO format. This is not a formal ontology language but a common format developed by the OBO Foundry to represent in a more human-readable manner although with less expressivity than OWL. 

OWL and RDF(S) can be serialized in multiple well-know syntaxis such as:
- Turtle
- N-triples
- RDF/XML
- JSON-LD

 There is a wide range of tools that allows you to encode and export the ontology in those formats:
- Protégé
- Chowlk
- Ontology Development Kit
- VocBench
- Fluent Editor
 </details></details>





