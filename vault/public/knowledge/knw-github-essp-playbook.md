---
id: knw-github-essp-playbook
title: GitHub ESSP playbook
status: draft
visibility: public
complexity: 2
references:
- id: knw-github-essp-zones-and-metrics
  relation: support
- id: knw-github-essp-step-1-identify-barriers
  relation: support
- id: knw-github-essp-step-2-evaluate-changes
  relation: support
- id: knw-github-essp-step-3-implement-monitor-adjust
  relation: support
- id: knw-github-essp-tailoring-and-change-management
  relation: support
- knw-github-essp-alternative-measurement-paths
- id: knw-github-essp-engineering-antipatterns
  relation: example
tags:
- github
- essp
- engineering-systems
derived_from_private: false
---

Source: `vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf`, especially pages 3-4, 13, 28-33.

GitHub's Engineering System Success Playbook treats engineering effectiveness as a system rather than a single productivity score. Business outcomes sit on top of three foundational zones: quality, velocity, and developer happiness. The playbook uses those zones to organize measurement and intervention work.

The playbook's operating loop is:

- identify the barriers that prevent the target future state
- evaluate which process, tooling, or organizational changes are worth trying
- implement changes incrementally, monitor results, and adjust

ESSP is intended for practical improvement work such as Copilot adoption or bottleneck removal. Its core claim is that teams should optimize the engineering system as a whole, because local gains in one area can create downstream regressions elsewhere if they are not balanced across the other zones.