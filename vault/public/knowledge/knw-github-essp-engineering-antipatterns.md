---
id: knw-github-essp-engineering-antipatterns
title: ESSP engineering antipatterns
status: draft
visibility: public
complexity: 3
references:
  - id: knw-github-essp-step-1-identify-barriers
    relation: example
  - id: knw-github-essp-zones-and-metrics
    relation: support
tags:
- github
- essp
- antipatterns
derived_from_private: false
---

Source: `vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf`, pages 34-37.

The appendix reframes common delivery problems as diagnostic antipatterns. Each antipattern is paired with typical root causes, likely impact on quality and velocity, possible AI-assisted responses, non-AI interventions that still matter, and leading indicators that can be watched before lagging zone metrics move.

Examples include big bang releases, gold plating, overengineering, accumulated technical debt, unclear requirements, manual deployments, testing bottlenecks, siloed teams, inconsistent feedback loops, and scope creep. The point is not to memorize a catalog. The point is to turn recurring symptoms into structured hypotheses about where friction lives in the engineering system.

This makes the appendix most useful during step 1 diagnosis and step 2 intervention design. It helps teams map a visible symptom to plausible causes and then choose a small set of leading indicators that can confirm whether the chosen intervention is actually reducing the underlying friction.
