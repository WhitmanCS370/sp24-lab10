# sp24-lab10
Materials for week 10 lab in CS-370.

_April 2, 2024_

Organization:
* mvc-timer: The MVC example application developed by Prof Davis

## Team Roles for Part 1
Who will start out as
* DRIVER: _Driver's name_
* NAVIGATOR: _Navigator's name_

You will switch halfway through this activity.

## Part 1 Documentation

_Write your answers to the questions below._

* What were the main ideas from the pre-lab reading?

Dependency inversion: higher level modules should depend on abstractions of the lower level functions
Dependency injection: Realization of dependency inversion through various methods
Model-View-Controller - A design pattern where an application is seperated into model - data and bussiness logic,

view - the interface shown to users,

controller - managing connection between model and view
### Exercise 0: Run the tests and the application
View the README file in the mvc-timer directory. Run the tests and the application.

_If you have any trouble running the application or tests, please note it here._

### Exercise 1: Read the code
Read the code to understand what happens when you run the text timer application, starting from timer.py. 

Then read the code to understand what happens when you run the GUI application, set the time, and start the timer.

What questions do you have? _Write them here. If you need to know, ask Prof Davis since she wrote the code!_

### Exercise 2: Patterns and principles
_Answer the following questions to the best of your ability._
* Which concrete classes implement the Observer and Subject roles?
* How do the model, controller, and view classes gain references to each other? What style of dependency injection does the application use: constructor, method, or property injection?

### Exercise 3: Extending the code
Extend the text or GUI application to play a sound when the timer is done.

As time permits, try other exercises from the README in the `mvc-timer` directory.

_Record here: What extensions did you implement or attempt to implement?_
