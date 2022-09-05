#AirBnB Clone

## Description

This project is simply same implementation of **Airbnb** website. Python objects are serialized to JSON strings and JSON strings are deserialized to python objects. for this purpose, we are going to use a file based implementation of storage.
We also have a command line interpreter for modifying a content on the website.

## The Command Interpreter

This is like a shell and used to create instances of a classes we've created for This project. These classes are used to build the objects(instances) of the website features such as city, user, amenty, and the like.

### How To Use It?

we have a python script called console.py that intializes and runs a command interpreter. so inorder to run the application. simply clone this repo and after navigating to your currently working directory, just type './console.py' or 'python3 console.py' and then there you go.

## Supported Command

Here are the supported commands on the command line interpreter.
	- Help [command]: this command is used to get a help with associated command name.
	- quit: quits the command interpreter console and returns to a terminal.
	- EOF: closes the command interpreter.
	- create [class name]: creates an instance of a class passed to it as argument.
	- count [class name]: counts a number of instances of a given class.
	- show [class name] [id]: shows an instance with a specific ID.
	- destroy [class name] [id]: deletes an instance with a specific ID.
	- show [class name] [id]: shows a string representation of a given instance with ID.
	- all [class name]: prints a list containing the string representation of all instance of the class name provided. if no class name is provided then all object's string representation will be printed.
	- update [class name] [id] [attr_name] [attr_value]: updates an attribute of a given object with an attribute value provided.

## Models

The following are the currently supported Models
- BaseModel: represents the base class for all models.
- User: a class representing the User Class and represents a users account on the website.
- State: represents a location where the _user_ lives.
- City: represents the urban center of the _state_.
- Amenity: represents a useful feature of a _place_.
- Place: Represents a relative location of room to be rented.
- Review: Represents a review of a _place_.
