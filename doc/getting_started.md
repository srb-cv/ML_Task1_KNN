# Getting Started

This document contains a few pointers on how to set up your system, so that you can start working on the project's tasks.

## Required Software

### Python

A working python installation of version 3.10 is required to solve the tasks, as you will be writing a lot of python code. Python should be installed by defaut on your terminals. You can follow the instructions below to setup your system by creating a virual environment using the [venv](https://docs.python.org/3.10/library/venv.html) module.


1. Create a new virtual environment for the ML task:

   ```shell
   $ python3 -m venv ML_task
   ```

2. Activate the new environment:

   ```shell
   $ source ML_task/bin/activate
   ```

3. Install any required packages. For the first task those are [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pytorch](https://pytorch.org/). The first two can be installed by the command

   ```shell
   (ML_task) $ pip3 install numpy matplotlib
   ```
You will also need to install (PyTorch)[https://pytorch.org/get-started/locally/] to download the datasets through the provided repository. However, you do not need to know or learn about this library unless you are working on a task involving neural networks:
   
   ```shell
   (ML_task) $ pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   ```

The packages you just installed will only be available if you use the interpreter of the `ML_task` environment. To run your python scripts with that interpreter instead of the system-wide interpreter, activate the `ML_task` environment before you run any python scripts in a new terminal window:
```shell
$ source activate venv/bin/activate
(ML_task) $ python your_script.py
```

<!-- ### Git
You will need to install the [Git](https://git-scm.com/) version control software on your system to check out your project repository. On a Debian-based system you can install it via
```shell
$ sudo apt install git
```
and for a Windows system, you can download the installer [here](https://git-scm.com/download/win). -->

### Submission
If you wish you can submit a report of your obtained results as document via email  to varshneya@cs.uni-kl.de

<!-- #### ShareLaTeX
You don't need to install any software on your PC to use LaTeX, since the SCI has set up a ShareLaTeX instance that you can use through your browser. Another advantage of this is that you can collaborate with your teammates in real time, much like it works in Google Docs, for example. However, you first need to create an account specifically for the ShareLaTeX instance:
1. Visit the [SCI Website](https://accounts.cs.uni-kl.de/sciuser) and log in with your SCI credentials.
2. Click on `SCI-Latex Account` and then `Create`.
3. Click on `Set a new password`, enter a password of your choice and click `Activate`.
4. You can now create a new project, invite your temamates and start writing your reports by accessing the [SCI ShareLateX Website](https://sci-latex.informatik.uni-kl.de/) using your newly created account. -->

<!-- #### Local Installation
On a Debian-based system, you can usually install the TeXLive distro directly from the OS's repos:
```shell
$ sudo apt install texlive texlive-latex-extra texlive-science
```
For Windows systems, [MikTeX](https://miktex.org/download) is a good alternative.

Technically speaking, you could start editing LaTeX documents with a simple text editor and use the CLI to compile them, but in pratice it is often more convenient to use an editor that is specifically made for working with LaTeX files. [TeXstudio](https://www.texstudio.org/) is a relatively lightweight, cross-platform editor with decent functionality. Again, it should be available from your distro's repos so that you can install it by running

```shell
$ sudo apt install texstudio
```

or you'll have to download the installer for Windows. -->

## Required Knowledge
### Python
We expect you to have a decent grasp on basic Python concepts (Objects, collections, functions, etc.), since all of the exercises should be implemented in Python. However, even if you have never used Python before, it should still be possible to solve the exercises, since Python is designed to be easy to use and easy to learn. Obviously, you'll need to invest more time to learn the basics; the [Google Python Tutorial](https://developers.google.com/edu/python/) is a good place to start.

### Git
We assume that you have used Git before and that you can clone your repo, know how to commit and collaborate with your fellow group members. If you have not used git before or if you are not sure how to use git correctly, have a look at the [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials).

<!-- ### LaTeX
You should be familiar enough with LaTeX to produce decent-looking reports. If you are unsure about that, have a look at the report template in your git repo (also avilable on [sharelatex](https://sci-latex.informatik.uni-kl.de/read/sfsvfdsyxrwp)). Note that you don't need to use the template to write your report, but it is certainly not the worst idea.

In case you need to refresh or build your skills in LaTeX, refer to the extensive collection of [Overleaf Tutorials](https://www.overleaf.com/learn/latex/Tutorials), which also explain how to use the ShareLaTeX instance. -->

### Machine Learning
We do not expect you to have any prior knowledge in machine learning. However, it might be useful to familiarise yourselves with both [Numpy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/), the Python libraries for numerical computation and plotting, respectively.

## Setting up your Repository
First of all, you'll need to clone your repository to your local machine. We recommend to fork the GitHub repository to your GitHub account and then clone the forked repository to your local computer.
```shell
$ git clone https://github.com/[GITHUB_USERNAME]/ML_Task1_KNN.git
```
Now you can make changes to your local copy, commit them, pull and push as usual.

### Updating your Repository

Whenever there are changes to the template repository, you can pull them to your local copy by executing the following commands:

```shell
$ git checkout master
$ git fetch
$ git pull
```

Make sure to commit or stash any pending local changes before you execute those commands.
You can then push the merged changes to your group's remote repository:

```shell
$ git push origin master
```

