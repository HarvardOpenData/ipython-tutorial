# HODP's iPython and Jupyter tutorial

## What is this?

iPython and Jupyter are important tools for data scientists like us. They let you experiment with code and play around with data extremely quickly - far faster than trying to write and run files. You can think of them as a much more powerful version of a command line or REPL, if you're familiar with that. It's also very similar to Mathematica.

Jupyter is an app that runs iPython, which is an interactive version of regular old Python. For the purposes of this tutorial, we'll say *iPython* because it's better-known than Jupyter. For most uses, the terms are interchangeable.

## Learning Python

Python is one of the premier languages for data science and extremely useful for other tasks like web development.

We'll be using Python in this tutorial, so if you aren't familiar, [use this tutorial!](https://www.learnpython.org/)

## Getting started

If you're using a Mac, get [Homebrew](https://brew.sh/). Fire up your terminal (also known as a *command line* or *command prompt*) and run the following command to install iPython:

```
brew install python
```
Now, install pip:
```
sudo easy_install pip
```

Once you have Python, run:

```
python2 -m pip install --upgrade pip
python2 -m pip install jupyter
```

(From https://jupyter.org/install)

Don't use `python` for this on Macs - that's the crappy pre-installed version of Python that comes with macOS. Instead, use `python2`, which was installed by Homebrew.

Still have problems? Call us over.

## Your first notebook

To get your first taste of iPython, clone this repository onto your computer.

Then run:

```
jupyter notebook
```

In your terminal.

![Screenshot of your terminal running `jupyter notebook`](img/terminal-screenshot.png)

You'll see a web browser window open with a list of your files. Open up `Bootcamp.ipynb` and follow along.

## Other useful stuff

* If you'll be installing packages, be sure you make a virtual environment first. [Here's how to do that.](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
* We recommend installing a few other packages, which will probably come in hands. Run `pip2 install pandas` and `pip2 install numpy` to get 2 useful packages.
