# Training Project

![Man holding a bazooka aiming a fly](https://d2wlcd8my7k9h4.cloudfront.net/static/figures/technology.jpg)

As an apprentice, after your self learning process you will be assigned to do a Ticket System Project to apply all your knowledge and to have another instance to learn, give and receive feedback from your Mentor. The actual specifications of the Ticket System are online at [Sophilabs' training](https://github.com/sophilabs/training).
Your mentor will give you the actual requirements for the projects and a deadline, which can be anywhere from one week up to two weeks. This project is a good opportunity to practice before a real client, handling deadlines, expectations, negotiating a real scope, and prioritizing.

## Requirements

![Ticket system screenshots](./tickets.png)

The ticket system requirements are described in the sophilabs [training](https://github.com/sophilabs/training) page.

## Activities

![Process](./process.png)

This section describes some activities you will do during your training project.

### Kickoff

Your mentor will meet with you to present the project, explain the scope, set the deadlines of the project. We will create a gitlab repository for the project to commit your code. Make sure you have access to the private company's [gitlab](https://git.sophilabs.io/). Please set up [gilp](https://sophilabs.co/blog/gulp-and-commit-hooks-gilp) commit hooks for Python, and Javascript languages to check your code complies to the [language guidelines](/programming/README.rst). You can download a sample gilp ready `gulpfile.js` [here](https://github.com/sophilabs/gilp/blob/master/examples/full.js) and adapt it to your needs.

### Feature work

After the kickoff meeting, you should be ready to work on the project. This is the perfect time to start practicing our development process, specifically you should follow a [git flow](http://nvie.com/posts/a-successful-git-branching-model/)  branching model development. In this project this means whenever you make a new feature you must create a feature branch for the work you are doing. Whenever you finish your work you should create a [Merge Request](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html) so every commit into the master branch is reviewed by a teammate first. In the training project your mentor will act as the reviewer following the [Code Review](https://sophilabs.co/playbook/#code-reviews) and give you feedback on your work.

### Demo

At the end of the project, we will ask you to  demo your Ticket system to your mentor. Think this like a product demo after the end of an SCRUM sprint where your mentor will act as a product owner. This [article](https://www.atlantbh.com/blog/4-steps-successful-product-demo/) shows some hints to make your demo as effective as possible.

## Tips

* *Prioritize*: Mandatory requirements vs Optional. Consider doing mandatory requirements first, and then focusing into the optional ones if you have time.
* *Organize*: your work using a Trello Board, this will prevent you on getting stuck and focusing in the important things.
* *Negociate* requirements. Any developer should negotiate if the scope is too big. Feel free to do so deadlines and requirements. Hitting deadlines are negotiating scope is common software projects with a fixed timeline.
* *Ask* around if you get stuck. In sophilabs we have several ways to get help if needed.
  * Use `/guru` slack command to find expert people in certain your question. Try it in any channel
    ![Animation showing how to type a /guru query](./guru.gif)
  * The appropriate Slack channels like [#developers](https://sophilabs.slack.com/messages/developers), [#python](https://sophilabs.slack.com/messages/python), or [#react](https://sophilabs.slack.com/messages/react).
  * Ask around! We are a friendly bunch and someone will surely know or at least point you towards the right direction.