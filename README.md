#  Employee Management System (CLI)

An efficient, command-line-based **Employee Management System** developed in Python. This project demonstrates core software development principles, utilizing Python's built-in `csv` and `os` modules to manage, persist, and manipulate organizational records dynamically without relying on external databases.

##  Key Features & Capabilities
- **Complete CRUD Functionality:** Seamlessly Add, View, Update, and Delete employee records.
- **Advanced Search & Filtering:** Filter and display employee records by department instantly.
- **Batch Processing Support:** Handle multiple employee IDs or departments simultaneously using comma-separated inputs (e.g., deleting or viewing multiple records at once).
- **Data Persistence:** Automatically synchronizes and saves all changes directly to a CSV file (`employees_project.csv`).
- **Robust Exception Handling:** Gracefully handles invalid inputs and file errors to prevent runtime crashes.

##  Technical Highlights
- **Data Structures:** Utilizes Python lists of dictionaries for efficient in-memory data manipulation.
- **File I/O Operations:** Implements `csv.DictReader` and `csv.DictWriter` for clean structured data mapping.
- **Modular Programming:** Built using clean, reusable Python functions and a centralized `main()` control loop.