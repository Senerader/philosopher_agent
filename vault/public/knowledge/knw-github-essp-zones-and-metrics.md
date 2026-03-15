---
id: knw-github-essp-zones-and-metrics
title: GitHub ESSP zones and metrics
status: draft
visibility: public
complexity: 3
references:
  - id: knw-github-essp-playbook
    relation: related
  - id: knw-github-essp-step-1-identify-barriers
    relation: support
  - id: knw-github-essp-step-3-implement-monitor-adjust
    relation: support
  - id: knw-github-essp-tailoring-and-change-management
    relation: related
  - id: knw-github-essp-alternative-measurement-paths
    relation: related
tags:
- github
- essp
- metrics
derived_from_private: false
---

Source: `vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf`, pages 4-12.

ESSP organizes measurement around four zones: quality, velocity, developer happiness, and business outcomes. It extends SPACE rather than replacing it, and GitHub explicitly recommends keeping coverage across at least three SPACE dimensions so the measurement system stays balanced.

The document proposes twelve downstream metrics, three per zone:

- Quality: change failure rate, failed deployment recovery time, code security and maintainability.
- Velocity: lead time, deployment frequency, PRs merged per developer.
- Developer happiness: flow state experience, engineering tooling satisfaction, Copilot satisfaction.
- Business outcomes: AI leverage, engineering expenses to revenue, feature engineering expenses to total engineering expenses.

GitHub warns against using these lagging metrics alone. Teams should pair them with leading indicators that move sooner and with companion metrics that reveal tradeoffs. The playbook also argues that engineering is a team sport, so these metrics should primarily be used at team and organizational level rather than to rank individual developers.
