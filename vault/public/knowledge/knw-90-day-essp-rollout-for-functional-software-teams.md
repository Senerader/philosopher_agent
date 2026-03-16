---
id: knw-90-day-essp-rollout-for-functional-software-teams
title: 90-day ESSP rollout for functional software teams
status: draft
visibility: public
complexity: 4
references:
  - id: knw-essp-goals-for-functional-software-teams
    relation: prerequisite
  - id: knw-functional-team-belonging-friction
    relation: prerequisite
  - id: knw-github-essp-step-3-implement-monitor-adjust
    relation: support
  - id: knw-github-essp-tailoring-and-change-management
    relation: support
tags:
  - essp
  - rollout
  - team-health
derived_from_private: false
---

This card translates the ESSP goals for the three functional software teams
into a 90-day pilot. It assumes that the main problem is weak belonging to the
functional team and that the first quarter should focus on baselining,
lightweight rituals, and team-level goals rather than on hard individual KPIs.

90-day structure

1. Days 1-14: baseline
   Run a short survey, collect a small collaboration baseline, and confirm
   current team rituals and participation.
2. Days 15-30: define team goals
   Each team defines 2-3 goals that are not tied to a single project and names
   an owner for the rollout.
3. Days 31-75: run the pilot
   Start the rituals, publish the team goals, and review early movement every
   two weeks.
4. Days 76-90: inspect and decide
   Review survey movement, collaboration signals, and delivery guardrails, then
   decide what becomes standard practice in the next quarter.

Recommended 5-question pulse survey

Use a 1-5 scale from strongly disagree to strongly agree.

1. I feel that I belong to my functional software engineering team, not only to
   my current project.
2. I understand my team's goals beyond the delivery goals of my current
   project.
3. My team gives me useful technical support and context when I need it.
4. Working across projects inside my functional team is normal and valuable.
5. Our team rituals help me do better work instead of creating overhead.

Recommended leading indicators

- average score for the five survey questions above
- attendance rate for team rituals
- number of cross-project design reviews or peer reviews inside the same
  functional team
- number of knowledge-sharing sessions, reusable standards, or engineering
  practices created by the team
- number of engineers who can name the team's quarterly goals without prompts

Recommended ESSP guardrails

- flow state experience
- lead time
- change failure rate

If these guardrails deteriorate while team-belonging metrics improve, then the
pilot is adding coordination cost and should be adjusted.

Example quarterly targets for the three teams

These are sample targets for the first quarter and should be calibrated after
the baseline. The intent is to set improvement targets, not arbitrary absolute
quotas.

Team A: identity and team rhythm

- improve the belonging survey question by at least 0.5 points from baseline
- achieve at least 80% average attendance in core team rituals
- publish and review 3 team goals that are visible to all members

Team B: cross-project collaboration

- increase cross-project design review or peer review activity by 30% from
  baseline
- run at least 2 internal knowledge-sharing sessions during the quarter
- improve the survey question about cross-project collaboration by at least 0.5
  points from baseline

Team C: shared standards and support

- produce at least 2 shared engineering standards, templates, or reusable
  practices adopted by multiple projects
- improve the survey question about useful technical support by at least 0.5
  points from baseline
- keep lead time and change failure rate within an agreed tolerance while the
  pilot is running

Recommended rituals

- weekly 30-minute team sync focused on cross-project issues, team goals, and
  engineering practices rather than project status reporting
- biweekly technical forum where one project shares lessons, tooling, or design
  decisions with the rest of the functional team
- monthly team retrospective focused on team identity, collaboration friction,
  and what support is missing across projects
- rotating cross-project design review or architecture review inside the
  functional team
- lightweight written team goals page that is reviewed every two weeks

Operating rules for the pilot

- measure at team level, not individual ranking level
- keep rituals short and tied to practical engineering value
- do not replace project goals; complement them with functional team goals
- inspect results every two weeks and remove rituals that create noise without
  improving belonging or collaboration
