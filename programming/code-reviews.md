# Code reviews

## Introduction

A code review is the process of manually inspecting source code written
by another person. It allows us to find errors that might have been
overlooked by the original author, and it does so at an early stage.
Code reviews are not only for finding errors though; reading code
written by someone else can improve our own skills and knowledge.

## Process

### As the developer[^1]

We use [Gitlab](https://git.sophilabs.io/) or
[Github](https://github.com/sophilabs) to manage our code reviews. We'll
be referring to Gitlab from now on since it's what you'll be using most
of the time, but they're fairly similar.

Every time you push changes to your branch Gitlab will allow you to open
a code review to merge those changes onto a branch of your choice
(usually `dev`, but it will depend on the project you're working on).
You get to choose the reviewer as well, typically your team will
instruct you on who to choose.

After the reviewer finishes, they will either merge your changes or add
comments (you will see these comments in Gitlab) to your code, probably
requesting to change/fix something. Some people prefer to simply talk to
the developer instead of adding comments, which is also fine. In the
case you receive feedback, you will need to make the necessary changes
to your code and push your branch again; Gitlab will automatically
update the code review so the reviewer sees the latest version of your
code.

### Tips

1. Don't check only your code: also make sure your branch is correctly
   named (naming conventions will depend on the project) and that
   you're requesting to merge your changes onto the right branch.
2. Avoid sending too many changes in one merge review as it get's
   easier for the reviewer to overlook errors if there is too much code
   to review. The ideal amount of code will depend on the language, but
   try to stay under 300 lines overall.
3. The primary reviewer is the author i.e. YOU.
4. Create a checklist for yourself of the things that the code reviews
   tend to focus on. Some of this checklist should be easy to put
   together. It should follow the outline of the coding standards
   document. Because it’s your checklist, you can focus on the thing
   that you struggle with and skip the things that you rarely, if ever,
   have a problem with. Run through your code with the checklist and
   fix whatever you find. Not only will you reduce the number of things
   that the team finds, you’ll reduce the time to complete the code
   review meeting—and everyone will be happy to spend less time in the
   review.
5. You are not your code. Remember that the entire point of a review is
   to find problems, and problems will be found. Don’t take it
   personally when one is uncovered.
6. Understand and accept that you will make mistakes. The point is to
   find them early, before they make it into production. Fortunately,
   except for the few of us developing rocket guidance software at JPL,
   mistakes are rarely fatal in our industry, so we can, and should,
   learn, laugh, and move on.
7. No matter how much “karate” you know, someone else will always know
   more. Such an individual can teach you some new moves if you ask.
   Seek and accept input from others, especially when you think it’s
   not needed.
8. Don’t rewrite code without consultation. There’s a fine line between
   “fixing code” and “rewriting code.” Know the difference, and pursue
   stylistic changes within the framework of a code review, not as a
   lone enforcer.
9. The only constant in the world is change. Be open to it and accept
   it with a smile. Look at each change to your requirements, platform,
   or tool as a new challenge, not as some serious inconvenience to be
   fought.
10. Fight for what you believe, but gracefully accept defeat. Understand
    that sometimes your ideas will be overruled. Even if you do turn out
    to be right, don’t take revenge or say, “I told you so” more than a
    few times at most, and don’t make your dearly departed idea a martyr
    or rallying cry.
11. Don’t be “the guy in the room.” Don’t be the guy coding in the dark
    office emerging only to buy cola. The guy in the room is out of
    touch, out of sight, and out of control and has no place in an open,
    collaborative environment.
12. Please note that Review meetings are NOT problem solving meetings.
13. Help to maintain the coding standards. Offer to add to the coding
    standards for things discussed that aren’t in the coding standards.
    One of the challenges that a developer has in an organization with
    combative code review practices is that they frequently don’t know
    where the next problem will come from. If you document each issue
    into the coding standards, you can check for it with your checklist
    the next time you come up for code reviews. It also will help cement
    the concept into your mind so that you’re less likely to miss
    opportunities to use the feedback.

### As the reviewer

When someone assigns you a code review, you will get a notification from
Gitlab by email. Simply visit the link in it and Gitlab will show you a
page with a diff between the two versions of each modified file. You are
able to add comments to individual lines of each file. If you do so, the
author will update their code and push their branch again, then you will
see an updated view of the merge request under the same url.

**Tips**[^2]

1. Don't check only the code: also make sure the branch is correctly
   named (naming conventions will depend on the project) and that the
   author is requesting to merge their changes onto the right branch.
2. Critique code instead of people – be kind to the coder, not to the
   code. As much as possible, make all of your comments positive and
   oriented to improving the code. Relate comments to local standards,
   program specs, increased performance, etc.
3. Treat people who know less than you with respect, deference, and
   patience. Nontechnical people who deal with developers on a regular
   basis almost universally hold the opinion that we are prima donnas
   at best and crybabies at worst. Don’t reinforce this stereotype with
   anger and impatience.
4. The only true authority stems from knowledge, not from position.
   Knowledge engenders authority, and authority engenders respect – so
   if you want respect in an egoless environment, cultivate knowledge.
5. Please note that Review meetings are NOT problem solving meetings.
6. Ask questions rather than make statements. A statement is
   accusatory. “You didn’t follow the standard here” is an
   attack—whether intentional or not. The question, “What was the
   reasoning behind the approached you used?” is seeking more
   information. Obviously, that question can’t be said with a sarcastic
   or condescending tone; but, done correctly, it can often open the
   developer up to stating their thinking and then asking if there was
   a better way.
7. Avoid the “Why” questions. Although extremely difficult at times,
   avoiding the”Why” questions can substantially improve the mood. Just
   as a statement is accusatory—so is a why question. Most “Why”
   questions can be reworded to a question that doesn’t include the
   word “Why” and the results can be dramatic. For example, “Why didn’t
   you follow the standards here…” versus “What was the reasoning
   behind the deviation from the standards here…”
8. Remember to praise. The purposes of code reviews are not focused at
   telling developers how they can improve, and not necessarily that
   they did a good job. Human nature is such that we want and need to
   be acknowledged for our successes, not just shown our faults.
   Because development is necessarily a creative work that developers
   pour their soul into, it often can be close to their hearts. This
   makes the need for praise even more critical.
9. Make sure you have good coding standards to reference. Code reviews
   find their foundation in the coding standards of the organization.
   Coding standards are supposed to be the shared agreement that the
   developers have with one another to produce quality, maintainable
   code. If you’re discussing an item that isn’t in your coding
   standards, you have some work to do to get the item in the coding
   standards. You should regularly ask yourself whether the item being
   discussed is in your coding standards.
10. Remember that there is often more than one way to approach a
    solution. Although the developer might have coded something
    differently from how you would have, it isn’t necessarily wrong. The
    goal is quality, maintainable code. If it meets those goals and
    follows the coding standards, that’s all you can ask for.
11. You shouldn’t rush through a code review - but also, you need to do
    it promptly. Your coworkers are waiting for you.
12. Review fewer than 200-400 lines of code at a time.

## References

[^1]: <https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/>

[^2]: <https://www.codeproject.com/Articles/524235/Codeplusreviewplusguidelines>
