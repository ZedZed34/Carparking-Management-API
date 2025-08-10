# Carpak Information Management with RESTful API developing with DJANGO Framework.

Application with Django framework using REST API to implement managing carparking information by address and types of carpark. API endpoints satisified for managing data related to existing carpark datasets.

## **Features of the App**

- **View All Carparks**: List all carparks.
- **Filter by Car Park Type**: Filters car parks by type.
- **Filter Free Parking**: Shows car parks with free parking.
- **Group by Parking Systme**: Display groups of car parks by parking system.
- **Average Gantry Height**: Calculates and shows average gantry heights
- **Add New Car Park**: Create a new car park data entry via a web form.
- **Search Car Parks by Address**: Do searching all car parks by address.

---

## **Requirements**

1. Python 3.8 or later
2. pip packages
3. Virtual environment tool (recommended for setup)

---

## **Setup Instructions**

### **1. Extract and open the zip archive**

```bash
cd <project-folder>
```

### **2. Install Django Framework**

```bash
pip install django
python -m django --version
```

### **2. Create a Virtual Environment**

```bash
python -m venv HLA
HLA\scripts\activate
```

### **3. Install Required Packages**

```bash
pip install -r requirements.txt
```

### **4. Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Data Setup**

```bash
python scripts/load_and_store.py
```

### **6. Run the Application**

```bash
python manage.py runserver
```

### **7. Access the Application**

Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

---


## **Testing**

To run the tests, execute the following command:

```bash
python manage.py test
```

---

