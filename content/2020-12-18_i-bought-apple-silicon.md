Title: I bought Apple Silicon
Image: images/apple-silicon.jpg
Lang: en
Tags: highlight
HackerNews-Comments: https://news.ycombinator.com/item?id=25472370
Twitter-Comments: https://twitter.com/honzajavorek/status/1340068645708439553
Reddit-Comments: https://www.reddit.com/r/apple/comments/kfx1yz/i_bought_apple_silicon/
Facebook-Comments: https://www.facebook.com/honzajavorek/posts/10158666148237707


I bought the new M1 Apple Silicon MacBook Air, and this is an article about why I did it, what was my decision process, what are my first impressions, and how I've approached the initial setup. The artcile is just a quick brain dump for the purposes of sharing my experiences with my friends and other readers of my blog, so don't expect any benchmarks or anything like that, this is not a serious review.

![Apple Silicon]({static}/images/apple-silicon.jpg)
Photo by me

## Why I bought new computer

My computer's display started slowly dying this year, suffering from gradually more and more serious [ghosting](https://www.youtube.com/watch?v=sbR2VhHLuW0). By November it was so bad that I could barely read any letters after an hour or two of using the machine. It's MacBook 12" early 2015, which I bought a few years ago, second hand, refurbished.

As far as I know, _refurbished_ should mean that the computer was used as a sample machine somewhere, e.g. in an Apple Store. When they didn't need it anymore, it got checked for defects and sold for a cheaper price as a second hand product in a very good shape. My theory is that the computer was almost unused by the time I've bought it, but perhaps it was open with the display shining all the time in the shop, so durability of the pixels suffered a lot.

Anyway, in addition to that, the machine's performance is a total potato these days. I have always appreciated its portability (size and weight of a magazine) and silence (has no fan), but I've spent most of this year at home, so I didn't care about portability, and the world got more bloated, so the minimum requirements for a smooth user experience are higher than in 2015. So by the summer 2020 I found myself wishing a new machine, and it just happened that Apple was about to release something with the new processors. I decided to wait, because I thought that (at the time) the latest machines would get cheaper if Apple releases something new.

## How I decided to buy Apple Silicon

When the first reviews were out, I waited for some more, but then it was just obvious this is a big change, a revolutionary machine, which is going to destroy the consumer market. I've enjoyed the following:

- [Apple Silicon M1: Black. Magic. Fuckery.](https://singhkays.com/blog/apple-silicon-m1-black-magic/) - compilation of various first impressions
- [Yeah, Apple’s M1 MacBook Pro is powerful, but it’s the battery life that will blow you away](https://techcrunch.com/2020/11/17/yeah-apples-m1-macbook-pro-is-powerful-but-its-the-battery-life-that-will-blow-you-away/) - general review
- [Why Is Apple’s M1 Chip So Fast?](https://debugger.medium.com/why-is-apples-m1-chip-so-fast-3262b158cba2) - how they made it and why competition won't be able to compete
- [Intel’s Disruption is Now Complete](https://jamesallworth.medium.com/intels-disruption-is-now-complete-d4fa771f0f2c) - how Intel failed the same way it won in the beginning

After that, I decided I'll buy the new Apple Silicon M1 MacBook Air, because it doesn't make sense to go for anything older if I plan to have the new computer for as many years as possible going forward. It's not _cheap_ cheap, but it's still huge performance for a reasonable price. Honestly, I'm surprised I happen to be buying a freshly released Mac announced just a few weeks ago, when so far I've been buying only second-hand Apple hardware, but it just felt like it makes sense to do this, all things considered.

I decided I don't need more RAM than 8 GB, because nobody from the first reviewers managed to give the RAM a hard time. It seemed to me it's a different beast altogether and it doesn't make sense to just compare numbers and say that more is better. Apple allows you to buy a computer with more than 8 GB RAM, but I think it's just a trap how to satisfy and charge those who don't believe the reviews and just want more RAM whatever it takes.

I also decided I want 512 GB drive, as I'm used to that size and I didn't want to downgrade. Also, I had serious capacity problems with my 16 GB iPhone SE and my wife still has serious capacity problems with her 128 GB old Air, so I really wanted to avoid that in the future.

I decided I don't mind that Docker or any kind of virtualization isn't supported (yet), because I don't use it. I'm self-employed solo enterpreneur now and Docker or Kubernetes play no role in my dev stack, also I use no virtual machines, nothing like that. If I was about to get a regular job somewhere, I assume they'd provide me a dedicated work computer. Also, I think [it's gonna be resolved soon](https://www.docker.com/blog/download-and-try-the-tech-preview-of-docker-desktop-for-m1/).

## First impressions

The new Air arrived this Tuesday, so as of writing this article, I work on it for 4 days. To be honest, upgrading from a years old machine with a dying display and a potato performance, to this shiny new beast, is… It's unbelievable.

The change in responsivity is really significant and I totally love it. I don't think I've ever used anything faster. With my potato machine I got used to going to bloated websites from my phone, as it felt that iPhone X can deal with them much better, but now the phone feels slow. [The optimized apps](https://isapplesiliconready.com/) are super snappy. Safari runs smooth and fast like crazy. Firefox the same. Spotify, Slack, Discord, Facebook, Twitter, LinkedIn, all the annoying bloated websites, which I used to hate so much for the past months, now run like if they were the most optimized websites on the internet. Honestly, I have problems to grasp the speed by my brain. It's just too much of a difference compared to my previous experience. It's like riding on a sloth and then suddenly switching to a super sonic rocket. I feel like I click on a tab in my browser and it happens instantly, and then it takes billion milliseconds until my brain realizes the action has been already performed and I can proceed to whatever else I wanted to do. I can now actually say when something needs network, because everything else is super fast. Whenever there's the slightiest lag, it's because network is involved, and because my network is slow.

I wanted to go with clean installation, so I didn't do any kind of smart restore from backup or anything like that. Just setting up the new system and moving my files, installing a few programs, like in the old days. Thanks to fast USBs and SSDs on both the computers and my external drive, moving the data was very fast, took just a few minutes.

I didn't upgrade to Catalina with my old laptop, because I wanted to play my 32bit Steam games, so macOS Big Sur is a quite a change for me now. A lot of setting up in the beginning, but all quite straightforward. A few surprises, such as zsh being the default shell in macOS now (change by `chsh -s /bin/bash`). Finally I can set Finder to sort by name AND have folders at the top, at the same time. For me as a person who switched to macOS from other systems, it has always felt so silly that this wasn't possible.

### TouchID

Having TouchID as part of the computer is a nice surprise. As a person who has sweaty hands all the time, I didn't believe it's gonna work. But it's actually able to read my fingers without any problems. The iPhone SE couldn't deal with my fingers. It was a source of a lot of frustrations and one of a few major reasons why I switched to iPhone X in Feb 2020, which has FaceID (only if the pandemics didn't bring face masks right after that).

It's very comfortable to use TouchID to login to the operating system, to 1Password, or to confirm a purchase in App Store (although that had to be first set up somewhere deep in the System Preferences, bah). Opening 1Password with a single finger touch is definitely a major productivity win for me.

### Battery

On Wednesday I tested the battery. 9am I unplugged the computer from electricity with 100% battery, and it started complaning about power only around 10pm. That's 13 hours. That said, during that day, I did mostly internet stuff, perhaps played some music, had 1 hour long call over MS Teams, 1 hour long call over Google Meet, and from 7pm to 10pm I attended an online meetup over Zoom. Before I connected to the meetup at 7pm, it still had almost 30 % battery left. Of course, no fan sound, as the machine has no fan, and it was only lukewarm between the keyboard and the display, cold everywhere else. Amazing!

### Games

On Black Friday I bought [Divinity: Original Sin 2](https://store.steampowered.com/app/435150/Divinity_Original_Sin_2__Definitive_Edition/), but it would crash on my machine. On the Apple Silicon Air, even though I run the game through Rosetta 2, I've put all the sliders in the performance settings to the highest positions, and it runs so smooth that when moving the game camera I actually experience problems to get my head around so many details happening on my screen. It's beautiful. Of course, the machine makes no sound, as it has no fan.

There is a [list of games which are optimized](https://applesilicongames.com/), but I just installed Steam using Rosetta 2, downloaded the games I wanted through it, and didn't bother further.

## Setup

### Homebrew

Setting up and figuring up Homebrew was a major drag, especially because my connection isn't very fast and initializing Homebrew downloads a lot of stuff over git, so it's endless. Before I found out the ideal configuration, I had to do it several times. I don't like Apple Store very much, so I only use it for installing apps which are not available as Homebrew casks, e.g. [Lungo](https://sindresorhus.com/lungo). I install everything else using Homebrew.

Homebrew suggests using it through Rosetta 2 (translation layer), which is fine, but I wanted to be able to also install apps which are already native to Apple Silicon. People post [tutorials on how to have two Homebrew installations side by side](https://www.youtube.com/watch?v=nv2ylxro7rM), but it still took me some time to figure everyhting out. My setup after some trial and error:

- Don't bother installing CLI apps natively. [It's a mess now](https://github.com/Homebrew/brew/issues/7857) and you'll only run into issues. Unless you want to help the Homebrew team with debugging, of course.
- I ended up having the default Homebrew installed through Rosetta 2, and I install everything with it, both CLI and GUI apps,
- except GUI [apps which are already optimized for the new Macs](https://isapplesiliconready.com/), such as Firefox, Spotify, VS Code, etc.

I follow the common advice on how to install Rosetta 2 Homebrew and how to install the native one. I won't repeat the many already existing tutorials:

- [Install Homebrew Natively on an Apple Silicon M1 Mac](https://www.youtube.com/watch?v=nv2ylxro7rM) (see also comments)
- [Homebrew on Apple Silicon](https://soffes.blog/homebrew-on-apple-silicon)
- [Workarounds for ARM-based Apple-Silicon Mac](https://github.com/mikelxc/Workarounds-for-ARM-mac)

The specifics of my setup are that I have this in my `.bash_profile`:

```bash
export PATH="/usr/local/sbin:$PATH"  # Rosetta 2
#export PATH="/opt/homebrew/bin:$PATH"  # ARM (native)

brew-arm() {
  HOMEBREW_NO_ENV_FILTERING=1 /opt/homebrew/bin/brew $@
}

brew() {
  arch -x86_64 /usr/local/bin/brew $@
}
```

When I want to install an optimized GUI app, I can use `brew-arm install firefox`. For anything else, I use `brew`. The `HOMEBREW_NO_ENV_FILTERING=1` is needed because I had some issues with the native Homebrew finding Git in the path. Maybe it was because I messed up with my setup too much, but whatever the reason, this has helped. I don't install CLI apps with the native Homebrew, so I don't have it in the `$PATH`. I had issues with the binaries and various other things stepping on each other's toes.

I also have this handy bash function for upgrading stuff, which allows me not to forget about something. With this I only need to type `upgrade` to my terminal from time to time:

```bash
upgrade() {
  echo "[brew update, upgrade]" && \
  brew update && \
  brew upgrade && \
  echo "[brew-arm update, upgrade]" && \
  brew-arm update && \
  brew-arm upgrade
}
```

### VS Code

Visual Studio Code is now optimized for Apple Silicon, or at least I was able to install it by `brew-arm install visual-studio-code` and it works and it's snappy. I hated that app on my last laptop, it was very slow and bloated, and I've been considering switching to something else. Now I don't care enough to see whether it's actually optimized or not, it's faster than my brain and that's quite enough. Unlike the other GUI apps I have, this one I want to have accessible from the terminal. It has a simple solution though, I just needed to [follow the official tutorial](https://code.visualstudio.com/docs/setup/mac#_alternative-manual-instructions) and put this to my `.bash_profile`:

```bash
PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

### Python

With Homebrew over Rosetta 2, installing Python 3 works just fine. It might work natively too, but as I mentioned, I decided not to mess with that yet. I usually also have `pipenv` and `poetry` installed globally, and over past years, by various trials and errors, I ended up installing those two by:

```bash
$ pip3 install --user poetry pipenv
```

Then it's necessary to put this into my `.bash_profile`:

```bash
# pipenv, poetry
export PATH="$(python3 -m site --user-base)/bin:$PATH"
```

I upgrade those two regulary whenever I upgrade Homebrew, so I lied to you, my function for upgrading actually looks like this:

```bash
upgrade() {
  echo "[brew update, upgrade]" && \
  brew update && \
  brew upgrade && \
  echo "[brew-arm update, upgrade]" && \
  brew-arm update && \
  brew-arm upgrade && \
  echo "[pipenv, poetry]" && \
  pip3 install --user pipenv poetry --upgrade
}
```

I hate it when new Python version gets released, Homebrew automatically upgrades it, all my virtual environments with their symlinks get broken, and I have to re-create them one by one. I was lazy to solve that issue on my previous laptop, but with the new one I wanted to do it in a smarter way, managing Python installations by `pyenv`. However, I got errors. It seems `pyenv`, although installed with Rosetta 2, has issues to get Pythons to Apple Silicon. So I gave up on that for now and I'm going to do it the old way, using Homebrew-managed Python 3, and swearing every time it upgrades system-wide.

### Terminal

When I've been setting up Homebrew, I worked a lot with the built-in macOS terminal. It felt quite okay, and to be honest, I forgot the reasons why I've been using iTerm2. So I decided I'll give the built-in one a go and see whether it's sufficient for the stuff I do. So far it's okay.

## Would I recommend it?

Well, yeah, sure, I'd totally recommend it. The computer is like a MIRACLE, especially if you upgrade from a potato machine. If nothing holds you back, like the lack of virtualization support, go for it. I hope it's gonna be this snappy for at least five years going forward. Given the little chance Intel or anyone else is going to keep up with this new level of performance, I believe this new laptop could be with me perhaps even longer, unless everyone else in the world buys it and developers start to create 10x bloated apps compared to today.

Secretly, of course, I wish other manufacturers to be able to keep up with Apple, against all the odds. I wish they rolled their sleeves and came up with something awesome, too. Because the last thing anyone needs is another market where Apple has monopoly.

