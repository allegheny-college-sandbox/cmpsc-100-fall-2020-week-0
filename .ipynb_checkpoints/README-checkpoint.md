# CMPSC 100: Fall 2020, Week 00

* Distributed: 31 August, 2020
* Due: 3 September, 2020

## Assignment status

[![Status](https://github.com/allegheny-college-sandbox/cmpsc-100-fall-2020-week-00-configuration/workflows/GatorGrader/badge.svg)](https://github.com/allegheny-college-sandbox/cmpsc-100-fall-2020-week-00-configuration/actions)

## Table of contents

---

For those who just want to get to work, consult the `Instructional Materials` section. However, for folks who want to walk through activites with explanations, some context or history, and general folderol/frivolity, start at [Setup](#Setup).

* [Overview](#Overview)
* [Instructional materials](#instructional-materials)
  * [Media](#media)
  * [Worksheets and activities](#worksheets-and-activities)
  * [Lab](#lab)
* [Setup](#Setup)
  * [The "terminal"](#The-"terminal")
    * [What is a "terminal"?](#What-is-a-"terminal"?)
    * [Using our terminal](#Using-our-terminal)
  * [GitHub: Part 0](#GitHub:-Part-1)
    * [Activity 0: Securing your GitHub account](#Activity-1:-Securing-your-GitHub-account)
    * ["Cloning" a repository](#"Cloning"-a-repository)
* [Wrap-up](#wrap-up)
  * [GatorGrader]
  * [GitHub: Part 1](#GitHub:-Part-2)
    * ["Committing" a repository](#"Committing"-a-repository)

## Overview

---

This week, we explore setting up the tools, technologies, and platforms that will guide our work this semester. These include:

* The "terminal"
* GitHub
  * "Cloning" a repository
  * "Committing" a repository
* JupyterLab
* Markdown
* GatorGrader

Follow the links below to access instructional materials for the week. Each `.ipynb` file is a `Jupyter notebook` (more on this later) which contains discussion, instruction, and activities -- some meant for use during class video sessions, others to be complete on your own. Simply double-click on it in the file tree to the right to open it in a new tab.

### Before we start

This week features a lot more "fiddly" parts than many of our upcoming weeks. This may require a bit more patience on your part; these steps are very important to having a successful class.

Of course, as will always be true throughout the semester, I am committed to making sure that these steps go as smoothly as possible and, where they might not, I will gladly offer assistance.

I give you my final prefatory note about assistance: **please do not hesitate to ask for it**. As I write in the course [Syllabus](https://github.com/allegheny-college-cmpsc-100-fall-2020/course-materials#syllabus):

> [h]istorically, students who are successful in my courses visit and discuss course concepts with the instructor and Technical Leaders early and often.

True, that.

## Instructional materials

---

### Media

Click the images below the headers to launch videos.

#### "Cloning" / "Committing" repositories

[Video]()


#### SSH keys

[![YouTube thumbnail](https://i3.ytimg.com/vi/qEPjUGQFmzQ/hqdefault.jpg)](https://www.youtube.com/watch?v=qEPjUGQFmzQ)

#### Terminal commands

[Video]()

#### Markdown

[![YouTube thumbnail](https://i3.ytimg.com/vi/s-oSuHFVnR4/hqdefault.jpg)](https://www.youtube.com/watch?v=s-oSuHFVnR4)

### Worksheets and activities

* [Week 00 - Worksheet 0 - Securing your GitHub account](worksheets/Week%2000%20-%20Worksheet%201%20-%20Securing%20your%20GitHub%20account.ipynb)
* [Week 00 - Worksheet 1 - "Cloning" a repository](worksheets/Week%2000%20-%20Worksheet%201%20-%20"Cloning"%20a%20repository.ipynb)
* [Week 00 - Worksheet 2 - Terminal commands](worksheets/Week%2000%20-%20Worksheet%202%20-%20Terminal%20commands.ipynb)


### Lab

#### _The Maltese Python_

![It's just a MacGuffin!](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-maltese-python.png)

> My way of learning is to heave a wild and unpredictable monkey-wrench into the machinery.
>
> Dashiell Hammett, _The Maltese Falcon_

In 2020 a professor attempted to boggle their students' minds by sending them a game in which they hid a Golden Python whose scales were conjured from digital text—an enterprising computer system seized this priceless token and the fate of the Maltese Python remains a mystery to this day...

It is hidden somewhere in the `/mansion`, but it is up to _you_ to find and `claim` it.

[Lab: _The Maltese Python_](lab/CMPSC%20100%20-%20Week%2000%20-%20Lab%20-%20The%20Maltese%20Python.ipynb)

## The "terminal"

---

> [f]rom the mid 1970's to the mid 1980's, most people used real text-terminals to communicate with large computers....They consisted only of a screen, keyboard, and only enough memory to store a screenfull or so of text (a few kilobytes). Users typed in programs, ran programs, wrote documents, issued printing commands, etc. A cable connected the terminal to the computer (often indirectly). It was called a terminal since it was located at the terminal end of this cable.
>
> David S. Lawyer, [1.7 What is a Text-Terminal?](https://linux.die.net/HOWTO/Text-Terminal-HOWTO-1.html#ss1.7)

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

<div class="alert alert-block alert-warning">
  It's possible that you've closed your <b>Launcher</b> tab. In that case:
    <ul>
        <li>you can either launch the terminal from the <b>File</b> menu</li> 
        <li>or create a new <b>Launcher</b> from the same place</li>
    </ul>
</div>

* Locate the `Launcher` tab at the top of this window
* Under the `Other` heading, click the `Terminal` tile

This will open a new tab for an active terminal.

## GitHub: Part 1

---

GitHub is the platform that we're going to use to distribute and store our code.

### "Repositories"

Simply put, a "repository" is a collection of files and folders from a "snapshot" taken at a given point in time. This text is contained in such a repository. What's even better: repositories "remember" previous versions of themselves. In fact, you can _always_ go back and get a previous "snapshot".

We use a program called `git` to take and manage different versions of our files. `git` is referred to as a `Version Control System (VCS)`.

#### What is a "GitHub", then?

The quasi portmanteau "GitHub" is really what it says: a hub for `git` repositories. There are many other places on the internet that provide the service that GitHub does, but it's the largest such service out there.

(It has that sweet Microsoft money now.)

One of GitHub's services is something called GitHub Classroom -- a tool that allows me to create assignments, give them to you, and enables you to create your own complete copy of them in a [repository](#"Repositories").

### Activity 0: Securing your GitHub account

* [Week 00 - Worksheet 0 - Securing your GitHub account](worksheets/Week%2000%20-%20Worksheet%201%20-%20Securing%20your%20GitHub%20account.ipynb)

### Activity 1: "Cloning" a repository

* [Week 00 - Worksheet 1 - "Cloning" a repository](worksheets/Week%2000%20-%20Worksheet%201%20-%20"Cloning"%20a%20repository.ipynb)

## Wrap-up

---

### GatorGrader

### GitHub: Part 1

#### Who are you?

GitHub will let you `clone` repositories without really knowing who you are. To assign your name to the work you've done, though, is a different story.

```
git config --global user.email "YOUR ALLEGHENY EMAIL"
```
```
git config --global user.name "YOUR NAME"
```

#### "Committing" a repository

#### A strong warning

<div class="alert alert-block alert-danger">
    <p><strong>While we may use this server to store code, <u>you</u> are responsible for using GitHub as your main backup.</strong></p>
    <p>While I back this server up on a regular basis, I cannot guarantee that I'll have the ability to restore up-to-the-minute data for your work.</p>
    <p>Remember: to err is human; to back up your work is divine.</p>
</div>