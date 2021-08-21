<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Layer of Protection Analysis API (<strong>LOPA API</strong>)</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---


<p align="center">
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Tech](#tech)
- [Installation](#installation)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)


## 🧐 About <a name = "about"></a>

LOPA API for Layer of Protection Analysis API is the Bowtie Diagram API for LOPA.

LOPA is a Graphical User Interface (GUI) used to evaluate high-consequence scenarios determining if the combination of probability of occurrence and severity of consequences meets a company’s risk tolerance. 

## Tech <a name = "tech"></a>

LOPA API is written in [Python 3](https://www.python.org) and [Django Rest Framework](http://www.django-rest-framework.org/)
  
## Installation  <a name = "installation"></a>
  
#### Windows 10 Users

Please install and set up the following packages first. Ugrade if you find the package already installed:  
* Download [Python 3](https://www.python.org/downloads/). It is advisable to install the package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.  
  ```sh
  python -V
  ```  
* Download [pip](https://pip.pypa.io/en/latest/installing) and follow the instructions in the link as an installation guide.  

* It is advisable to use LOPA API in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this virtual environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:
  ```sh 
  py -m pip install virtualenvwrapper-win 
  ```
  
* Create a new virtual environment:
  ```sh
  mkvirtualenv <envname>
  ```
* Change your directory to the directory of the virtual environment

* Activate the virtual environment with:
  ```sh
  <envname>\Scripts\activate
  ```
* Install requirements in the virtual environment created:

  ```sh
  pip install -r requirements.txt
  ```
* Run server to ensure everything is running properly.
  ```sh
  python runserver manage.py
  ```
* Deactivate the virtual environment with:
  ```sh
  deactivate
  ```


## Usage
* Start the application `$ python manage.py runserver`
* Use `Postman` to consume available endpoints
* A user can:
  * Get all Events
  * Get a single Event
  * Get a single Cause
  * Get a single Cause Barrier
  * Get a single Consequence
  * Get a single Consequence Barrier

## Endpoints
| Request type      | Endpoint          | Action |
| ------------- |:-------------:| -----:|
| GET         | / / | Get all Events|
| GET         | /event/:id  | Get an Event |
| GET         | /cause/:id  | Get a Cause |
| GET         | /cause_barrier/:id  | Get a Cause Barrier |
| GET          | /consequence/:id      | Get a Consequence
| GET        | /consequence_barrier/:id  | Get a Consequence Barrier |



## ⛏️ Built Using <a name = "built_using"></a>

- [Django Rest Framework](http://www.django-rest-framework.org/) - API
- [MySQL](https://www.mysql.com/) - Database


## ✍️ Authors <a name = "authors"></a>

- [@seun-beta](https://github.com/seun-beta) - Software Development



## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
