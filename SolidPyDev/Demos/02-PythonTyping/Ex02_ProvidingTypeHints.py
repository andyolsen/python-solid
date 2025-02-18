# Python typings, you can sanity-check correct usage.
y: int = 42
y = 43          # OK
y = "Hello"     # Not OK

# To check types:
#   pip install pyright
#   pyright <filename.py>