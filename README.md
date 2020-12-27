# File-based key-value data-Store

> This is a file based data store meant to be used as a local storage for one single process on one laptop

### Features / Functional Requirements met

- Supports Create, Read, Delete and Update operations (Entire CRUD)
- Can be initialized using optional file path
- Appropriate error handling for all operations
- There's an optional expiration(an integer) for every key, if provided; the key is no longer valid after the time frame for any read or delete operation.

### Non Functional Requirements met

- Size of file does not exceed 1GB
- A single client process is allowed to access a file at a given time
- The data stored is thread safe and can be accessed using multi-threading.

### Programming Language:

- Python is used, which is an interpreted language and syntactically pretty simple to use and effective in integrating systems more efficiently.
