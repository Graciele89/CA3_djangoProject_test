# CA3 Django Project Testing & Security

### Student: Graciele Maria Ludwig
### Student ID: 22711
### Back-end Web Development - BSC30922
### CA1 - Individual Project - 25% weighting

To complete this assessment, we need to build a web application using Django.
This application should have the capability to conduct CRUD (Create, Read, Update, Delete) 
operations and generate positive (acceptable data) and negative (unacceptable data) tests.
Additionally, it is required to document the function testing and integrate a minimum of 
two anti-hacking security measures.

I created an exercise planner where the user can select a type of exercise and a workout plan,
day of the week and time he wants to do it, using the django forms to create it.
Django forms provide several advantages for developers building web applications.
They primarily offer a straightforward and standardized means of handling user input 
and validating data. With Django forms, developers can simply design forms that validate
user input and handle errors, saving them the time and effort of implementing bespoke 
validation code. Moreover, Django forms offer a layer of abstraction that enables programmers
to divide the functionality of a form's presentation from that form's presentation, making it simpler 
to change a form's appearance without changing its underlying logic. Finally, Django forms may be easily
adjusted to address specific use cases and can be connected with other Django components such as models and views.
When a form is submitted, Django automatically validates the data and provides error messages if necessary.
If the information is accurate, it can be added to the database or used for other tasks like emailing the user
or directing them to another page. Overall, Django forms provide a powerful and flexible way to handle user input
and are an essential component of any Django-based web application.

As part of the assessment, it was necessary to write positive and negative tests to ensure the proper functionality of our code. 
Positive tests are designed to confirm that the expected behavior is functioning as intended, while negative tests aim to verify 
the program's ability to handle unexpected behavior. To construct positive tests, developers can leverage the Django testing 
framework to generate test cases and ascertain that their applications are operating as anticipated. Conversely,
when creating negative tests, it is feasible to purposely introduce errors or invalid inputs to assess the program's ability 
to handle them appropriately. Through a combination of positive and negative testing, developers can establish the effectiveness
and reliability of their codebase.

In this project, beyond the user authentication, I added other two security steps as set the "debug = false" on the settings.py, so only allowing the specific hosts 
preventing unauthorized access, as well as "{% csrf_token %}" that helps prevent Cross-Site request Forgery attacks because this tag 
generates a unique token for each form submission which is validated on the server side making sure that the request is coming from a trust source.



## References
### images: https://unsplash.com/s/photos/exercising
### Django docs: https://docs.djangoproject.com/en/4.1/intro/tutorial01/ , https://docs.djangoproject.com/en/3.2/topics/forms/