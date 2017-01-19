Title: Testing in JavaScript and in Python
Date: 2017-01-18 10:43:00


In this article, I'd like to share why I'm disappointed about testing server-side JavaScript. If you're not in the mood of reading [rants](http://www.urbandictionary.com/define.php?term=rant), I recommend you to choose a different article for your afternoon.

I'm originally a Python person, so I'm going to compare _developer experience_ of both languages to be clear about what exactly is bothering me. Although I'm a big fan of Python and I'm heavily involved in the [Czech Python user group](http://python.cz/), my intention isn't to write down hateful text on JavaScript and to say that Python is the best language in the world. I just want to point to certain flaws in one of the two ecosystems. Next time I'm completely okay to write a text about how I hate Python packaging and why npm feels much better.

## Testing in Python

Many folks use the [unittest](https://docs.python.org/3/library/unittest.html) when writing tests in Python. It's a module of Python's standard library, which allows people to quickly jump into [XUnit](https://en.wikipedia.org/wiki/XUnit) way of writing tests, full of `class TestSomething`, `self.assertThis()` and `setUp/tearDown` that.

While unittest is able to find and run tests, when the test suite grows larger, people often get a alternative third-party test runner, for instance [nose](http://nose.readthedocs.io/en/latest/). The aim of having a dedicated test runner is to find and run tests in a smart way - e.g. just those, which previously failed.

Thanks to the fact nose runs tests, it allows you to leave the XUnit style behind and offers some extra tricks how to make your tests better and simpler. Usually people don't use them though, because they don't know about them. However, in general, if you want to run a particular set of your tests or control the output of testing, test runner always has a smart command line option to do exactly that. That's very convenient primarily because it provides:

- Convention (my colleague doesn't need to learn which options are available in a project),
- comfort and developer experience (the option is there for me even when it's just three times in my lifetime I need it).

And then there's [pytest](http://pytest.org/), a framework, which is probably capable of everything nose can do, but adds even more and often crazy ways how to simplify writing of tests. Although idiomatic Python should opt for [_be explicit_ and _no magic_](https://www.python.org/dev/peps/pep-0020/), the popularity of pytest has proved that in case of tests, magic is acceptable and useful. It turns out, it can make tests more readable and declarative.

Thanks to the fact a person who wrote [PyPy](http://pypy.org/) (interpreter of Python written in Python) is part of the team which works on pytest, the magic goes into pretty deep levels of the language. For example, Python has a keyword `assert`, which is by default quite primitive. It can just compare two values and raise a generic assertion error if they don't match. Basically it works the same way as [assert function
in Node.js](https://nodejs.org/api/assert.html). However, pytest [leverages introspection to dive into bytecode of the Python interpreter](http://pybites.blogspot.co.at/2011/07/behind-scenes-of-pytests-new-assertion.html) and enhances [asserts](https://pytest.org/latest/assert.html) in such way they're able to recognize what they're comparing. This way even the basic assert statement can provide very nice output. And I don't need a cheatsheet to find the right `assert.whateverComparisonFunction`, I write plain Python code, using just built-in operators and types.

I also like the fact frameworks usually provide sections about testing in their documentations and give me a hand (guides, tips, tools, classes to inherit from) so I could test my application in simpler and faster ways, without writing redundantly detailed [boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code). See [Flask](http://flask.pocoo.org/docs/0.12/testing/), [Django](https://docs.djangoproject.com/en/1.10/topics/testing/), [Scrapy](https://doc.scrapy.org/en/latest/topics/contracts.html) (links to dedicated chapters in respective docs).

At the end of the day, I feel very comfortable when writing tests in Python. I can write a website using a microframework, but even such stripped-down tool still gives me means to simplify writing tests. Often a test is just a few lines long, which saves my time, time of my code reviewer, and time of all other people reading the test suite in the future. I can easily run any set of tests I need, e.g. just those which didn't pass.

## Mocha

In the world of server JavaScript, which I had the chance to meet in [Apiary](https://apiary.io/) where I currently work, the golden standard is [Mocha](http://mochajs.org/). The _feature-rich_ in their claim means that even the [assert library](http://chaijs.com/) needs to be installed separately. Okay, now seriously. _Killer features_ of Mocha look like this:

- It runs all tests and if I type `.only` in code of my tests, I can run just that particular test,
- it allows usage of _glob patterns_ to select which tests I want to run,
- it allows me to grep through descriptions of tests (if the grep matches more descriptions, all of them get ran),
- wannabe-[BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) approach, which composes of `describe` and `it`,
- tons of boilerplate code in `before` or `beforeEach` (because [_Mocha currently has no concept of a shared behaviour..._](https://github.com/mochajs/mocha/wiki/Shared-Behaviours)),
- if test fails, it's sometimes hard to even realize in which file the problem happened,
- docs are just a bit less terrible than those of [Mongoose](http://mongoosejs.com/),
- it's able to print test results in colors, using unicode character ✔️, which is very cool,
- it allows to use just one reporter at a time (good luck generating test coverage or `xunit.xml`).

Just to give an idea, what are pytest _killer features_:

- No XUnit classes, no faux BDD, just [plain functions](http://docs.pytest.org/en/latest/getting-started.html#our-first-test-run) with [simple asserts](http://pytest.org/latest/assert.html),
- helps to uncover [what the hell actually happens](http://pytest.org/latest/example/reportingdemo.html),
- automatic [management of `stdout` when running tests](http://pytest.org/latest/capture.html)
- concept of [fixtures](http://pytest.org/latest/fixture.html) for writing dependencies of individual tests,
- [parametrization of tests](http://pytest.org/latest/parametrize.html),
- [distributed testing](http://pytest.org/latest/xdist.html),
- is able to run any Python tests, [nonpython tests](http://pytest.org/latest/example/nonpython.html), or [documentation tests](https://docs.python.org/3/library/doctest.html).

I can't blame Mocha or [Chai](http://chaijs.com/) they're not using introspection to go deep into bytecode, because JavaScript has no real introspection and neither has bytecode. The thing is, Mocha can probably easily implement the rest, but it's not doing so. See [this feature request to parametrize tests](https://github.com/mochajs/mocha/issues/1454) (something I consider a basic feature of a decent general-purpose test framework), which includes also rant about Mocha maintainers refusing new features as not needed or not reviewing them at all.

But it's not just about maintainers. All right, there's no supply, but surprisingly, there's also no demand. From search and GitHub issues I'm getting an impression that nobody in the Node.js ecosystem has any ambitions to use or want such features. It looks like most of the writers of Mocha tests probably don't even know these things can exist. The result being,

- they won't work on these things and contribute them,
- in larger test suites their tests uncontrollably grow into 1000 lines long files full of boilerplate code, which are both hard to read and hard to be executed.

If they could somewhere spot the existence of parametrization or management of fixtures, maybe they would embrace the concepts and they'd try to use them to write cleaner tests. But it's not available, so tests get often just copy-pasted, [DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself)-ied out by `forEach`, or by ad-hoc functions to share assertions. I don't even know which of these approaches is worse. The former is readable, but non-manageable, the later is non-readable, but at least illusively more manageable.

## npm to the rescue - or not

A person who is familiar with Node.js knows that searching npm packages is usually the ultimate answer to solve everything. But as I already indicated, because of a missing demand, this is not completely true for this case. Even if the packages exist, [they often have up to 10 commits and the last one is 2 years old](https://github.com/jpstevens/mocha-shared). The authors probably already jumped on writing [Elm](http://elm-lang.org/) exclusively, so they don't bother with new versions... Moreover, it seems like Mocha-related packages usually just fix what's broken, not add any cool new features to make the _developer experience_ better.

In the time of writing this article, [mocha-clean](https://github.com/rstacruz/mocha-clean) is a Mocha extension with the most stars on GitHub. Well, among those which actually add something to Mocha - I've excluded integrations, such as Mocha + React, Mocha + Mongo, Mocha + browser, etc. You know what mocha-clean does? It fixes stack traces.

What else I'd like to have? Look at [pytest-testmon](https://github.com/tarpas/pytest-testmon/). An extension, which leverages code coverage to execute just the tests which make sense to be ran again. I.e. something, which extremely improves productivity. No more manual `.only` or wearing grepping.

And regarding controlling of which tests to run or how the output should look like, even if I found an npm package adding my desired command line options, it won't be a standard implementation, standard convention, which a new colleague would be automatically familiar with.

## Trends

I'm writing this article as a result of a long-term frustration of the fact that when testing in JavaScript, you need to not only reinvent the wheel, but that nobody is actually even attempting to deliver the wheel. Not even new funky, shiny, fashionable, hyped, ... projects like [AVA](https://github.com/avajs/ava) try to fight against [spaghetti](https://en.wikipedia.org/wiki/Spaghetti_code) tests. Just reading the `README` I can't see anything which would be trying to solve any of the problems I mentioned. AVA looks like Mocha with a different syntax, even less features (i.e. it will require a brand new `ava-*` ecosystem of extensions) and just one and only _killer feature_, asynchronous tests (Promises, async/await). Of course, that's something which isn't available in pytest...

[Oh await!](https://pypi.python.org/pypi/pytest-asyncio)

All right, I won't be that vicious. AVA clearly leads to isolation of tests and extremely speeds up runtime of the test suite. I admit, that looks really great. But there's nothing to help me to write complex tests in simple ways, to structure them better, and so on. The authors burned a lot of time to provide integrations with Babel and React and TypeScript, but that's not going to help me to save time when writing tests. Those are not features, it's just clowning of the JavaScript ecosystem, which doesn't bring any real value to me, a regular user.

## TL;DR

To sum it up, there are two main issues on testing in JavaScript, which disappoint me:

- Because of language limitations, no library can provide asserts like those in pytest (or declarative decorators, but that's something coming to JavaScript probably very soon).
- If AVA is a successor of Mocha and represents the future of JavaScript testing, then JavaScript testing frameworks are not pursuing simpler and more comfortable writing of tests, but faster execution thanks to parallelization (thumbs up) and _fashion as a feature_ (grumpy cat). I can't see even smart test runner emerging, and that's something Python world was passionate about years ago and now it's a commodity. Today Python is buzzing with making tests structured, managable, more readable. In comparison with JavaScript, this sounds like very distant _first world problems_. I'm sad nobody in the ecosystem is missing it, but I understand it's similar to promoting waste recycling in Sudan.

_In the middle of 2016 I wrote this article from pure frustration, in my mother tongue (Czech). It's available as [Testování v JavaScriptu a v Pythonu]({filename}2016-05-31_testovani-v-javascriptu-a-v-pythonu.md). In January 2017 I published this translation._
