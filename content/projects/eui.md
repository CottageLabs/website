---
title: EUI Covid Data
name: EUI COVID Data Portal
tags:
  - python
  - invenio
  - dr
template: project
logo: eui.svg
externalurl: https://covid19data.eui.eu/
challenge:
  text: A metadata-only repository using brand new software, we customised a few components to better suit EUI's needs.
  screenshot: "eui1.png"
solution:
  text: A stripped-out version of InvenioRDM, deployed on a virtual machine hosted by us and themed, customised for EUI. The harvesters were re-written from R to Python, with great improvements to code reuse and a data pipeline to improve metadata quality.
  screenshot: "eui2.png"
success:
  text: We have great uptime and stability on our InvenioRDM instance, which has seen research use for a number of years. We've successfully migrated through various InvenioRDM versions to maintain support and gain features.
  screenshot: "eui3.png"
---

During the pandemic, the **European University Institute** reached out to us to build a digital repository for COVID-19 related research.  We customised and deployed an instance of CERN's InvenioRDM platform to support their metadata project. We subsequently re-implemented their metadata harvesters to further populate this repository.