# Project: Chai (Chat + AI)

This repository contains the source code for the "Chai" command-line AI chat application, developed as part of the DBT230 course.

## Author

**Name:** Nathan Spackman

## Lab 1: Flat-File Persistence

This lab focuses on building the foundational persistence layer using a simple flat-file (JSON) system. The goal is to establish a performance baseline for file I/O operations, which will serve as a benchmark for subsequent labs involving more advanced database technologies.


1. What are two different designs you contemplated for your multiple conversations implementation?
     
    I thought about embedding the user id into the conversation id so I can just regex the conversation ids. The solution i picked was just storing the id as a member in the json file.

2. A vibe coder wants to make a quick MVP (minimum viable product) over the weekend that handles chat threads with AI models. Do you recommend using JSON files for persistence? Why?

    Most likely, If data persistence was a requirement json is very easy and quick way to setup storing and reading data. It would make the crud operations a lot easier and save time over other persistence solutions.

3. You are interviewing at OpenAI. The interviewer asks if you would use raw JSON files to store user chats or if you would use a database or other form of persistence and to explain your choice. How would you reply?

    In like 90% of solutions a database is better because there is a lot better scaling and is a lot easier to manage then just a bunch of files in folder.

4. What did you notice about performance using this file storage method?

    The performance was very fast it will suffer a lot as the file scales and it takes a lot of time to read and write the file. It is somewhat inconsistent in speed.