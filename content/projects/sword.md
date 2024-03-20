---
title: SWORDv3
tags:
  - sword
  - python
  - js
  - ruby
  - standards
  - apis
  - invenio
  - samvera
  - dspace
  - oai
template: project
logo: sword.png
challenge:
  text: Before SWORD there was no standardised way of depsositing individual digital objects in repositories; a machine-to-machine counterpart to the manual deposit forms of the early repositories.  The aim was to replace that, and to then support the ongoing integration between scholarly systems supporting this kind of point-to-point transfer.  The primary use case was CRIS systems, which were increasingly being used as front-ends to repository deposit.
  screenshot: "sword1.jpg"
solution:
  text: SWORDv1 supported a single package deposit in a "fire and forget" protocol.  Subsequently we developed more sophisticated RESTful interactions with repositories, supporting the full CRUD (Create, Retrieve, Update, Delete) lifecycle.  This enabled systems like CRIS to integrate, and allowed institutions to build embeddable deposit interfaces in, for example, departmental web pages.  The latest version of SWORD modernises the standard, moving it from XML to JSON, supporting operations for large file deposit, and removes aspects of the specification that were unwarranted in earlier versions.
  screenshot: "sword2.jpg"
success:
  text: SWORD is broadly supported in all the major open source repository platforms, and has been used extensively in custom integrations between machine users.  The latest version has been constructed with a view to support the latest use cases around research data, designed in collaboration with the community.
  screenshot: "sword3.jpg"
---

In 2011 Jisc in the UK identified the need for a repository deposit protocol, which came to be SWORD.  Soon after that more advanced deposit use cases became apparent, and Cottage Labs took over as technical lead for the specification and have driven it forward through 2 subsequent versions.