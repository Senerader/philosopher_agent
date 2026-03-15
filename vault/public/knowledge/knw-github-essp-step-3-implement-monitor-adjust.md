---
id: knw-github-essp-step-3-implement-monitor-adjust
title: ESSP step 3 implement monitor adjust
status: draft
visibility: public
complexity: 3
references:
  - id: knw-github-essp-step-2-evaluate-changes
    relation: prerequisite
  - id: knw-github-essp-zones-and-metrics
    relation: support
  - id: knw-github-essp-tailoring-and-change-management
    relation: support
tags:
- github
- essp
- workflow
derived_from_private: false
---

Source: `vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf`, pages 22-27.

Step 3 is the execution and learning loop. GitHub recommends assigning clear owners, communicating why the change is happening, training teams when needed, and monitoring both quantitative metrics and qualitative feedback after rollout.

This step assumes lagging metrics will take time to move, so leading indicators and developer surveys are important early signals. Teams should look for early wins, detect resistance quickly, and keep continuous feedback loops active through dashboards, retrospectives, and stakeholder reviews. The document also stresses watching for unintended consequences and protecting psychological safety so people continue surfacing problems.

GitHub's example uses incremental rollout and feature flags for process and tooling changes. It also shows that implementation can require updating the measurement model itself: after changing the deployment pipeline, GitHub refined rollback metrics to distinguish customer impact from internal impact. For Copilot adoption, the document recommends leading indicators and developer feedback before expecting downstream business effects.
