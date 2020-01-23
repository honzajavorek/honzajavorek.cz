Title: Courting Haskell
Image: images/pawel-czerwinski-LEbkdsB8OMg-unsplash.jpg
Twitter-Comments: https://twitter.com/honzajavorek/status/1217065971707449345
Facebook-Comments: https://www.facebook.com/honzajavorek/posts/10157720662087707
HackerNews-Comments: https://news.ycombinator.com/item?id=22044262
Reddit-Comments: https://www.reddit.com/r/haskell/comments/eokuao/blog_post_courting_haskell_honza_javorek/
LinkedIn-Comments: https://www.linkedin.com/posts/honzajavorek_courting-haskell-honza-javorek-activity-6625070791035756544-J3Hr


In the past two months I've been trying to learn the Haskell programming language. It's vastly different from anything I know, so it served me also as a way how to empathize with complete beginners to coding. This is a diary from my journey.

![Triangles]({static}/images/pawel-czerwinski-LEbkdsB8OMg-unsplash.jpg)
Photo by [Paweł Czerwiński](https://unsplash.com/@pawel_czerwinski)

## First sight love

I spent my university years juggling studying, freelancing, and partying. To accommodate all three, some sleep included, I decided to reframe courses as "tours into potentially interesting topics". Regardless whether I liked a course or not, I formally finished it with E, which was satisfactory to continue the school. E as in EFFICIENT.

Personally, I categorized the topics into three sets. Respectable ones, which are noble and beautiful, but too hard for me to get my head around them (e.g. math). Intriguing ones, which I wished to dive into later in my life (compilers, functional programming…). And finally, topics I never wished to see again, ever (e.g. hardware).

A superficial experience with Haskell programming language in one of the courses got stuck in my head as a divine encounter. Since then I have secretly desired to explore it further. It seemed to be as noble and pure as math, but unlike math, I felt there is a chance I could be able to actually learn how to do it without too much pain.

## What is Haskell?

> Haskell is a statically typed, purely functional programming language with type inference and lazy evaluation.
>
> — [Wikipedia](https://en.wikipedia.org/wiki/Haskell_(programming_language))

My first useful experience with programming was with PHP 4. Later I learned PHP 5 and its object-oriented programming concepts, dreaming about switching to Java one day. But then I've encountered Python and it changed everything. Unlike PHP, it seemed to be "purer" and "nicer". At that time, [PHP was a mess](https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/). Also, unlike Java or PHP (which at that time started to converge to Java), it seemed to be "simpler". It wasn't forcing me into so many [unnecessary layers and abstractions](https://sw-samuraj.cz/2019/02/remcani-proti-jave/) (and types and classes). In my eyes, Python was noble, pure, divine.

Over time I learned about Python's warts and imperfections, and my old memory of Haskell from university years gave me an irrational expectation that these things wouldn't happen there, because _Haskell is without compromises, it's divine, for real, it's the purest of all programming languages, invented by scientists…!_

> As of September 2019, Haskell was the 23rd most popular programming language in terms of Google searches for tutorials and made up less than 1% of active users on the GitHub source code repository.
>
> — [Wikipedia](https://en.wikipedia.org/wiki/Haskell_(programming_language))

Haskell isn't exactly popular. It's partly because it's exclusively [functional](https://en.wikipedia.org/wiki/Functional_programming). Most programmers start with imperative languages, perhaps spiced with object-oriented programming here and there. For someone coming from Python, Haskell is like from another world, which turns the learning into a tough experience. Another reason might be that unlike more mainstream functional languages, such as F# or Scala, it's not tied to any existing ecosystem, such as those of C# or Java.

Some people also say it's so academically pure that it's impractical and that it's too math-like. It's, indeed, heavily founded on mathematical theories (category theory and lambda calculus). You'll stumble upon whiteboards with diagrams, and even the most basic materials won't avoid using strange terms, such as monoids, monads, or functors. Check [videos from Bartosz Milewski](https://www.youtube.com/user/DrBartosz/videos) as an illustration of what I mean:

![Bartosz Milewski's YouTube channel]({static}/images/bartosz-milewski.png)

I don't say theory and whiteboards are bad, but it's not the usual experience when learning a new programming language, and for many it can be a bit intimidating.

This all causes people to think Haskell (perhaps [together with Lisp](https://twobithistory.org/2018/10/14/lisp.html)) is some sort of sorcery. First, Haskell and Harry Potter both start with H. Second, nobody truly understands why it all works, perhaps only the most ~~mad matematicians~~ powerful wizards. Third, the apprentices (nerds, in the eyes of the majority society) are encouraged to use eerie ~~syntax~~ script and to ~~speak in mathematical terms~~ cast bizarre spells, such as ~~_monad!_~~ _alohomora!_

Being aware of these things, I kept my desire for Haskell as something I'll probably never really pursue and I focused on mastering Python and later JavaScript as my tools of trade.

## FP sneaking into my life

I think it started in 2018, when [Vladimir Gorej](https://twitter.com/vladimirgorej) joined [Apiary](https://apiary.io/). Vladimir is a functional programming aficionado with strong theoretical background, who introduced us to [Ramda](https://ramdajs.com/) and [Ramda Adjunct](https://char0n.github.io/ramda-adjunct/), [RxJS](https://rxjs.dev/), and more. Suddenly, FP was all around me.

We attended the [LambdUp](https://www.lambdup.io/) conference. I started to write my imperative code with more pure functions, immutability, and with _maps_, _filters_, and _reduces_ in mind. I started noticing how widespread Ramda is, how popular [Elm](https://en.wikipedia.org/wiki/Elm_(programming_language)) is (I first heard about Elm at [Devel.cz 2016](https://devel.cz/konference/2016) from [Richard Feldman](https://twitter.com/rtfeldman)), and every day I kept being reminded about [Closure](https://en.wikipedia.org/wiki/Clojure) on Twitter by [Aleš Roubíček](https://twitter.com/alesroubicek/). Moreover, one of my other colleagues, a C++ genius [Thomas Jandečka](https://www.linkedin.com/in/tjanc/), couldn't pass a kitchen small talk without mentioning how powerful Haskell is.

## The Grand Budapest Hotel

<small markdown="1">Yeah, [pun intended](https://www.imdb.com/title/tt2278388/reference)!</small>

The last day of October 2019 was my last day in Apiary. I left to have a break from work for a few months and to have time to start [junior.guru](https://junior.guru/). Fresh to my sabbatical, in November I accompanied my wife on a business trip to Budapest. The weather was bad and I didn't feel entirely healthy, so while she was enjoying a conference, I ended up slacking in our hotel room. And I was quite in a mood to learn something new. What about finally learning _the real deal_?

Yeah, I could have chosen something everyone else is learning, like React or Go, but I didn't feel like being actually productive. I had a unique opportunity to learn _anything_, regardless its usefulness. So I decided I'll finally take a look at Haskell. Also, where else to start learning an obscure language if not in [Hungary](https://en.wikipedia.org/wiki/Hungarian_language)?

So I started. I knew [Learn You a Haskell](http://learnyouahaskell.com/) from the times of my university course, and I decided to give it a chance, because I remembered how the naive cartoons helped me to feel comfortable even around words like _functor_.

![The list monster]({static}/images/listmonster.png)
Cartoon by Miran Lipovača, taken from [An intro to lists](http://learnyouahaskell.com/starting-out#an-intro-to-lists)

After a few hours of continuous reading, I felt like [sharing my immense success](https://www.facebook.com/photo.php?fbid=10157585323962707&set=a.10151458393497707&type=3&__xts__%5B0%5D=68.ARA6QiDX2SzA2lZQRzKzNWT-NzBLDOw8JT5fzoUKoe5ZbdOcmhEglED2Su6VjGPD72lra_A23zHOzLDgcA_Aen5v6kD1alSnZ832C0i1iHNrVMNpREbJ6Ou8aYo-00FM5jIdtNHwjfsh4ZVuDAvGqX3Jc8zDjyOqApY5fQKiDys4MeyqaIcz2Za6-3kJ1IWJeAq96QCxvWCkzxtlpKHAvxm_ISP6zzmxgKJKgmijHwJKqiIqKpDlN8f2oVO5dGPjLDrMaQ&__tn__=-R) and as a true millennial, I concluded my day with writing more Facebook comments about how I learn Haskell than writing actual Haskell code.

I didn't stop learning though. Even after returning from the trip, I tried to find some time here and there to continue with the book. And it was a strange experience. After quite long time I was back in learning something this intensively. Also, as Haskell is so different from anything I know, more and more I felt like I'm able to empathize with programming beginners. That's usually very hard for a person who's coding for ~20 years. Even though I'm spending my time around beginners, [helping them](https://junior.guru/), and mentoring them, I didn't ever get as close to their troubles as I did when learning Haskell.

There are two types of materials for two types of learners. Some people like to first read and then try out stuff, some people require very practical, hands-on learning from the very start. I'm the reading type, so I didn't have any fundamental problem with [LYAH](http://learnyouahaskell.com/) as a learning material, but I have to admit the fact that [Hello World](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) is in [Chapter 9](http://learnyouahaskell.com/input-and-output) did feel a bit intimidating. It's not the book's fault though. Printing text is a [side effect](https://en.wikipedia.org/wiki/Side_effect_(computer_science)) and in a strictly [pure](https://en.wikipedia.org/wiki/Pure_function) language, you better read 8 chapters before you start with side effects!

## Advent of Code

My friend [Míla](https://twitter.com/MilaVot/) told me about [Advent of Code](https://adventofcode.com/), an advent calendar for puzzle solvers. Every day in December there's a programming puzzle and it's up to the solver how they come up with an answer, so it's a good opportunity for trying out new programming languages on small exercises. Programming puzzles aren't usually my thing, but this coincided with my Haskell learning, so why not? Apart from [Míla with Scala](https://github.com/miiila/aoc2019), I noticed other people joining: [Czechitas](https://www.czechitas.cz/en/) director [Dita Přikrylová with Python](https://twitter.com/ditaprikrylova/status/1201177777011118080), my ex-colleague [Stephen Mizell with Racket](https://github.com/smizell/aoc/), and more. That motivated me to try it out. Except it was 2nd of December and I didn't even know how to print text in Haskell yet…

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Learning <a href="https://twitter.com/hashtag/Haskell?src=hash&amp;ref_src=twsrc%5Etfw">#Haskell</a>. My goal was to try it out in the <a href="https://twitter.com/hashtag/adventofcode?src=hash&amp;ref_src=twsrc%5Etfw">#adventofcode</a>, but I&#39;ll be happy if I get to printing stuff out to terminal within the end of the year.</p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/status/1201608887302074373?ref_src=twsrc%5Etfw">December 2, 2019</a></blockquote>

Albeit late, in the end I started with the puzzles. They usually contained some test inputs and expected outputs, so I thought about solving the puzzles in a test-driven way. I didn't want to dive into installing Haskell packages yet and I didn't find anything for testing in the standard library, so I decided to go with writing small CLI programs and verifying them with [bats](https://github.com/bats-core/bats-core). Bash tests also have the benefit that they will work with any language, if I decided to go with a different one later. Following the example of others, I've set up a [repo with my solutions](https://github.com/honzajavorek/aoc/).

The first puzzles were okay. It was nice feeling to write my first Haskell program, and second, and third, and to practice the alien syntax and the functional approach. In the beginning, I felt like using Haskell for the puzzles is cheating. I just declaratively wrote down what I wanted and I got it. However, the puzzles got quickly harder and I found myself spending several hours per day solving them. And I don't think the language is to blame. I'd probably have the same issues when solving the problems with Python, which I know very well.

As I mentioned, programming puzzles are not my thing, and usually they cause me more pain than joy. I used to play [Interlos](https://interlos.fi.muni.cz/), an online puzzle game organized by people from [FI MUNI](https://www.fi.muni.cz/), but I bailed out a few years back when I realized that each year, _despair_ is the overwhelming emotion I'm getting from participating (in contrast with games for non-programmers such as [Sendvič](http://www.hrasendvic.cz/), which I can enjoy). I guess I'm not a "puzzle solver". I rather think of myself as a "project builder".

Well, enough of excuses. The third day I spent 7 hours to solve the puzzle, and, despite my success, I felt like shit for the rest of the evening. I decided there are perhaps better ways to learn Haskell - or to spend my sabbatical, when we're at it. I dropped out from Advent of Code, and I soothed myself by reading [functional.christmas](https://functional.christmas), a nice resource _with no annoying puzzles!_ someone sent me around that time.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Although I enjoyed it as my first real experience with <a href="https://twitter.com/hashtag/haskell?src=hash&amp;ref_src=twsrc%5Etfw">#haskell</a>, I pretty much failed continuing <a href="https://twitter.com/hashtag/adventofcode?src=hash&amp;ref_src=twsrc%5Etfw">#adventofcode</a> as it was too time demanding.<br><br>This advent calendar though looks like something I could actually finish 🎄 <a href="https://twitter.com/hashtag/functionalprogramming?src=hash&amp;ref_src=twsrc%5Etfw">#functionalprogramming</a> <a href="https://twitter.com/hashtag/fp?src=hash&amp;ref_src=twsrc%5Etfw">#fp</a><br><br><a href="https://functional.christmas">functional.christmas</a></p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/status/1204321603850366976?ref_src=twsrc%5Etfw">December 10, 2019</a></blockquote>

Although I didn't continue with it, Advent of Code definitely gets credit for helping me to start writing my first Haskell programs. The first puzzles were exactly the sort of tasks I was able to solve with my very basic knowledge of the language.

## First real-world project

I wasn't sure Haskell is going to be something I'll be doing from now on, but I didn't want to stop learning it until I build a real-world project. At least a small one, to really see how the language feels in practice.

A few months ago my friend [Ivan Kvasnica](https://twitter.com/ikvasnica), who's proficient mainly with PHP, wanted to try out a new language. Python, or perhaps server-side JavaScript. I recommended him to learn syntax at [Learn X in Y minutes](https://learnxinyminutes.com/) and to build a small project, as I think it's the most efficient way of learning (see the [theory behind it](https://en.wikipedia.org/wiki/Project-based_learning)). In the end, Ivan implemented one of my silly ideas, and wrote a [Bude Hezky? bot](https://github.com/ikvasnica/bude-hezky) in Python. It's a bot which checks weather and messages me 7pm every day if I should go cycling tomorrow.

I'm so good in advising others! Well I wonder why I didn't start with Haskell at [Learn Haskell in Y minutes](https://learnxinyminutes.com/docs/haskell/)?

Anyway, I was looking for a small project idea. Some of my friends often forget when exactly the [Prague Python meetup](https://pyvo.cz/en/praha-pyvo/) takes place (even though it's regularly on the third Wednesday of each month), so I decided to test my Haskell skills on a bot which would send out meetup reminders.

The advantage of a project like this is that it's a small CLI app, and you don't need a sophisticated runtime to deploy it. [CircleCI](https://circleci.com/) or [GitHub Actions](https://github.com/features/actions) allow you to run code in basically any language, and they both support running your code on a schedule. So all you need to do is to put your code inside a GitHub repo and configure how, and how often your app should be executed. CircleCI has a [ready-made tutorial on how to set up a Haskell project](https://circleci.com/docs/2.0/language-haskell/), so it's easy to get started even with a language you don't know very well yet.

Despite having the tutorial, I spent most of the time on understanding how to have a working project with [Stack](https://docs.haskellstack.org/). The tool is one of the most documented things I've encountered in Haskell ecosystem, and still, even after a lot of reading, I wasn't quite sure how it all works, and how to properly work with dependencies. Learning the packaging took away my excitement and I caught myself procrastinating the project. To be honest, I'd say learning Python packaging probably causes the same to people. Taking my hat off to [npm](https://www.npmjs.com/), which has an amazing developer experience, especially from the beginner's point of view.

[I tell beginners to look for inspiration in Open Source](https://junior.guru/practice/#opensource), and that's also what I tried when setting up my project. Unfortunately, as Haskell isn't very popular language, there is just about two real-world projects on GitHub: [Pandoc](https://github.com/jgm/pandoc) and [Semantic](https://github.com/github/semantic). Perhaps I'm bad in searching GitHub, but I really couldn't find much else. I don't know where code of all the packages at [Hackage](https://hackage.haskell.org/) is hosted.

In the end, I got the best advice from the [Alexis King](https://twitter.com/lexi_lambda)'s blog. There are [several articles tagged Haskell](https://lexi-lambda.github.io/tags/haskell.html), but I'd definitely point out [An opinionated guide to Haskell in 2018](https://lexi-lambda.github.io/blog/2018/02/10/an-opinionated-guide-to-haskell-in-2018/) and [Four months with Haskell](https://lexi-lambda.github.io/blog/2016/06/12/four-months-with-haskell/). Later on when I was done with the app setup and I worked on processing dates & time, [A Haskell Time Library Tutorial](https://two-wrongs.com/haskell-time-library-tutorial) by Christoffer Stjernlöf served me as a great resource.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">After failing to follow the <a href="https://twitter.com/hashtag/adventofcode?src=hash&amp;ref_src=twsrc%5Etfw">#adventofcode</a> I thought about making a small, real-world project in <a href="https://twitter.com/hashtag/Haskell?src=hash&amp;ref_src=twsrc%5Etfw">#Haskell</a> to test my skills. Here it's 😤 <br><br><a href="https://github.com/honzajavorek/pyvo_bot">https://github.com/honzajavorek/pyvo_bot</a></p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/status/1208776915445792773?ref_src=twsrc%5Etfw">December 22, 2019</a></blockquote>

[It's done](https://github.com/honzajavorek/pyvobot) and [it's working](https://circleci.com/gh/honzajavorek/pyvo_bot/tree/master), so if you use [Telegram](https://telegram.org/) and you want to know that the next Prague Python meetup is about to be soon, subscribe to the [https://t.me/pyvopraha](https://t.me/pyvopraha) Telegram channel.

## How does Haskell feel?

Powerful! It takes just a few lines to implement your own clone of [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)):

```haskell
import Control.Monad

main = do
    line <- getLine
    when (line /= ":wq") $ main
```

<small markdown="1">
    To run this on macOS, first run `brew install ghc` to install Haskell. Save the code as `vim.hs`, then execute `runhaskell vim.hs`. Done! You can type characters and finish each line with the return key. The program will keep confusing you until you [exit](https://github.com/hakluke/how-to-exit-vim/blob/master/README.md) by typing `:wq`.
</small>

### Latin

Okay, now seriously. Learning Haskell feels like if I was a Chinese and I decided to learn Latin. It's not very practical, but it gets me a strong foundation for learning almost any contemporary European language, and it gives me an intro to the cultural background. I'd say Haskell and Lisp are like Latin and Greek of functional programming. Many other functional languages adopt Haskell's theory, naming, syntax, type declarations, etc. At the LambdUp conference it felt like if an F# person wants to talk to a Closure person, they talk in Haskell. When I went through [this issue](https://functional.christmas/2019/4) of [functional.christmas](https://functional.christmas/), I was surprised that the Elm code examples were almost valid Haskell.

### Math

If SQL or Python read like an English sentence, then Haskell reads like math. Feels like math. It _is_ math. It's like if someone copied a page of your university math course workbook using only ASCII letters, and saved it as `.hs`. The `/=` operator is much closer to ≠ than `!=`, which can be found in other languages. Naming functions `foo'` is completely normal in Haskell, even inside the standard library. You know what I mean. Basically, you see the code and automatically your head reads it with your math professor's voice:

> `parseDay line` equals `fromGregorianValid y m d`, where `y` equals…, `m` equals…, and `d` equals…

This can be a bit challenging for people who have always been bad at math, like me.

### Types

One thing, which is very different from what I know, is types. It's a long time since I've been doing anything in C, C++, or Java. Most of my career I'm writing PHP, Python, or JavaScript. Haskell is a strongly typed language, and designing a program in such environment can get very different from what I'm used to do in Python. I didn't really play with TypeScript much and I'm yet to try out [Python's type annotations](https://realpython.com/python-type-checking/). In Haskell, types are everything. Read the [Parse, don’t validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) article by Alexis King and you'll get what I mean. So far I'm a noob around this. I need more practice to learn how to use types as a powerful, active element of my program, not just as something I'm trying to get somehow right so my code compiles.

### Motto

The same way Python has its [Zen](https://www.python.org/dev/peps/pep-0020/), Haskell seems to have the following motto:

> Worst practices should be hard

I found a good explanation of the motto in an unsurprisingly titled article [Worst practices should be hard](http://www.haskellforall.com/2016/04/worst-practices-should-be-hard.html) by Gabriel Gonzalez. To me, it feels like a very powerful concept not only when designing a programming language, but when designing virtually anything.

## Downsides

Haskell definitely feels very powerful and elegant. There are some parts of it though which I found, ehm, suboptimal.

The `String` vs `Text` dichotomy is very annoying. It's very well described in the chapter **The String problem** of the [Four months with Haskell](https://lexi-lambda.github.io/blog/2016/06/12/four-months-with-haskell/), so go an read it.

The ecosystem feels like a mess. Cabal, Stack, packages, it all seems everything but straightforward. I couldn't get my head around how it works. Why Stack downloads half of the internet to my computer before installing any packages? Why it then refuses to install a package I found on [Hackage](https://hackage.haskell.org/)? Very early I got into some version mismatches or whatever it was, without any luck finding out what's the problem and what is the preferred way to solve it.

Which brings me to _no documentation_. And when I say no, I really mean none, nothing, nada. The most annoying downside! It seems Haskell people consider type declarations to be enough prose to be considered as documentation. That feels very, _very_ uninviting. I'm fine reading type declarations, but sometimes I just need more explanation, perhaps even a tutorial. Well, most of the packages I found had nothing but a heading in their README! Not even a single usage example. Apart from trying to stumble upon random blog articles on the internet, I was basically left with reading code, or with trial and error. Some people tell me Python docs aren't sufficient. Well, from now on I'll be sending them to check out Haskell. They'll return crying and begging for forgiveness!

Also, I'm super scared of the [lens](https://hackage.haskell.org/package/lens) library. It's implementing the [concept of lenses](https://www.linkedin.com/pulse/functional-lenses-javascript-vladim%C3%ADr-gorej/), which I'm okay with, but in a way that it seems like a separate language within Haskell. Luckily, I didn't need to use it much.

## Try Haskell

How can you start playing with Haskell? Installing Haskell on macOS is easy with [Homebrew](https://brew.sh/):

```
$ brew install ghc
```

Originally, I didn't know at all that Haskell can be also interpreted. You can run your first program in a similar manner as your first Python program:

```
$ runhaskell hello.hs
```

This helped me a lot in the beginning. Haskell also has a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), which you can run as follows:

```
$ ghci
```

If you only want to try Haskell without installing it, you can paste your code to [tryhaskell.org](http://tryhaskell.org/).

## Resources

If I was to continue with learning Haskell, I'd probably dive into the following:

- I'd try to finish [LYAH](http://learnyouahaskell.com/),
- I'd take a look at [RWH](http://book.realworldhaskell.org/read/) and [HLHT](http://www.happylearnhaskelltutorial.com/),
- I'd play around with the [Haskell Hero](https://haskellhero.grifart.cz/) (Czech),
- I'd go through [What I Wish I Knew When Learning Haskell](http://dev.stephendiehl.com/hask/),
- and I'd make [/r/haskell](https://www.reddit.com/r/haskell/) a central part of my life, as it seems to contain a lot of tips, answers, and good advice on books and projects. I'd proactively ask there about anything I'm confused about.

## What next?

Honestly, I don't know if I'll continue learning Haskell. I didn't have a clear goal when I started with it. I wanted to get know better something I thought is divine for many years. I expected a hardcore intro to functional programming. I don't think anymore that Haskell is divine, and I definitely got a good intro to FP. I think I could have spent more time on playing with Haskell's types and properly handling all corner/error cases.

Perhaps one day Haskell will compile to [WebAssembly](https://webassembly.org/) and that will make it more popular, but meanwhile, I think I'll take a look at something else. Elm? Closure?

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If you like Java, program in Java. If you like C#, program in C#. If you like Ruby, Swift, Dart, Elixr, Elm, C++, Python, or even C; by all means use those languages. <br><br>But whatever you do, learn Clojure, and learn it well.</p>&mdash; Uncle Bob Martin (@unclebobmartin) <a href="https://twitter.com/unclebobmartin/status/1214906676840669184?ref_src=twsrc%5Etfw">January 8, 2020</a></blockquote>

Perhaps courting Haskell won't work out in the end, but I'm pretty sure that I'm not about to stop courting functional programming any soon. Did you know there's a whole [page on functional programming in Python](https://docs.python.org/3/howto/functional.html) in its documentation? I didn't!
