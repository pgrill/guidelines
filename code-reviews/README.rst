Code reviews
------------

Introduction
============

A code review is the process of manually inspecting source code written by
another person. It allows us to find errors that might have been overlooked by
the original author, and it does so at an early stage. Code reviews are not
only for finding errors though; reading code written by someone else can
improve our own skills and knowledge.

Process
=======

As the developer
^^^^^^^^^^^^^^^^

We use Gitlab to manage our code reviews. Every time you push changes to your
branch Gitlab will allow you to open a code review to merge those changes onto
a branch of your choice (usually ``dev``, but it will depend on the project
you're working on). You get to choose the reviewer as well, typically your team
will instruct you on who to choose.

After the reviewer finishes, they will either merge your changes or add
comments (you will see these comments in Gitlab) to your code, probably
requesting to change/fix something. Some people prefer to simply talk to the
developer instead of adding comments, which is also fine. In the case you
receive feedback, you will need to make the necessary changes to your code and
push your branch again; Gitlab will automatically update the code review so the
reviewer sees the latest version of your code.

As the reviewer
^^^^^^^^^^^^^^^

When someone assigns you a code review, you will get a notification from Gitlab
by email. Simply visit the link in it and Gitlab will show you a page with a
diff between the two versions of each modified file. You are able to add
comments to individual lines of each file. If you do so, the author will update
their code and push their branch again, then you will see an updated view of
the merge request under the same url.

Tips
====

As the developer
^^^^^^^^^^^^^^^^
#. You are the first reviewer of your code: read all your changes thoroughly
   before submitting the code review.
#. Don't check only your code: also make sure your branch is correctly named
   (naming conventions will depend on the project) and that you're requesting
   to merge your changes onto the right branch.
#. Don't take things personally: the point of code reviews is to improve the
   resulting code. Don't take it personally if there are mistakes or errors to
   fix.

As the reviewer
^^^^^^^^^^^^^^^
#. Don't check only the code: also make sure the branch is correctly named
   (naming conventions will depend on the project) and that the author is
   requesting to merge their changes onto the right branch.
#. Be respectful: not all developers have the same expertise or learn at the
   same rate.
#. Base your comments: if you are requesting the author to change something, be
   sure that it actually needs changing. It's better if you can reference
   coding standards or good practices.