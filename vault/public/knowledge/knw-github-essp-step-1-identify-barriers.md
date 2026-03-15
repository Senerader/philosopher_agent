---
id: knw-github-essp-step-1-identify-barriers
title: ESSP step 1 identify barriers
status: draft
visibility: public
complexity: 3
references:
  - id: knw-github-essp-zones-and-metrics
    relation: prerequisite
  - id: knw-github-essp-engineering-antipatterns
    relation: example
tags:
- github
- essp
- workflow
derived_from_private: false
---

Source: `vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf`, pages 14-17.

Step 1 is about understanding the current state, the desired future state, and the barriers between them. GitHub recommends clarifying which zones matter most for current business goals, gathering qualitative feedback from developers and stakeholders, and quantifying baseline performance where possible.

The important methodological point is to look for root causes rather than symptoms. A visible slowdown in velocity can come from testing trust, unclear requirements, deployment process friction, or cross-team coordination issues. The playbook explicitly says work can start even if baseline instrumentation is incomplete, but the goal is still to develop a defensible picture of current friction.

GitHub's example in this section starts from a quality concern. The team measured change failure rate and recovery time from incident tooling, then combined that baseline with investigation into how rollbacks and issue detection were actually happening. That pattern makes step 1 a diagnosis phase, not a solution phase.
