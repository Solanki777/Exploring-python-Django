

### 1. Create virtual environment

```bash
python -m venv todo_env
```

---

### 2. Activate virtual environment

#### 👉 Windows:

```bash
todo_env\Scripts\activate
```

#### 👉 Mac/Linux:

```bash
source todo_env/bin/activate
```

## 🔹 Activate Virtual Environment

### 👉 Windows (PowerShell)

If you get an error like:

```
execution of scripts is disabled on this system
```

Run this command **once**:

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the virtual environment:

```bash
todo_env\Scripts\activate
```

---

### 👉 Windows (Command Prompt)

```bash
todo_env\Scripts\activate
```

---

### 👉 Mac/Linux

```bash
source todo_env/bin/activate
```


---

### 4 Install dependencies

```bash
pip install django
```

---

## check what the dependencies are installed

``` bash
pip freeze
```

### 5 Create a Django project called todomanager

``` bash
django-admin startproject TodoManager
```

### 6 create an apps inside the project

``` bash
python manage.py startapp home
```

### 6 Now go back to main folder and start the server

```bash
python manage.py runserver
```

to run on specific port tryout 

```bash
python manage.py runserver 5000
```

7. when you create new app first it must defined inside the installed_apps in settings.py in main files then create new app

