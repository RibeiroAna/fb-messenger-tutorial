# Create a serverless FAQ Messenger bot with Wit.ai
_Does your clients always message your Facebook page with the same kind of question? If so you should create a bot to answer them! Learn how!_


Table of contents:

1. [Overview](#Overview)
2. [Architecture](#Architecture)
3. Setting up your Wit.ai Application
4. Setting up your database
5. Creating AWS CloudFront
6. Setting up your Messenger application
7. Creating your AWS Lambda functions
8. Conclusion

## Overview

In this tutorial, I’ll teach you how to create a bot to answer Frequent Answered Questions (FAQ) on your Facebook page, so when users message you they can get an (almost) instant answer about the question s/he made.

To follow this tutorial, you will need the following:
1. A Facebook account and a Facebook page;
2. An AWS account (Free tier is Ok), no previous AWS knowledge is necessary;
3. Basic knowledge of programming (I’m going to use Python, but probably any programming language knowledge is fine, so you can understanding what I’m doing);

To host your bot and database, you’ll use Serverless technology to build this bot, this technology reduces the time you need to set up and manager your infrastructure, and it escales automatically to match your demand, it is great for applications such as a messenger bot.

For Natural Language Processing, you are going to use Wit.ai, which is a Facebook platform that does half of the work necessary for creating a bot.
