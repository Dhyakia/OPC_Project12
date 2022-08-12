# OPC_Project12
Développez une architecture back-end sécurisée en utilisant Django ORM

# Welcome

The of this project was to create an secure API from the entity-relation diagram to the use of filter.

# Requirements

* Python3 at https://www.python.org/downloads
* ... and that's it !

# Installation

## Step 1: Acquire the codebase

### Using Git Desktop
With the desktop app, simply click on the "Code" (green button) at the top of this page and then "Open with GitHub Desktop".

Clone the file to desired location and you're done !

### Using Git Console
Navigate to desired location and use:
```
git clone https://github.com/Dhyakia/OPC_Project10.git
```

### Using the manual download
Click on the "Code" (green button) at the top of this page and then "Download Zip"

Un-zip the file into the desired location and you're done !

## Step 2: Setting up a virtual environement

For a better user experience, it is recommanded to use a virtual environnement.

1. With the console, navigate to the folder of installation.

2. Next, to create the environnement, enter this command:
    
    Windows: ```python -m venv venv ```

    MacOs/Linux: ```python -m venv venv ```

3. Now, all that's left if to activate it:

    Windows: ```venv/scripts/activate```

    MacOs/Linux: ```venv/bin/activate```

If everything is done correctly, you should now see the "venv" tag at the start of the line of the console.

## 3. Install the dependencies

Using the console, navigate to the project folder and enter:
```
pip install -r requirements.txt
```

## 4. First launch: setting up the database

Using the console, navigate inside the LITReview folder, where the manage.py file is and enter:
```
python manage.py migrate
```

Congratulation, you're now all setup for using the application !

# Usage

## Starting the server
Activate the virtual environnement.


Using the console, navigate inside the LITReview folder, and enter:

```
python manage.py runserver
```

# Authorization

Here, i set up a table showing what actions are possible and what user can access it.

The current program has 3 type of users : ADMIN(Gestion) / SELLER / SUPPORT

## Admin (gestion/manager)

| Object | List | Create | Retrieve | Update | Destroy |
| --- | --- | --- | --- | --- | --- |
| User | Yes | Yes | Yes | Yes | Yes |
| Client | Yes | Yes | Yes | Yes | Yes |
| Contract | Yes | Yes | Yes | Yes | Yes |
| Event | Yes | Yes | Yes | Yes | Yes |

## Seller

| Object | List | Create | Retrieve | Update | Destroy |
| --- | --- | --- | --- | --- | --- |
| User | No | No | No | No | No |
| Client | Yes | Yes | Limited | Limited | No |
| Contract | Yes | Yes | Limited | Limited | No |
| Event | Yes | Yes | No | No | No |

## Support

| Object | List | Create | Retrieve | Update | Destroy |
| --- | --- | --- | --- | --- | --- |
| User | No | No | No | No | No |
| Client | Yes | No | No | No | No |
| Contract | No | No | No | No | No |
| Event | Yes | No | Limited | Limited | No |

# Futur viewing

This is the twelfth out of thirteen python project with OpenClassRoom