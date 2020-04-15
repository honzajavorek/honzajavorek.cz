Title: Virtualenv for beginners (and JavaScript developers)
Reviewers: Honza Král, Adéla Popelková, Míla Votradovec, Věroš Kaplan, Stařenka


When I grappled with learning Git twelve years ago, I found an article titled [Git for Idiots (and Java developers)](https://trak3r.blogspot.com/2008/04/git-for-idiots-and-java-developers.html). I&nbsp;wasn't exactly a Java developer, but I've been using Eclipse and Subversion, so it worked very well for me. It became my favorite cheat sheet. I've used it many times myself and shared it with many friends.

Today I'd like to steal the title for an article addressing a topic I believe many people grapple with: Python's virtual environments. But it's 2020, so I made a few changes to the wording 😉

## What is a virtualenv?

A virtualenv, short for _virtual environment_, is a developer tool that allows you to have your project's dependencies isolated from the rest of the system. It starts to be handy when your project needs dependencies installed by `pip`, but it is especially useful when you work on multiple Python projects on one computer. Having a separate virtualenv for each of your projects prevents their dependencies from clashing with your system or with each other.

Virtualenvs are [terrariums](https://en.wikipedia.org/wiki/Terrarium) for your Python projects!

> **Example:** Your project _todo-list_ requires a dependency [requests](https://pypi.org/project/requests/) to be in version 2.0 at least, but your older project _youtube-video-downloader_ depends on requests in version 1.5. You cannot satisfy both conditions without isolating the projects in virtualenvs.
>
> **JavaScript developers:** You probably already know that, but let's be sure: `pip` is like `npm`.

## How do I create one?

Let's create a project first. Create a new directory with a Python file `hello.py`, which looks like this:

```python
print('Hello!')
```

Now go to that directory in your terminal, so that if you list files in your current working directory with `ls` (Linux, macOS) or `dir` (Windows), you see something like this:

```
$ ls
hello.py
```

Now let's create a virtualenv. It's bundled with Python, so we don't need to install anything. Run this:

```
$ python -m venv venv
```

> **Troubleshooting:** It's bundled with Python ≥ 3.3. If you're getting errors like `No module named venv`, you have unsupported Python version — at the time of writing this article, the oldest Python to be used is 3.5. Check your Python version with `python --version`, and find or install a newer one. If you're quite sure you already have a newer one somewhere, try `python3` instead of `python`. I know, [it's complicated](https://xkcd.com/1987/).

The first `venv` is the name of a [built-in Python module for creating virtualenvs](https://docs.python.org/3/library/venv.html). It's always gonna be `venv`. The second `venv` is the name of a directory where the virtualenv should be created. It can be anything, but it's conventional to call it `venv`, and yes, it's a bit confusing. In fact, you could use `python -m venv ./venv` with the same effect.

The command won't print anything, but it creates a `./venv` subdirectory in your current working directory. It's gonna contain some infrastructure for the virtualenv itself (scripts, [symlinks](https://en.wikipedia.org/wiki/Symbolic_link)), and all dependencies you later install.

If you now list files in your current working directory with `ls` (Linux, macOS) or `dir` (Windows), you should see the new subdirectory:

```
$ ls
venv
hello.py
```

> **JavaScript developers:** The `./venv` directory is like `./node_modules`.

## How does it work?

Now the virtualenv contains a few subdirectories. One of them is `./venv/bin/` where you can find isolated `python` and `pip` executables. So `./venv/bin/python` is a Python living inside the virtualenv terrarium, and you can use it the same way as the `python` command you know:

```
$ ./venv/bin/python hello.py
Hello!
```

The difference is that this Python has access to everything installed in the virtualenv. Let's see exactly what that means. At this moment, if we run our program with this isolated Python, it's gonna be the same as running it with the usual, global `python` command:

```
$ ./venv/bin/python hello.py
Hello!
$ python hello.py
Hello!
```

But let's add dependencies to the mix. Let's change our program so it needs [requests](https://pypi.org/project/requests/):

```python
import requests

number = input('Hello! What is your favorite number? ')
print(requests.get('http://numbersapi.com/' + number).text)
```

Now the program not only greets the user, but also downloads and prints a random trivia about their favorite number. For the program to work, the requests library needs to be downloaded and installed. We could use the global `pip` to do that and run `pip install requests`, but that would:

- Make requests accessible to any Python program running on your computer.
- Create an opportunity for clashes if different versions of requests are required by different projects.
- Make it difficult to ever uninstall requests. You'll forget which of your projects need it and which don't.
- Require admin permissions to install (e.g. `sudo` on Linux or macOS).

For the above reasons, we'll want to use `./venv/bin/pip`, which is isolated in the "terrarium". That one only sees what's in the virtualenv and doesn't know anything about the surrounding world.

```
$ ./venv/bin/pip install requests
```

Now if we run the program with Python from inside the virtualenv, it's gonna work:

```
$ ./venv/bin/python hello.py
Hello! What is your favorite number? 42
42 is the answer to the Ultimate Question of Life, the Universe, and Everything.
```

However, if we try to run the same program with the global Python, it's gonna complain that the requests library isn't installed:

```
$ python hello.py
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```

If you peek into `./venv/lib/python3.7/site-packages/` (the `python3.7` might contain different numbers depending on what Python version you're using), you'll see all dependencies installed in the virtualenv:

```
$ ls ./venv/lib/python3.7/site-packages/
certifi
certifi-2019.11.28.dist-info
...
requests
requests-2.23.0.dist-info
...
```

There's not just requests, because the requests library itself has some dependencies too, so all of them were also installed. Of course, figuring out what's exactly installed by looking into a directory is a bit clunky. `pip` can do it for you:

```
$ ./venv/bin/pip freeze
certifi==2019.11.28
chardet==3.0.4
idna==2.9
requests==2.23.0
urllib3==1.25.8
```

If you run `pip freeze` with the global `pip`, it prints your globally installed Python packages. For the above-listed reasons, installing dependencies globally is not recommended. It's sometimes handy for programs (like [HTTPie](https://httpie.org/)), but only for those you want to access from anywhere in your system. Keep the list short!

> **JavaScript developers:** The `./venv/bin/` directory is similar to `./node_modules/.bin/`. Installing with `pip` is like `npm install --global` and installing with `./venv/bin/pip` is like `npm install`.

## Using magic to control virtualenv

Using `./venv/bin/pip` is very explicit and straightforward. The only problem is that it's a lot of characters to type. And when developers are lazy to type something explicit, they add "magic". Magic is something which saves you time and typing, but it's implicit and incomprehensible at first sight, if you're not already familiar with it. In beginner's eyes, magic translates as confusion. Take a deep breath and let's go through it!

Every virtualenv is born with a few handy scripts for "activating" and "deactivating" it. When you want to work on your project, you can activate its virtualenv like this:

```
$ . ./venv/bin/activate
```

Mind the dot in the beginning. It's actually equivalent to the `source` command, so if the dot feels too eerie, feel free to use the following:

```
$ source ./venv/bin/activate
```

And, of course, if you're on Windows, it's completely different:

```
$ .\env\Scripts\activate
```

All the three above do the same thing. They activate the virtualenv at hand. The `activate` is a shell script — a file full of terminal commands. When it's "sourced", it's like if you've written the commands yourself and executed them in your terminal. What do they do? They're the spells you need to cast to enchant your terminal:

```
(venv)$
```

See? Your terminal prompt is now prefixed with parentheses and the word "venv". That means it has been successfully enchanted. Now when you type `python` in your terminal, it'll automagically translate as `./venv/bin/python`!

```
(venv)$ python hello.py
Hello! What is your favorite number? 5
5 is the number of kyu (pupil) grades in judo.
```

The same now works for `pip` as well as any other executables from the `./venv/bin/` directory:

```
(venv)$ pip freeze
certifi==2019.11.28
chardet==3.0.4
idna==2.9
requests==2.23.0
urllib3==1.25.8
```

Confusing? Sure! Handy? Yeah! I told you, this is dark terminal magic. But if used right, it really saves a lot of typing — and that's definitely worth risking accidentally summoning some Bash demons.

Once you're done with your work on the project, you can deactivate it by another, rather straightforward magic spell:

```
(venv)$ deactivate
```

From now on, both `python` and `pip` are pointing back to the global commands, and the only way how to reach the ones from virtualenv is again typing their full path, i.e. `./venv/bin/python` and `./venv/bin/pip`. And that's it!

> **Hint:** When the virtualenv is activated, you can't easily reach the global `python` or `pip` commands. If you need them, deactivate the virtualenv or open a new terminal window.
>
> **JavaScript developers:** The `activate` and `deactivate` magic is something that is partly included in the `npm` itself, partly something available through the `npx` utility.

## Specifying dependencies

You are maybe wondering how you could send your project to a friend in a way that they can run it with all dependencies installed. Should you send them the `./venv` directory? Should the `./venv` directory be committed to Git?

Virtualenvs are ephemeral. You need one, you create one. Something's off? You can delete the directory and create a new virtualenv. They shouldn't be something you send anyone or share in Git. The best practice is to put the name of your virtualenv directory to the `.gitignore`, so it can never get picked up by Git.

But if virtualenvs are to be created and deleted regularly, then re-creating one for a project with 20 dependencies might get quite deadening. That's why it's a good idea to record dependencies of your project in a file called, by convention, `requirements.txt`. Let's create one for our project with the following content:

```
requests
pytest
```

I've added [pytest](https://pypi.org/project/pytest/) just in case we'd like to write tests for our project — and to illustrate how it works if the project has more than one dependency. If you now list files in your current working directory with `ls` (Linux, macOS) or `dir` (Windows), you should see the new file:

```
$ ls
venv
hello.py
requirements.txt
```

Now if you want to have all the listed dependencies installed, all you need to do is to run `pip` with the `-r` argument and the name of the file:

```
$ ./venv/bin/pip install -r ./requirements.txt
Requirement already satisfied: requests ...
Collecting pytest ...
```

As you can see, `pip` goes line by line and installs every listed dependency. If it's already installed, it considers the requirement satisfied and moves on to the next one.

The `requirements.txt` file should be tracked by Git and distributed with your code. With the file at hand, anyone who has your project on their computer and wants to run it, can create their virtualenv and easily install all required dependencies into it.

Perhaps first you've spotted the `pip freeze` command, you were wondering why it's called freeze and not list? That's because the primary purpose of it is to freeze your virtualenv — by generating a `requirements.txt` file! On Linux or macOS, you can save a command's output into a file using the `>` character like this:

```
$ ./venv/bin/pip freeze > ./requirements.txt
```

It's equivalent to running `./venv/bin/pip freeze`, saving its output to clipboard, opening the `requirements.txt` file, and overwriting its contents with the contents of your clipboard. So now the file contains a complete list of the dependencies installed in your current virtualenv, including versions:

```
attrs==19.3.0
certifi==2019.11.28
chardet==3.0.4
idna==2.9
importlib-metadata==1.6.0
more-itertools==8.2.0
packaging==20.3
pluggy==0.13.1
py==1.8.1
pyparsing==2.4.6
pytest==5.4.1
requests==2.23.0
six==1.14.0
urllib3==1.25.8
wcwidth==0.1.9
zipp==3.1.0
```

Way less vague than the manual specification! This can be still used with `pip`:

```
$ ./venv/bin/pip install -r ./requirements.txt
Requirement already satisfied ...
Requirement already satisfied ...
Requirement already satisfied ...
```

If you keep `requirements.txt` file like this around your code, anyone can easily create a virtualenv with exactly the dependencies you used to develop your project. Of course, you need to update the file (freeze your virtualenv) every time you install or uninstall dependency in your virtualenv.

> **Note:** Only dependencies installed by `pip` go to the `requirements.txt` file. If your project uses modules from Python's standard library, such as `random` or `math`, those shouldn't be listed. They are always already present as they're bundled with Python, and don't need to be installed.
>
> **JavaScript developers:** The `requirements.txt` is like `package-lock.json` or `yarn.lock`. If dependencies are specified without their version constraints, it can, kind of, work as `package.json`, too.

Specifying dependencies using the `requirements.txt` is easy and it works well for scripts or web apps. However, it's good to know that there are also other ways to do this — libraries, for example, use `setup.py` files. There are also emerging new formats like `pyproject.toml`. Those are out of the scope of this article though and it usually takes time until a beginner needs them. The [Python Packaging User Guide](https://packaging.python.org/) is a good resource to learn about that.

> **JavaScript developers:** The `setup.py` or `pyproject.toml` are like `package.json`.

## Where do virtualenvs live?

It's customary virtualenvs live in a directory right alongside your project, usually called `venv`, and you add the name of the directory to your `.gitignore` so it's not tracked by Git. You track dependencies in your `requirements.txt` file, which is also alongside your project, but tracked by Git. Thanks to this file you or anyone else can re-create the virtualenv and use the project with its dependencies.

However, you should know there are several tools which build on top of virtualenvs (as if it wasn't complicated and confusing enough already) and they work in a bit different way. They are out of the scope of this article, but you may see them out in the wild, and people enthusiastic about them will try to convince you that you should use them:

- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/) introduces a central location for all virtualenvs and adds more magical spells to save you more typing, such as `mkvirtualenv` or `workon`
- [direnv](https://direnv.net/) allows you to drop `.envrc` files into your directories, which can activate or deactivate virtualenvs, environment variables, anything…
- [pipenv](https://pipenv.pypa.io/) introduces new formats for tracking dependencies, `Pipfile` and `Pipfile.lock`, and it bundles everything together — `pip`, virtualenvs, and whatnot

It's up to everyone what they want to use, it's their workflow and their computer. As far as you have a virtualenv created, dependencies installed, and the project working, it's nobody's business if you achieved it with `python -m venv ./venv` or with `mkvirtualenv`. Although the above isn't entirely true for `pipenv`, because if a project you want to work on uses it for dependencies, you pretty much can't avoid learning it and using it.

For a beginner in 2020, I think all of them are unnecessary magic, i.e. confusion. Stick with pure virtualenvs. You have plenty of time to learn any of the above later, when you properly understand what the basics are about.

## What is this other virtualenv I've found on the internet?

If you [search the internet for the word virtualenv](https://duckduckgo.com/?q=virtualenv), there's a high probability you'll find the [virtualenv utility](https://virtualenv.pypa.io/). It can be very confusing.

The virtualenv utility is the original implementation of virtual environments before it got bundled to the Python itself as the [venv](https://docs.python.org/3/library/venv.html) module. For Python < 3.3, installing this original utility was the only way to get virtualenv working. Although the documentation of the utility mentions it still has some advantages over the built-in module, there is no real reason for the mere mortals like us to install and use it.

If you need official documentation on how virtual environments work, use [the one for venv](https://docs.python.org/3/library/venv.html).

## Summary

As you've probably noticed, the article isn't as short as the [Git for Idiots (and Java developers)](https://trak3r.blogspot.com/2008/04/git-for-idiots-and-java-developers.html) was. That's partly because I'm a total failure when it comes to short articles, and partly because this isn't a cheat sheet, this is a tutorial.

Of course, there are [existing tutorials](https://realpython.com/python-virtual-environments-a-primer/), but I decided to write my own, because I feel like the existing ones are either outdated, mixing things, or starting with the magic instead of explaining the basics first.

I hope I helped you to understand Python's virtual environments! Here's the [**TL;DR** you can return to](#cheatsheet):

<a name="cheatsheet"></a>

### Starting a new project

1. Create the project directory, e.g. `mkdir ~/Projects/my-project/`, and go inside
4. Create a virtualenv: `python -m venv ./venv` (or `python3 -m venv ./venv`)
5. Activate the virtualenv: `source ./venv/bin/activate` (or `.\env\Scripts\activate`)
7. Do what you need to do with the project
8. Every time you (un)install a new package by `pip`, make sure to update the `requirements.txt` file either manually or by `pip freeze`
9. When you're done, close your terminal or type `deactivate`

### Cloning a project from GitHub

1. Say you're supposed to work on a project [github.com/honzajavorek/honzajavorek.cz](https://github.com/honzajavorek/honzajavorek.cz)
2. Clone the project on your machine
3. Go to the project directory, e.g. `cd ~/Projects/honzajavorek.cz/`
4. Create a virtualenv: `python -m venv ./venv` (or `python3 -m venv ./venv`)
5. Activate the virtualenv: `source ./venv/bin/activate` (or `.\env\Scripts\activate`)
6. Install dependencies: `pip install -r requirements.txt`
7. Do what you need to do with the project
8. Every time you (un)install new package by `pip`, make sure to update the `requirements.txt` file either manually or by `pip freeze`
9. When you're done, close your terminal or type `deactivate`

### Business as usual on an existing project

1. Go to the project directory, e.g. `cd ~/Projects/my-project/`
5. Activate the existing virtualenv: `source ./venv/bin/activate` (or `.\env\Scripts\activate`)
7. Do what you need to do with the project
8. Every time you (un)install a new package by `pip`, make sure to update the `requirements.txt` file either manually or by `pip freeze`
9. When you're done, close your terminal or type `deactivate`
