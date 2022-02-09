# Python gym booking App
### First project in Python

### Includes (but not limited to):
##### Members screen
![Screenshot 2022-02-09 171432](https://user-images.githubusercontent.com/86377797/153254125-b78798e6-219c-418f-97cb-7b0ec3e73dd8.png)

##### Book classes through member
![Screenshot 2022-02-09 171524](https://user-images.githubusercontent.com/86377797/153254242-6b1096bf-b024-4db8-9ba9-ba3c4434df45.png)

# Run commands
## SQL commands while in GYM_APP directory:

- createdb gym

- psql -d gym -f db/gym_manager.sql

- psql -d gym

## Python commands (if desired):

- python3 console.py ## To run seeded data as example of members and classes ##

## Other commands:

- flask run to enable program to run at 'http://localhost:5000/'


## Brief:

### Gym
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

### MVP
The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class
Inspired By
Glofox, Pike13

### Possible Extensions
Classes could have a maximum capacity, and users can only be added while there is space remaining.
The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.


### Technologies used:

Pyhton3, Flask, Jinja, CSS3, HTML5, PostgresQL
