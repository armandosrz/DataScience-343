# Genetic Algorithm Password Cracker

A specific web page was setup in such a way that when submitting a specific
username and an alphanumeric string as a password it will return a time as a
float. This float represents how close you are to guessing the password,
so the longer the submit time is, the closer you are to guess it.

By using a genetic algorithm a new character is randomly generated until the
password is reached based on the feedback approximation.

## Usage

Version: `Python 2.7`

`python main.py`

## Content

- [password.txt](password.txt): The final cracked password for my profile.
