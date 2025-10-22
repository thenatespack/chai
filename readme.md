# Project: Chai (Chat + AI)

This repository contains the source code for the "Chai" command-line AI chat application, developed as part of the DBT230 course.

## Author

**Name:** Nathan Spackman

## Lab 2: MongoDB & Flat-File Persistence


# Chat Application Storage Analysis

## Question 1: Performance Analysis (5 points)

Run `performance_test.py` and record the results.

**a.** How did **append times** change as the number of messages increased, comparing FlatFileManager and MongoDBManager? 

They stay fairly consistent as the number of messages increase where flat-file storage increases as message count increase.

**b.** What differences did you observe in **read times** when retrieving the full conversation between the two storage methods?  

Flat file increases as file grows while Mongo stays relatively similar as size grows.

**c.** Based on your observations, explain the reasons behind these performance differences.

Flat file has to read and serialize every time a change is made VS Mongo only has to edit the document and has to search for it

---

## Question 2: Atomic Operations (5 points)

In the `append_message()` method of `MongoDBManager`, the `$push` operator is used.

**a.** Research and explain what **"atomic operations"** mean in the context of databases.  

    Atomic Operations mean that either all of request happens or nothing.

**b.** Why are atomic operations important in a **chat application**, especially when multiple messages may be appended at the same time?

    Atomic Operations mean that different users can write without losing data when two different queries are done at the same time.

---

## Question 3: Scalability (5 points)

Imagine your chat application now has **1 million users**, each with an average of **10 conversation threads** and **500 messages per thread**.

Compare how **FlatFileManager** and **MongoDBManager** would handle the following tasks:

**a.** Finding all conversation threads for a specific user  

    FlatFile - Search For User folder and then Parse File
    MongoDB  - use find({user_id:User_ID})

**b.** Loading a specific conversation  

    FlatFile -  Read Entire file To find thread then return conversation 
    MongodB  - Use Index to find thread quickly

**c.** Organizing storage and dealing with file system limitations

    FlatFile - limited by disk speed and os/dir limits
    MongoDB  - indexing,sharding,splitting to collections.
---

## Question 4: Data Modeling Design Challenge (5 points)

1.One advantage of the embedded messages design (what we currently use)

    It saves time when gathering results because you don't have to join.

2.One advantage of the separate message documents design

    It would save space and scale better.

3.A scenario where you would choose the separate messages design instead

    Embedded - When you have few users and small conversations
    Separate - When you have a lot of users OR very long complex messages


