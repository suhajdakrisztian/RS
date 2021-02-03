from subprocess import call
from os import path

NYSE_SYMBOLS = open(path.join(path.dirname(path.abspath(__file__)),
                    ".nyse.txt")).read().split('\n')
NASDAQ_SYMBOLS = open(path.join(path.dirname(path.abspath(__file__)),
                      ".nasdaq.txt")).read().split('\n')

SYMBOL_LIST = NASDAQ_SYMBOLS + NYSE_SYMBOLS

class ShellExecutor():

  def check_last_update(self):
    call(path.join(path.dirname(path.abspath(__file__)), "check_last_update.sh"))

def main():
  shell_caller = ShellExecutor()
  shell_caller.check_last_update()

main()