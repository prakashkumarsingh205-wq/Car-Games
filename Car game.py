while True:
      user_command = input("Enter your command: ")

      if user_command == "help":
        print(""" start - car started...we are ready to go!
stop - car stopped.. 
quit - game terminates.!
""")

      elif user_command == "start":
        print("car started...we are ready to go!")

      elif user_command == "stop":
        print("car stopped..")

      elif user_command == "quit":
          break

      else:
        print("I am not able to read this command")

