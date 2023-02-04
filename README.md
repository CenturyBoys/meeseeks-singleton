# A Singleton python project

![Alt text](https://ih1.redbubble.net/image.1140492877.4744/mp,504x516,gloss,f8f8f8,t-pad,600x600,f8f8f8.jpg "Title")


By CenturyBoys

Did you need help? Call meeseeks from a single box from anywhere

This is meeseeks a single class to do singletons. In the core meeseeks is a class decorator that allows you to have a global singleton scope or a specialized one, some configurations can be used to give more flexibility to your code.


# Scopes

Each class with his decorator has a specialized scope, that is otherwise you create meeseeks object (OnlyOne) and this object will have your configuration and singletons

### Specialized

```python
import meeseeks

@meeseeks.OnlyOne()
class A:
    def __int__(self, a):
        pass

a1a = A(10)
a1b = A(10)
a1c = A(20)

assert a1a == a1b == a1c
```

or

```python
import meeseeks

only_one = meeseeks.OnlyOne()

@only_one
class A:
    def __int__(self, a):
        pass

a1a = A(10)
a1b = A(10)
a1c = A(20)

assert a1a == a1b == a1c
```

On this example we register the class reference in the meeseeks class instance scope

# Configuration

We provide two configuration options:
- `tll: int` (time to live) in seconds. Setting a value greater than 0, the singleton reference will have a time to live in seconds (default 0). Obs: the expired time validation will be made only when you create a new instance of the registered class _ie_ your object will still be in memory
-  `by_args_hash: bool` ( a hash will be made of all args and kwargs ). Setting True, a singleton reference will be created for each arg + kwargs hash (default False). Obs:  The kwargs`s order doesn't have influence
        

### TTL 

```python
import meeseeks
import time

@meeseeks.OnlyOne(ttl=1)
class A:
    def __int__(self, *args, **kwargs):
        pass

a1a = A(1, var_a="a")
a1b = A(1, var_a="a")

time.sleep(1)

a1c = A(1, var_a="a")

assert a1a == a1b
assert a1b != a1c
```

In this example, we set the `ttl` to `1` second and validate if the first two calls result in the same object and after 1 second we validate if the object is different from the first two

### BY_ARGS_HASH


```python
import meeseeks
import time

@meeseeks.OnlyOne(by_args_hash=True)
class A:
    def __int__(self, *args, **kwargs):
        pass

a1a = A(1, var_a="a", var_b="b")
a1b = A(1, var_b="b", var_a="a")
a1c = A(10, var_b="b", var_a="a")



assert a1a == a1b
assert a1c != a1b
```
In this example, we set  `by_args_hash` variable to `True` and validate if the first two calls result in the same object despite the kwargs order being different. The last validation shows us that different args and kwargs result in different objects.
