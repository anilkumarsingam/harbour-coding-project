# Harbor Take Home Project

Welcome to the Harbor take home project. We hope this is a good opportunity for you to showcase your skills.

## The Challenge

Build us a REST API for calendly. Remember to support

- Setting own availability schedules
- Showing own availability schedules
- Finding overlap in schedule between 2 users

It is up to you what else to support.

## Expectations

We care about

- Have you thought through what a good MVP looks like? Does your API support that?
- What trade-offs are you making in your design?
- Working code - we should be able to pull and hit the code locally. Bonus points if deployed somewhere.
- Any good engineer will make hacks when necessary - what are your hacks and why?

We don't care about

- Authentication
- UI
- Perfection - good and working quickly is better

It is up to you how much time you want to spend on this project. There are likely diminishing returns as the time spent goes up.

## Submission

Please fork this repository and reach out to Prakash when finished.

## Next Steps

After submission, we will conduct a 30 to 60 minute code review in person. We will ask you about your thinking and design choices.


## How to run??
- Make sure you have installed `docker` and `docker-compose`
- Run `docker-compose up -d`
- Head over to http://localhost:8080/api/v1/schedules/docs for schedules service docs
  and http://localhost:8080/api/v1/user/docs for user service docs

## Also deployed on an ec2 instance
- Head over to http://3.80.71.250:8080/api/v1/schedules/docs http://3.80.71.250:8080/api/v1/user/docs
