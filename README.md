# SQLAlchemy Data Modeling: ARRAY vs. Separate Tables vs. Dictionary

## Overview
This repository explores three different approaches for managing relational data using SQLAlchemy:

- ARRAY Data Type
- Separate Tables
- Dictionaries
  
Each approach is examined with practical examples using a Company and Members model to illustrate how they handle relational data. The blog post provides a detailed comparison of the pros and cons of each method.

## Project Structure
```bash
/project-root
│
│── set_up_db.sql
│── team_JSON.py
│── team_array.py
│── team_seperate_table.py
└── README.md
```

## Brief Description
-  Data Type: array_example.py demonstrates how to use SQLAlchemy's ARRAY data type for storing lists of members directly in a single table.
-  Separate Tables: separate_tables_example.py shows how to implement a normalized schema with separate tables for companies and their members.
-  Dictionaries: dictionary_example.py illustrates how to use a JSON-like column to store complex member data.

## Pros and Cons
### Using ARRAY Data Type
- Pros: Simpler schema; easier management for small datasets.
- Cons: Harder to enforce constraints; inefficient with large arrays.

### Using Separate Tables
- Pros: More normalized; easier to enforce constraints; flexible for complex queries.
- Cons: More complex schema; slightly more complex queries.

### Using Dictionary
- Pros: Flexible for detailed attributes; easier updates without schema changes.
- Cons: Complex with nested structures; harder to enforce constraints.

## Blog Post
For a detailed analysis and examples, check out the blog post:[ARRAY vs. Separate Tables vs. Dictionary for SQLAlchemy Data Modeling](https://medium.com/@wisdomokposin/array-vs-separate-tables-vs-dictionary-in-sqlalchemy-24e62b05b85e).
