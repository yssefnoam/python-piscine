import sys

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

NESTED_MORSE = {
   "A": "._",
   "N": "_.",
   "B": "_...",
   "O": "___",
   "C": "_._.",
   "P": ".__.",
   "D": "_..",
   "Q": "__._",
   "E": ".",
   "R": "._.",
   "F": ".._.",
   "S": "...",
   "G": "__.",
   "T": "_",
   "H": "....",
   "U": ".._",
   "I": "..",
   "V": "..._",
   "J": ".___",
   "W": ".__",
   "K": "_._",
   "X": "_.._",
   "L": "._..",
   "Y": "_.__",
   "M": "__",
   "Z": "__..",
   "1": ".____",
   "6": "_....",
   "2": "..___",
   "7": "__...",
   "3": "...__",
   "8": "___..",
   "4": "...._",
   "9": "____.",
   "5": ".....",
   "0": "_____",
   " ": "/"
}


def error():
   """func: error()"""

   print("AssertionError: the arguments are bad")


def main():
   """func: main()"""

   args = sys.argv[1:]
   if args[1:] != []:
      error()
      return 0
   result = ""
   err = False
   for c in args[0]:
      if c in LETTERS:
         result += NESTED_MORSE[c.upper()]
      else:
         err = True
         break
   if err:
      error()
   else:
      print(result)

if __name__ == "__main__":
   main()
