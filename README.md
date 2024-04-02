# sp24-lab10
Materials for week 10 lab in CS-370.

_April 2, 2024_

Organization:
* mvc-timer: The MVC example application developed by Prof Davis

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Rhys Sorenson-Graff
* NAVIGATOR: Luke Samuels

You will switch halfway through this activity.

## Part 1 Documentation

_Write your answers to the questions below._

* What were the main ideas from the pre-lab reading?

The MVC model is used for software where all the processing happens in the same place,
such as a desktop app. It works by having a frontend/GUI make requests to a controller,
which then makes request to a database or internal storage. The advantages of this system
is that the model, view and controller modules are very decoupled (if implemented well).

* What questions did you have about this material? What did you find confusing?

We were pretty confused by the idea of dependency of inversion and what problem it is supposed to solve.
To us, the name suggests that the control of internal elements inside a module should be "inverted" or
controlled by other modules. However, we understood the description to dependency of inversion to be that
internal elements should be abstracted and that there should be a high-level interface that other modules
interact with.

### Exercise 0: Run the tests and the application
View the README file in the mvc-timer directory. Run the tests and the application.

_If you have any trouble running the application or tests, please note it here._

### Exercise 1: Read the code
Read the code to understand what happens when you run the text timer application, starting from timer.py. 

Then read the code to understand what happens when you run the GUI application, set the time, and start the timer.

What questions do you have? _Write them here. If you need to know, ask Prof Davis since she wrote the code!_

1. We were pretty confused about the @ operator and what it does. Thanks for explaining it to us!


### Exercise 2: Patterns and principles
_Answer the following questions to the best of your ability._
* Which concrete classes implement the Observer and Subject roles?
* How do the model, controller, and view classes gain references to each other? What style of dependency injection does the application use: constructor, method, or property injection?

The concrete subject is the threadTimerModel, in model_thread.py. The concrete observer is teh TimerController in controller.py.

The Controller class inherits the observer class, the ThreadTimerModel inherits the observer class. Both the view_gui and view_text classes inherit the viewTimer class. They use property injection to assure that they all have common interfaces that can call each other.


### Exercise 3: Extending the code
Extend the text or GUI application to play a sound when the timer is done.

As time permits, try other exercises from the README in the `mvc-timer` directory.

_Record here: What extensions did you implement or attempt to implement?_
