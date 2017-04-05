#!/usr/bin/env python

class LustObject(object):
  # executes the command
  def handle(self, arguments): pass
  def print_help(self): pass

class SquareCommand(LustObject):
  def handle(self, arguments):
    try: argument = int(arguments[0])
    except (ValueError, IndexError):
      print("square: could not read integer argument.")
      return

    print(self.__square(argument))

  def print_help(self):
    print(" square <integer>")
    print("   Calculates the square of <integer>.")

  def __square(self, argument):
    return argument**2

class QuitCommand(LustObject):
  def handle(self, arguments = None):
    print("Bye!")
    exit()
  def print_help(self):
    print(" quit")
    print("   Quits.")

class HelpCommand(LustObject):
  def __init__(self, commands):
    self.commands = commands
  def handle(self, arguments = None):
    print("List of all commands")
    print("--------------------")
    for command in sorted(self.commands):
      self.commands[command].print_help()
  def print_help(self):
    print(" help")
    print("   Prints help for all commands.")


print("Hello! Welcome to the LARICS Universal Shell Terminal (LUST)!")
print("Enter 'help' for a list of commands. Press Ctrl-D or enter 'quit' to quit.")

# dictionary for storing all commands
commands = { }

commands["square"] = SquareCommand()
commands["quit"] = QuitCommand()
# help command needs a reference to the parent dictionary in order to call each
# command's print_help() function
commands["help"] = HelpCommand(commands)

while True:
  # read current line and try to extract command name
  try:
    cmd_line = raw_input(">> ")
  except (EOFError):
    break
  arguments = cmd_line.split()
  try: cmd_name = arguments[0].lower()
  except IndexError: continue

  # look up the appropriate command in commands dictionary
  if cmd_name not in commands:
    print("lust: no such command '{}'.".format(cmd_name))
    continue
  else:
    # command found, pass its handler the rest of the read arguments
    commands[cmd_name].handle(arguments[1:])

print
commands["quit"].handle()
