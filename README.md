# sp24-lab10

Materials for week 10 lab in CS-370.

_April 2, 2024_

Organization:

- mvc-timer: The MVC example application developed by Prof Davis

## Team Members for Part 1

Fabian Clara

## Team Roles for Part 1

Who will start out as

- DRIVER: Fabian
- NAVIGATOR: Clara

You will switch halfway through this activity.

## Part 1 Documentation

_Write your answers to the questions below._

- What were the main ideas from the pre-lab reading?
  MVC design pattern (Model View Controller). The Model part consists of data and business logic, View displays the data, while the Controller moves the data from the Model to the View.
  Dependency Inversion Principle. Modules should depend on abstractions and not on each other. Abstractions should not depend on details. In version control can help us implement the dependecy.
- What questions did you have about this material? What did you find confusing?
  How can we efficiently find out what is an abstraction and what is a concrete implementaion?

### Exercise 0: Run the tests and the application

View the README file in the mvc-timer directory. Run the tests and the application.

_If you have any trouble running the application or tests, please note it here._

### Exercise 1: Read the code

Read the code to understand what happens when you run the text timer application, starting from timer.py.

Then read the code to understand what happens when you run the GUI application, set the time, and start the timer.

What questions do you have? _Write them here. If you need to know, ask Prof Davis since she wrote the code!_

In the text version, is there a way to stop the timer?

### Exercise 2: Patterns and principles

_Answer the following questions to the best of your ability._

- Which concrete classes implement the Observer and Observable roles?
  Controller: Observer
  ThreadTimerModel: Observable
- How do the model, controller, and view classes gain references to each other?
  When ThreadTimerModel makes a change, it uses the notify method to update all of its observers about the change.
- What style of dependency injection does the application use: constructor, method, or property injection?
  Property injection?

### Exercise 3: Extending the code

Extend the text or GUI application to play a sound when the timer is done.

As time permits, try other exercises from the README in the `mvc-timer` directory.

_Record here: What extensions did you implement or attempt to implement?_

We implemented the extensions 1-6 that were indicated on the README. They were all successful!
