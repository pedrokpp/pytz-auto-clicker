# pytz - A simple Python Auto Clicker
Pretty easy to use and functional with some randomization between clicks.

## Requirements
``pip install -r requirements.txt``

## Bypass guide
If you are using this somewhere that is prohibited and they ask you to see your screen here's what you should do:
- Put in a folder not so suspicious;
- Edit its content to something like:

```python
import os

def main():
  if not os.name == "nt":
    print("this program only works with windows")
    exit()
  else:
    pass
  print(f"Your OS is Windows '{os.name}'")
  x = input("rate this program 1 to 10: ")
  print(f"{x} is a reasonable score")
   
if __name__ == "__main__":
  main()
  ```
  
  - You're good to go
