---
layout: post
title: "How to make a self-driving car"
date: 2024-10-19
author: Andrei Radulescu-Banu
image: /assets/images/how-to-make-a-self-driving-car.png
categories: [ai, programming, tech, reviews]
description: "A hands-on engineer's take on self-driving car system design: lidar, ROS, perception, mapping, and cloud data infrastructure — with AI Camp 2024 slides."
---

*Notes on an a16z survey of self-driving cars, and slides from my AI Camp Jan 2024 Talk*

## The Self-Driving Landscape

[Fantastic survey of self driving](https://www.linkedin.com/feed/update/urn:li:activity:7237489267084550146/) – how does the stack look like? What is readily available off the shelf, and what is not – [from Erin Price-Wright](https://www.linkedin.com/feed/update/urn:li:activity:7237489267084550146/#). She talks of issues tackled in perception, localization & mapping, control, planning. Excellent stuff.

## Personal Experience with Lidar Systems

I recall dealing with drift in lidar point cloud detection while turning corners at speed due to rotation of laser. …And I recall the issues synchronizing multiple lidars to get a merged point cloud!

Lidar calibration – had to be done manually, because there was no ready product available for auto-calibration…

## ROS and System Integration Challenges

This was a time when I was using ROS, and I was integrating C++ and python ros nodes… Designing the ROS bag recording infrastructure… Integrating with simulation… Refactoring to simplify the coordinate frames… Dealing with latency and jitter through the ROS components…

A year into it, I moved into architecting the offline computer vision data infrastructure, which meant learning AWS, terraform, evaluating data lake vendors like Databricks and Snowflake…

## Building from Scratch

Those were heady days! But, it was a lot of work from scratch, building the on-board and cloud system architecture. A lot of it should have been available as a ready-made product, ready for integration – but was, actually, not readily available.

Or if a vendor had some ready-made components, they were pretty expensive for a scrappy startup.

I suppose the self-driving car industry, while bringing a great promise, is still too small for a solid middleware ecosystem to develop. It's a challenge, and therefore, also an opportunity…

## Industry Insights

Anyhow… I enjoyed [Erin Price-Wright](https://www.linkedin.com/feed/update/urn:li:activity:7237489267084550146/#) piece tremendously!

While at HackMIT '24, I also enjoyed sitting on the same hackathon panel with [Chris Urmson](https://www.linkedin.com/in/chris-urmson-5392273/), ex-lead at Waymo, and current cofounder/CEO of Aurora. He spoke to students about his career, a recording is available here. The hackers/students had very good questions for him… Some were working at interns at a couple other self driving car companies. But, they had run into very similar issues I was running into.

## My AI Camp Presentation

Back in January, I gave a talk on **How to Build a Self-Driving Car - A Look at Robotics System Design**. It goes into a lot of the same details in Erin's survey, but more from an implementation angle.

I am making the slides available for the first time: **[How to Build a Self-Driving Car Slides](https://docs.google.com/presentation/d/1zl9OxqveTH6ASSh2oFmGDQUA-CwMWr-D6tjHNFMAnvs/edit?slide=id.g1efc3f84a80_0_21#slide=id.g1efc3f84a80_0_21)**. Comments would be appreciated!

## Conclusion

Self driving cars are obviously a huge subject, and my presentation was through a particular viewpoint – that of a hands-on implementer of system design, both at the ROS level, and at data and ML infrastructure for the cloud.

Difficult though as it may be, it is also one of the most exciting things an engineer can do.
