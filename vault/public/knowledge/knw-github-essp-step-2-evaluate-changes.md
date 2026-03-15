---
id: knw-github-essp-step-2-evaluate-changes
title: ESSP step 2 evaluate changes
status: draft
visibility: public
complexity: 3
references:
  - id: knw-github-essp-step-1-identify-barriers
    relation: prerequisite
  - id: knw-github-essp-zones-and-metrics
    relation: support
tags:
- github
- essp
- workflow
derived_from_private: false
---

Source: `vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf`, pages 18-22.

Step 2 converts diagnosed barriers into candidate interventions. GitHub recommends identifying process, tooling, cultural, or organizational changes that could address the bottlenecks found in step 1, then evaluating those changes for impact, effort, risk, cost, and sustainability.

The playbook treats tradeoffs as first-class design constraints. A change that improves one zone while damaging another is not automatically a success, so teams should estimate likely cross-zone effects before rollout. High-risk or high-cost interventions should start as pilots, not as broad organizational mandates.

GitHub's example centers on deployment quality. The team considered extending wait time between deployments to catch problems earlier, accepted that this could reduce deployment frequency, and then looked for compensating changes such as increasing the number of changes per deploy. They also used a test application to evaluate process and tooling changes before wider rollout.
