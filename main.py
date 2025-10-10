import datetime
from threading import Thread
import time
import os
from db_wrappers.flat_file_manager import FlatFileManager

def main():
    """
    Main function to run the Chai AI chat application.
    Handles the REPL (Read-Eval-Print Loop) for user interaction.
    """
    print("Welcome to Chai!")
    user_id = input("Please enter your user ID to begin: ")

    # --- TODO 1: Instantiate the Database Wrapper ---
    # Create an instance of the FlatFileManager, passing the user_id to it.
    # This object will handle all our file reading and writing.
    # Specify the storage directory as "data"
    db_manager = FlatFileManager("data")

    # --- TODO 6 (do this last): Create a way for a user_id to have multiple conversation threads
    # Requirements:
    #   - If user already exists, then have the user select which thread (conversation_id) they want to use
    #       - Give the option to use a new thread
    #   - Proceed to run_chat() with the correct conversation_id
    #   Hint: This is not a "clean" addition, you may need to restructure how data is stored and indexed
    #         There are many ways to do this. Devise a plan and implement your own solution.
    db_manager.save_index()
    threads= db_manager.get_threads(user_id)
    conversation_id = f"{user_id}_conversation"

    if(len(threads)>0):
        index=0
        for thread in threads:
            print(f"{index}: {thread}")
        while True:
            print("Select Option: ")
            id=int(input(">"))
            if(id>-1 and id< len(threads) ):
                conversation_id = threads[id]
                print(conversation_id)
                break

    run_chat(db_manager, conversation_id,user_id)

def run_chat(db_manager: FlatFileManager, conversation_id: str,user_id:str) -> None:
    # --- TODO 2: Check if conversation already exists, printout conversation if so ---
    #   - Add a timer that times how long it took to use get_conversation and print the results after
    start_time = time.perf_counter()
    messages = db_manager.get_conversation(conversation_id)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(duration)
    if messages:
        for message in messages:
            print(message)
        print(f"Load time: {duration:.4f} seconds")

    print(f"Conversation: '{conversation_id}'. Type 'exit' to quit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # --- TODO 3: Start the performance timer ---
        # Record the start time before performing the database operations.
        # Use time.perf_counter() for high precision.
        start_time = time.perf_counter()

        # --- TODO 4: Implement the Read-Append-Write Cycle ---
        # 1. Get the entire conversation history from the file.
        if not messages:
            messages =db_manager.get_conversation(conversation_id)

        # 2. Append the new user message to the list of messages using messages.append()
        #    Each message should be a dictionary, e.g., {"role": "user", "content": user_input}
        messages.append({"role": "user", "content": user_input})

        # 3. Create a mock AI response and append it to the list.
        #    The AI response should also be a dictionary using format: {"role": "assistant", "content": ai_response}
        ai_response = "This is a mock response from the AI."
        messages.append({"role": "assistant", "content": ai_response}) 

        # 4. Save the *entire*, updated list of messages back to the file.
        #    Call your db_manager's save method.
        relative_filepath = f"{conversation_id}.json"
        # fixme! use db manager save method here
        db_manager.save_conversation(conversation_id,relative_filepath,messages,user_id)
        # ----------------------------------------------------

        # --- TODO 5: Stop the timer and calculate duration ---
        # Record the end time and calculate the difference to see how long the
        # entire read-append-write cycle took.
        end_time = time.perf_counter() # fixme!
        duration = end_time- start_time # fixme!
        # ---------------------------------------------------

        print(f"AI: {ai_response}")
        print(f"(Operation took {duration:.4f} seconds)")
        db_manager.save_index()



if __name__ == "__main__":
    main()