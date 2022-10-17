![HBS](https://user-images.githubusercontent.com/98336206/177213884-58390904-70c0-42b2-9e90-fdc51163761f.png)

# Holberton School - AirBnb clone

### Project description

AirBnB clone project as part of a Holberton School project.
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
All the features are not implemented but you will find the most important

The following elements compose the AirBnb clone and can be found in the repository files :

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)



![first step](https://postimg.cc/56qYKq0J)

### Requirements 

Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04 LTS using python3 and PEP8 style corrector.

### Installation
Clone the repository:
```
$ git clone https://github.com/MoustaphaElPsyCongroo/holbertonschool-AirBnB_clone.git
```
Launch the console application in interactive mode:
```
$ ./console.py;
```

### Console application

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

Here is the list of commands available in the console, followed by examples to guide you in its handling :

| Command | Description |
| --- | --- |
| `all` |  	Prints all string representation of all instances based or not on the class name 
| `create` | Creates a new instance of the <class_name>. Creates a Json file with the object representation. and prints the id of created object.
| `destroy` | Deletes and instance base on the class name and id.
| `EOF` | Exit the program
| `help` | Provides description of commands
| `quit` | Exit the program
| `show` | Prints the string representation of an instance based on the class name and id.
| `update` | Updates an instance based on the class name and id by adding or updating attribute

### Examples


### Tests
All tests are located in tests/ and can be execute all by running this command:
`$ python3 -m unittest discover tests`





