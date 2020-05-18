Title: Notify yourself from Python
Image: images/luis-perdigao-JMabq3k4gk8-unsplash.jpg
Twitter-Comments: https://twitter.com/honzajavorek/status/1262378532476420096
Facebook-Comments: https://www.facebook.com/honzajavorek/posts/10158123579887707
LinkedIn-Comments: https://www.linkedin.com/posts/honzajavorek_notify-yourself-from-python-honza-javorek-activity-6668143772011896832-9cRv


Sharing a quick tip on how to get notification on macOS when a function in Python is done with its job.

![Reading]({static}/images/luis-perdigao-JMabq3k4gk8-unsplash.jpg)
Photo by [Luís Perdigão](https://unsplash.com/@scalabis)

## The problem

I'm working on a website for juniors in tech, [junior.guru](https://junior.guru/) (the content is Czech only so far, I'm sorry). There is a component with web scrapers made in [Scrapy](https://docs.scrapy.org/), which helps me to download and aggregate job advertisments from other places.

I often run the scrapers on my local computer, but since it takes a few minutes until they're done, I couldn't stop myself from switching to Twitter or something while waiting. Then I often found myself watching funny cat gifs one hour later, only hardly realizing that the scrapers are probably done by then and I can resume my work.

## Notification

If all you need to support is macOS, there are at least three simple ways how to notify yourself:

- Terminal sound,
- standard notification,
- the `say` command.

### Say say say

Oh, you didn't know about the `say` command? I'm sorry for ruining your productivity today then. Type the following to your terminal with sound on and see what happens:

```
$ say 'Hello!'
```

And yes, it works for other languages, too:

```
$ say -v zuzana 'Dobrý den, jedno pivo prosím'
```

In Python, it's easy to run commands using the `subprocess.run()` function, so in your script, one can do something like this:

```python
from subprocess import run

run(['say', '-v', 'zuzana', 'Jedno pivo prosím!'])
```

This thing has one major disadvantage though. There is a significant potential it scares the shit out of me. Just imagine - you sit in a silent room, and just like that, out of nowhere, there is a human voice talking to you. It's really spooky.

So I've used the other two options, to have feedback on both screen (when I'm with sound off) and from speakers (when I leave the computer to e.g. brew myself a cup of coffee).

### Terminal sound

Your terminal can make a sound. There's a dedicated [bell character](https://en.wikipedia.org/wiki/Bell_character) you can print and if you didn't mute sounds in settings or something, your terminal should beep whenever the character is printed. In Python, it can be done like this:

```python
print('\a')
```

Better, you can remove new line from behind the print, and you can flush the `stdout` immediately:

```python
print('\a', end='', flush=True)
```

If you don't know what's "flushing `stdout`", search for keywords "output buffering python".


### Standard macOS notification

With the [pync](https://pypi.org/project/pync/) library, you can send native macOS notifications directly from your Python code:

```text
$ pip install pync
```

Then in your Python program:

```python
import pync

pync.Notifier.notify('Hello!', title='Greeting')
```

Check out the library's README, there're more usage examples. My personal tip is to import it with exception handling, just in case someone wants to run your code somewhere else than on macOS:

```python
try:
    import pync
except ImportError:
    pync = None

if pync:
    pync.Notifier.notify('Hello!', title='Greeting')
```


## Decorator

Now I wanted to notify myself when a long-running function ends, but I didn't want to pollute the code of the function with printing bell characters or sending notifications. Also, what if there's an error and the function raises an exception? A solution is to have the code as a function decorator. Also, that way I can easily measure duration of the function and put the result into the notification:

```python
from functools import wraps
from time import time


try:
    import pync
except ImportError:
    pync = None


def notify(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time()
        try:
            return fn(*args, **kwargs)
        finally:
            t = time() - t0
            print('\a', end='', flush=True)
            if pync:
                fn_name = f'{fn.__module__}.{fn.__name__}()'
                pync.Notifier.notify(f'{t / 60:.1f}min',
                                     title=f'Finished: {fn_name}')
    return wrapper
```

That funky thing near the end is [advanced formatting](https://pyformat.info/#number) inside [f-strings](https://realpython.com/python-f-strings/). I have this code in a separate module, `timer.py`. (Module `timer`, function `notify`… well I'm unsure about proper naming yet, but this is what I have so far.) It can be used as follows:

```python
from .timer import notify

@notify
def long_running_function():
    ...
```

When the function is done, my terminal beeps and a notification appears:

> **Finished: myproject.mymodule.long_running_function()**<br>
> 3.5min<br>

Because the notifying part is in the `finally` block, it happens even if the function raises an exception. This is great, because if I make a typo in my code, run the scrapers, and muscle memory in my fingers immediately switches windows to Twitter, the sound and notification lets me know about the mistake immediately.

## Summary

Even if you don't need to notify yourself from a Python program, I hope this article gave you some inspiration for other problems you might be solving, or taught you some new tricks. Also, now that you know about it, find some [good use](https://www.youtube.com/watch?v=uyV0IVItlM4) for the the `say` program!

**Update:** If your program targets Linux as well, my friend [Vuyisile Ndlovu](https://vuyisile.com/) has written a [follow-up article](https://vuyisile.com/how-to-send-desktop-notifications-in-linux/) on how to send notifications on Ubuntu. Check it out!
