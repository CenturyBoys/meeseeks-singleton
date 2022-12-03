# A Singleton python project 
![Alt text](https://ih1.redbubble.net/image.1140492877.4744/mp,504x516,gloss,f8f8f8,t-pad,600x600,f8f8f8.jpg "Title")

```python
import meeseeks

meeseeks.OnlyOne.set_global_options(
    by_args_hash=True
)

@meeseeks.OnlyOne
class A:
    def __int__(self, a):
        pass

a1a = A(10)
a2a = A(20)
a1b = A(10)
a2b = A(20)

assert a1a == a1b
assert a2a == a2b
assert a2a != a1b
```