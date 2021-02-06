Title: How to create a non-interactive Discord bot
Image: images/rock-n-roll-monkey-FTfjMijq-Ws-unsplash.jpg
Lang: en
Reddit-Comments: https://www.reddit.com/r/discordapp/comments/ldxi2l/how_to_create_a_noninteractive_discord_bot_honza/
Twitter-Comments: https://twitter.com/honzajavorek/status/1358035919807385602
HackerNews-Comments: https://news.ycombinator.com/item?id=26046309


I recently started a [club for Czech & Slovak juniors in tech](https://junior.guru/club/), which runs on [Discord](https://discord.com/). To be able to do some record keeping, or create a dynamic showcase of current members on the club page, I wanted to create a script, which would connect to Discord's API on a daily basis, download some data, then terminate.

But as I learned, people usually strive for interactive bots with continual runtime, so all the tooling and tutorials describe that use case. After figuring it all out pretty much myself, here I present a missing tutorial for building a non-interactive bot, a one-time script.

![Robot]({static}/images/rock-n-roll-monkey-FTfjMijq-Ws-unsplash.jpg)
Photo by [Rock'n Roll Monkey](https://unsplash.com/@rocknrollmonkey)

I'll be using Python and the [discord.py](https://discordpy.readthedocs.io/) library. There are myriads of tutorials on how to start and set up a Discord bot in Python, so I won't be covering that. Be guided by the [Getting started](https://discordpy.readthedocs.io/en/latest/index.html#getting-started) section of the discord.py docs.

I'll add only one pro tip, which I don't think the docs cover very well. To be able to interact with the Discord API, you'll need to reference your server (in the API terminology it's _guild_), your channels, users, etc. using IDs, but it's not very clear where those IDs come from. The trick is that you need to [switch your Discord app to dev mode](https://www.swipetips.com/how-to-get-channel-id-in-discord/) and then you can get the IDs using the context menu.

Now let's say you went through the intro, finished it with the following code, and it works for you:

```python
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('... token ...')
```

As you can see, this is an interactive bot, which prints out a message when it starts, then runs indefinitely and listens to messages, reacting to greetings. Under the hood, the code uses [asyncio](https://docs.python.org/3/library/asyncio.html) to communicate with the API, and as soon as the `client.run()` happens, it runs in an asyncio loop forever. That's kind of cool, but we won't need any of that. We want to spin up the loop, do whatever we need, then immediately stop the loop and terminate the program.

## Creating a one-time script

```python
import discord

class NonInteractiveClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        print('We have logged in as {0.user}'.format(self))
        await self.close()

client = NonInteractiveClient()
client.run('... token ...')
```

The code above is very different, but part of it is because it takes a different approach to using the client. The previous program instantiated the client class and then used the `@client.event` decorators to register listeners to various events. This code inherits from the client class, implements the listeners as methods, and then runs this custom client's loop. I suspect these approaches are equivalent, but when I searched for solutions and asked around, this inheritance-based approach was what I got, so this is what I'm using in my solution.

When `client.run()` executes, it spins up an endless loop. The _ready_ event fires, which triggers the `on_ready()` method. In it, we use `self.wait_until_ready()` until everything is in place. Now we can do our non-interactive work, which is represented by the `print()` call in the example. When we're done, we explicitly close the client, which also stops the loop and lets the program to end, instead of hanging forever.

## Adding error handling

This would be all great, but there's one problem. When error happens, it prints out, but the program hangs. Even if you do some changes to the code and force the program to end on error, it's hard to ensure it has a correct exit code. Exit code of a program should be 0 if all went nice and smooth, but it should be 1 (more precisely, non-zero) in case of a problem. If we run the script as part of a CI job (CircleCI, GitHub Actions…) and it fails, returning a non-zero code ensures the whole job fails. So how do we do this?

The issue is multi-level. First, the discord.py library eats the errors. Second, the asyncio loop eats the errors. If there's an exception raised, it won't crash the program. It gets eaten by one of the error handlers, printed, but silenced. This is a desired behavior in case of a long-running process, where the program is expected to log errors for later inspection, but ideally recovers and continues to do its job. In a one-time script, we want exactly the opposite.

### Working around discord.py

```python
import discord

class NonInteractiveClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        print('We have logged in as {0.user}'.format(self))
        await self.close()

    async def on_error(self, event, *args, **kwargs):
        raise

client = NonInteractiveClient()
client.run('... token ...')
```

In the example above, we added an `on_error()` listener method, which by default eats errors, but we implemented it in a way that it re-raises them. This way we can work around the discord.py behavior, but it isn't enough for the program to crash on error, because the asyncio loop will still eat it.

### Working around asyncio

Luckily, `client.loop` allows us to access the loop object and we can modify the behavior. It's not gonna be very nice, but it's gonna work and that surely counts.

```python
import discord

class NonInteractiveClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        print('We have logged in as {0.user}'.format(self))
        await self.close()

    async def on_error(self, event, *args, **kwargs):
        raise

client = NonInteractiveClient()

exc = None
def exc_handler(loop, context):
    nonlocal exc
    exc = context.get('exception')
    loop.default_exception_handler(context)
    loop.stop()

client.loop.set_exception_handler(exc_handler)
client.run('... token ...')

if exc:
    raise exc
```

So the `client.loop.set_exception_handler()` allows us to specify our own error handler. I've found it [deep in the Python docs](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler). It expects a _handler_. That's a fancy name for a function, which would be called in case an error occurs. In such case, it will be given the _loop_ object as the first argument and something mysterious called _context_ as the second. The docs say this:

> _context_ is a `dict` object containing the details of the exception (see `call_exception_handler()` documentation for details about context).

Down the rabbit hole, [the linked docs](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler) explain all the contents of the dictionary. We see that the actual exception can be found under the `exception` key. So in the example code above, we add a custom error handler, `exc_handler()`, and pass it to the `client.loop.set_exception_handler()`. In this custom handler we get the exception object from the context, save it to a global variable `exc` (actually _nonlocal_ variable, but in this case it doesn't matter), then call whatever default exception handler the loop has, and stop the loop.

So now, when error occurs, we re-raise it in the `on_error()` listener (discord.py level), and our custom `exc_handler()` gets called (asyncio loop level), which saves the exception object for later and stops the loop. At that moment, `client.run()` stops blocking the program and the lines after it can be executed. In a simple `if` statement we can peek if an error happened. If yes, we can finally raise it like normal synchronous Python beings, without any loop magic interfering anymore. This crashes the program and sets the exit code to 1. If there is no error (the `client.run()` has been stopped by `self.close()` in `on_ready()`), the program ends normally.

## Full program

The example below adds a separate function for the actual code of the one-time script. It loads members of a specific Discord server, aka _guild_, and [pretty prints](https://docs.python.org/3/library/pprint.html) them one by one. The ugly rest is the infrastructure needed to work around all the built-in loop architecture.

```python
import discord
from pprint import pprint


# Actual code of the one-time script, which does something useful

async def run(client):
    guild = client.get_guild(123445...)
    for member in guild.members:
        pprint(member)


# The ugly rest

class NonInteractiveClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        await run(self)
        await self.close()

    async def on_error(self, event, *args, **kwargs):
        raise

client = NonInteractiveClient()

exc = None
def exc_handler(loop, context):
    nonlocal exc
    exc = context.get('exception')
    loop.default_exception_handler(context)
    loop.stop()

client.loop.set_exception_handler(exc_handler)
client.run('... token ...')

if exc:
    raise exc
```

## Closing notes

This all took me a while to figure out. It's not very beautiful, but it seems to work as I need. If anyone knows of a better, shorter, nicer code, which achieves the same, I'd be happy if you share it with me in the comments. Also, thanks a lot to [@Rapptz](https://github.com/Rapptz) for [guiding me the right way](https://github.com/Rapptz/discord.py/discussions/6278).
