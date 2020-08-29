# CMPSC 100: Fall 2020, Week 00

[![Status](workflows/GatorGrader/badge.svg)](https://github.com/allegheny-college-sandbox/cmpsc-100-fall-2020-week-00-configuration/actions)

## Table of contents

* [Overview](#Overview)
* [Setup](#Setup)
  * [GitHub: Part 1](#GitHub-Part-1)
    * ["Cloning" a repository](#"Cloning"-a-repository)
* [Instructional materials](#instructional-materials)
  * [Media](#media)
  * [Worksheets and activities](#worksheets-and-activities)
  * [Lab](#lab)
* [Wrap-up](#wrap-up)
  * [GitHub: Part 2](#GitHub-Part-2)
    * ["Committing" a repository](#"Committing"-a-repository)

## Overview

This week, we explore setting up the tools, technologies, and platforms that will guide our work this semester. These include:

* The "terminal"
  * Why do we use a terminal?
  * Using our terminal
* GitHub
  * What is a "repository"?
  * "Cloning" a repository
  * "Committing" a repository
* JupyterLab
* Markdown
* GatorGrader

Follow the links below to access instructional materials for the week. Each `*.ipynb` file is a Jupyter notebook which contains discussion, instruction, and activities -- some meant for use during class video sessions, others to be complete on your own. Simply double-click on it in the file tree to the right to open it in a new tab.

### Before we start

This week features a lot more "fiddly" parts than many of our upcoming weeks. This may require a bit more patience on your part; these steps are very important to having a successful class.

Of course, as will always be true throughout the semester, I am committed to making sure that these steps go as smoothly as possible and, where they might not, I will gladly offer assistance.

I give you my final prefatory note about assistance: **please do not hesitate to ask for it**. As I write in the course [Syllabus](https://github.com/allegheny-college-cmpsc-100-fall-2020/course-materials#syllabus):

> [h]istorically, students who are successful in my courses visit and discuss course concepts with the instructor and Technical Leaders early and often.

## The "terminal"

> [f]rom the mid 1970's to the mid 1980's, most people used real text-terminals to communicate with large computers....They consisted only of a screen, keyboard, and only enough memory to store a screenfull or so of text (a few kilobytes). Users typed in programs, ran programs, wrote documents, issued printing commands, etc. A cable connected the terminal to the computer (often indirectly). It was called a terminal since it was located at the terminal end of this cable.

David S. Lawyer, [1.7 What is a Text-Terminal?](https://linux.die.net/HOWTO/Text-Terminal-HOWTO-1.html#ss1.7)

### What is a "terminal"?

The discussion above provides good history with an eye toward why we still use the word "terminal" to describe the interface we use to issue commands to a system. While we're not beholden to [room-sized computers anymore](https://en.wikipedia.org/wiki/UNIVAC), you're not exactly sitting in front of the server running any of the programs we use. Ergo, you need an interface that serves the same purpose as a historical "terminal": an "endpoint" used to issue different system or programming commands.

### Using our terminal

Whenever we're using JupyterLab, it's probably a good idea to have a terminal open, as we will see now and in the coming weeks.

There are two ways to launch a terminal in JupyterLab:

#### File menu

* From the `File` menu, select the `New` option
* In the resulting sub-menu, click `Terminal`

This will open a new tab for an active terminal.

#### Launcher tab

* Locate the `Launcher` tab at the top of this window
  * It's possible that you've closed your `Launcher` tab; in that case, you can either launch the terminal from the `File` menu, or create a new `Launcher` from the same place
* Under the `Other` heading, click the `Terminal` tile

This will open a new tab for an active terminal.

## GitHub

GitHub is the platform that we're going to use to distribute and store our code.

### "Repositories"

Simply put, a "repository" is a collection of files and folders from a "snapshot" taken at a given point in time. This text is contained in such a repository. What's even better: repositories "remember" previous versions of themselves. In fact, you can _always_ go back and get a previous "snapshot".

We use a program called `git` to take and manage different versions of our files. `git` is referred to as a `Version Control System (VCS)`. 

#### What is a "GitHub", then?

The quasi portmanteau "GitHub" is really what it says: a hub for `git` repositories. There are many other places on the internet that provide the service that GitHub does, but it's the largest such service out there.

(It has that sweet Microsoft money, now.)

### Securing your GitHub account

This may seem like an extra step -- and it is. But, it's an important one.

Now that you have some familiarity with a terminal, I'm going outsource explaining how to generate a key to, er..., myself.

[![]()]()

### "Cloning" a repository

In GitHub lingo, "cloning" a repository is the way that we, effectively, download the content. (As you've discovered, this paraphrase is pretty inaccurate, as "repositories" are much more than just downloads.)

To clone _this_ repository:

* Open a [terminal](#Using-our-terminal), and 

## Instructional materials

### Media

```
Media
```

### Worksheets and activities

* [Worksheet: The terminal](worksheets/1%20-%20CMPSC%20100%20-%20Week%2000%20-%20Worksheet%20-%20Terminal%20commands.ipynb)
* [Worksheet: Markdown](worksheets/2%20-%20CMPSC%20100%20-%20Week%2000%20-%20Worksheet%20-%20Markdown.ipynb)

### Lab

#### _The Maltese Python_

![It's just a MacGuffin!](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-maltese-python.png)

> My way of learning is to heave a wild and unpredictable monkey-wrench into the machinery.

Dashiell Hammet, _The Maltese Falcon_

In 2020 a professor attempted to boggle their students' minds by sending them a game in which they hid a Golden Python whose scales were conjured from digital text—an enterprising computer system seized this priceless token and the fate of the Maltese Python remains a mystery to this day...

It is hidden somewhere in the `/mansion`, but it is up to _you_ to find and `claim` it.

[Lab: _The Maltese Python_](lab/CMPSC%20100%20-%20Week%2000%20-%20Lab%20-%20The%20Maltese%20Python.ipynb)

## Wrap-up

### GitHub: Part 2

#### "Committing" a repository

#### A strong warning

<div class="alert alert-block alert-danger">
    <p><strong>While we may use this server to store code, <u>you</u> are responsible for using GitHub as your main backup.</strong></p>
    <p>While I back this server up on a regular basis, I cannot guarantee that I'll the ability to restory up-to-the-minute data for your work.</p>
    <p>Remember: to err is human; to back up your work is divine.</p>
</div>
