# sp24-lab10
Materials for week 10 lab in CS-370.

_April 2, 2024_

Organization:
* mvc-timer: The MVC example application developed by Prof Davis

## Team Members for Part 1
Enter your names here
Zurain Zeeshan
Molly Halverson

## Team Roles for Part 1
Who will start out as
* DRIVER: Zurain Zeeshan
* NAVIGATOR: Molly Halverson

You will switch halfway through this activity.

## Part 1 Documentation

_Write your answers to the questions below._

* What were the main ideas from the pre-lab reading?
We learned about the model, view, controller design pattern. The model represents the data and the business logic of the application. The view is what the user sees and displays data from the model to the user. The controller is the intermediary between the model and the view. The second reading talked about the dependency inversion principle as well as the inversion of control and dependency injection.

* What questions did you have about this material? What did you find confusing?
What is meant by abstractions in inversion of control ("higher level modules to depend on abstractions")?

### Exercise 0: Run the tests and the application
View the README file in the mvc-timer directory. Run the tests and the application.

_If you have any trouble running the application or tests, please note it here._

### Exercise 1: Read the code
Read the code to understand what happens when you run the text timer application, starting from timer.py. 

Then read the code to understand what happens when you run the GUI application, set the time, and start the timer.

What questions do you have? _Write them here. If you need to know, ask Prof Davis since she wrote the code!_
We were curious as to why there is an increment and decrement feature in the timer, but when we click on it, it decrements/increments for a second and then jumps back to the original second it was on. 

### Exercise 2: Patterns and principles
_Answer the following questions to the best of your ability._
* Which concrete classes implement the Observer and Subject roles?
Classes concreteObserverA and concreteObserverB and concreteSubject

* How do the model, controller, and view classes gain references to each other? What style of dependency injection does the application use: constructor, method, or property injection?
The model, controller and view reference each other using constructor injection.

### Exercise 3: Extending the code
Extend the text or GUI application to play a sound when the timer is done.

As time permits, try other exercises from the README in the `mvc-timer` directory.

_Record here: What extensions did you implement or attempt to implement?_
