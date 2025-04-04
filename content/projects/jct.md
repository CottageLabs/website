---
title: Journal Checker Tool
name: Journal Checker Tool
tags:
  - oai
  - search
  - api
  - python
  - js
template: project
externalurl: https://journalcheckertool.org/
logo: jct.svg
challenge:
  text: cOAlition S's Plan S requires funded authors to publish under certain conditions for their grant funding to be valid.  To enable authors to check that their preferred publishing route is compliant, or to support them in finding alternative routes, the coalition wanted a tool which would survey the known information about journals in multiple sources and deliver advice on the publishing options available.
  screenshot: "jct1.png"
solution:
  text: We developed several new data sources which we maintain (and especially for Transformative Agreements), and we built a comprehensive data gathering and caching system which pulls information from definitive scholarly information sources such as Crossref, DOAJ, ROR, and OA.Works.  Then in close collaboration with our colleagues at the coalition, we developed a layered query algorithm that allows us to answer compliance questions with nuanced responses, references to additional information, and detailed information about how the result was deteremined.  This system is then kept up-to-date with the current state of the data in those external systems, so the results are as timely and accurate as possible in the changing publishing landscape.
  screenshot: "jct2.png"
success:
  text: The Journal Checker Tool is widely used, and has visitors from all over the globe.  It has served over 1m compliance checks.  It has been customised to deliver funder-specific advice as new funders have joined the coalition, and has even driven publishers to be interested in how well represented their Open Access policies are.
  screenshot: "jct3.png"
---

cOAlition S, a consortium of 25+ funders, has put together an ambitious plan to improve the state of Open Access and
encourage more and more publishers to support that route. Cottage Labs provides several services to the consortium,
including **Journal Checker Tool** that allows authors to verify the compliance of their preferred publishing routes.