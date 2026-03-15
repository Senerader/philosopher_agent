---
source_path: vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf
visibility: public
page_start: 34
page_end: 37
section_title: Engineering success antipatterns appendix
chunk_index: 5
---

## Page 34

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 34
Antipatterns  are “common solutions to 
common problems where the solution  
is ineffective and may result in 
undesired consequences. ” The first  
step  in GitHub’s ESSP is to understand 
friction or bottlenecks in the team or 
organization’s engineering system. The 
following table provides examples of 
antipatterns that may be synonymous 
with friction or bottlenecks. The table 
also lists potential changes that may 
address the antipatterns and potential 
leading metrics and indicators that may 
be used to monitor whether the changes 
are having the desired impact. GitHub 
recommends asking engineering teams 
to support the identification of these 
antipatterns and to confirm the leading 
indicators that are best suited to the 
situation, as those listed may not be an 
appropriate fit for your situation.
Appendix: 
Engineering 
success 
antipatterns
Anti-Pattern Big Bang Releases
Description Teams wait too long to release, deploying large 
batches of code at once.
Potential root-causes Fear of destabilization with frequent releases.
Lack of CI/CD pipeline maturity.
Preference for ‘all-at-once’ (or quality) certainty.
Strict compliance requirements.
Long review cycles between PR and deployment.
Quality impact Bugs and regressions are harder to detect and fix 
in larger code bases. Some features may also be 
released without having met quality expectations.
Velocity impact Slows release cycles due to complex, high-risk 
deployments.
How AI could help Use GitHub Copilot to write and review 
code faster, potentially leading to quicker 
PR completion, leading to more frequent 
deployments. Detect and resolve integration 
issues to prevent change failures.
Friction requiring non-AI 
intervention
Cultural issues or lack of communication 
between teams.
Potential leading or 
additional metrics or 
indicators that may  
indicate this antipattern 
[↑ ↓ trend suggestions 
antipattern]
Size of PRs ↑
PRs reviewed not merged ↑
PR review time ↑
Long-lived feature branches ↑
Zone metrics that may 
indicate this antipattern
[↑ ↓ trend suggestions 
antipattern]
Deployment frequency ↓
Change failure rate ↑
Lead time ↑

## Page 35

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 35
Anti-Pattern Gold Plating Overengineering Racking up technical debt
Description Developers spend too much 
time perfecting code or adding 
unnecessary features.
Building overly complex solutions 
for simple problems.
Ignoring or deferring technical debt, 
allowing inefficient and vulnerable 
systems to persist.
Potential root-causes Culture of perfectionism.
Desire to showcase technical skills.
No clear MVP focus or feature 
prioritization.
Desire to future-proof 
unnecessarily.
Pressure to add value through 
complexity.
Deadline-driven focus on features.
Long-term impact of technical debt 
undervalued.
Significant risk in unknown 
upgrades and effort to resolve 
incompatibility issues.
Quality impact Increased complexity introduces 
more potential for bugs without 
added value to user.
Complex systems are more prone 
to bugs and harder to maintain.
Code becomes brittle and bug-
prone, leading to poor system 
health.
Velocity impact Adds unnecessary time to 
development as teams over-focus 
on perfection.
Slows development as complexity 
adds overhead to build and 
maintain systems.
Increases time to develop new 
features as workarounds grow.
How AI could help Use GitHub Copilot to simplify 
code and remove redundant code.
Use GitHub Copilot to refactor 
existing code. This could be to 
make the code more modular, or to 
suggest a simpler way of solving the 
problem.
Use GitHub Copilot to create 
tests and refactor existing code. 
This could be to make the code 
more modular, or to suggest a 
simpler way of solving the problem. 
Autofix may reduce effort and 
increase satisfaction with starter 
suggestions in PRs.
Friction requiring non-AI 
intervention
Product management decisions 
about feature prioritization.
Overdesigning systems to solve 
edge cases that rarely occur.
Prioritize and allocate engineers to 
address the technical debt.
Potential leading or 
additional metrics or 
indicators that may  
indicate this antipattern 
[↑ ↓ trend suggestions 
antipattern]
Work in Progress ↑ 
Late-in cycle code churn ↑
Usage of features/sub-features ↓
Developer satisfaction with delivery 
cadence ↓
Usage of features/sub-features ↓ 
Cognitive complexity ↑
Code complexity ↑
Large blocks of commented out 
code ↑
Duplicated Blocks ↑
Hardcoded values and secrets ↑
Dependency issues ↑
Zone metrics that may 
indicate this antipattern
[↑ ↓ trend suggestions 
antipattern]
Lead time ↑ Code security and maintainability ↓
Lead time ↑
Code security and maintainability ↓
Lead time ↑
Change Failure Rate ↑

## Page 36

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 36
Anti-Pattern Unclear requirements Manual deployments Testing bottlenecks
Description Teams receive vague or incomplete 
requirements, leading to 
misunderstandings.
Relying on manual steps for 
deployment instead of automation.
Relying on manual testing or 
insufficient test automation, 
causing delays.
Potential root-causes Pressure to start development 
quickly.
Immature product discovery 
process.
Frequent priority shifts from 
stakeholders.
Perception that manual is ‘good 
enough.’
Fear of effort needed for 
automation.
Lack of investment in DevOps 
practices.
Belief in thoroughness of manual 
testing.
Resource constraints for 
automation.
Limited familiarity with modern  
test tools.
Previous experience with brittle, 
costly, or flaky tests.
Quality impact Poorly defined requirements lead to 
incorrect or low-quality features.
Manual deployments introduce 
inconsistent outcomes that can 
lead to post-deployment bugs.
Lack of thorough testing introduces 
more bugs into production.
Velocity impact Time wasted clarifying 
requirements or building incorrect 
features.
Slows releases. Delays releases as testing takes 
longer.
How AI could help Stay tuned: GitHub’s AI powered 
platform continues to evolve
Use GitHub Copilot to create 
automation, such as GitHub Action 
workflows, to replace manual 
deployments.
Use GitHub Copilot to troubleshoot 
why a deployment automation has 
failed.
Use GitHub Copilot to create test 
suites, and automate CI workflows, 
to remove frictions.
Friction requiring non-AI 
intervention
Engaging with stakeholders to 
ensure real-world needs are 
reflected in the requirements.
Inconsistent  processes and 
human reluctance to adopt 
automated deployment pipelines.
The need for a robust  
testing strategy aligned with  
the project’s goals
Potential leading or 
additional metrics or 
indicators that may  
indicate this antipattern 
[↑ ↓ trend suggestions 
antipattern]
Time spent in meetings ↑
Work in Progress ↑
Rework ↑
Developer frustration ↑
Count of manual steps per 
deployment ↑
Dwell (delay) time during CI/CD  ↑
Deployment duration  ↑
Automated test coverage ↓
Time spent on manual testing ↑
Zone metrics that may 
indicate this antipattern
[↑ ↓ trend suggestions 
antipattern]
Flow state experience ↓
Lead time ↑
PRs merged per developer ↓
Deployment frequency ↓
Failed deployment recovery time ↑
Change failure rate ↑
Engineering tooling satisfaction ↓
Change failure rate ↑
Deployment frequency ↓
(Median) Lead time ↑
Engineering tooling satisfaction ↓

## Page 37

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
PAGE — 37
Anti-Pattern Siloed teams Inconsistent feedback loops Scope creep
Description Teams operate in silos, failing to 
share data, tools, or processes 
across teams.
Feedback from testing, users, or 
other stakeholders is not provided 
in a timely or consistent manner.
Constant addition of features or 
changes mid-development without 
proper evaluation.
Potential root-causes Incentives misaligned across 
teams.
Culture prioritizes team-specific 
goals.
Historical habit of independent 
operation.
Waterfall mindset undervaluing 
iteration.
Feedback viewed as an end-phase 
activity.
Lack of real-time feedback tools.
Unclear project boundaries.
Poor change management 
practices.
Culture discourages saying “no” to 
requests.
Quality impact Inconsistent processes and tools 
result in lower-quality handoffs 
between teams.
Bugs and user issues linger due to 
delayed feedback.
Rushed development due to scope 
creep often leads to more bugs and 
lower quality.
Velocity impact Cross-team dependencies lead to 
delays when teams aren’t aligned.
Slows iteration cycles, as engineers 
aren’t able to adapt quickly.
Introduces unplanned work that 
delays original timelines.
How AI could help Copilot features can help improve 
documentation and code 
explanations.
Use GitHub Copilot for Pull 
Requests to automatically analyze 
pull requests and suggest changes 
to provide a more consistent 
feedback loop.
Developers can use GitHub 
Copilot to ask questions about a 
pull request, providing for a more 
informed pull request review 
that leads to a more consistent 
feedback loop
Stay tuned: GitHub’s AI powered 
platform continues to evolve
Friction requiring non-AI 
intervention
Cultural issues or lack of 
communication between teams.
Human communication and 
prioritization of feedback.
Managing stakeholder expectations 
and ensuring a disciplined 
approach to scope management.
Potential leading or 
additional metrics or 
indicators that may  
indicate this antipattern 
[↑ ↓ trend suggestions 
antipattern]
Cross-team collaboration 
frequency ↓
Handoff delays ↑
Rework frequency ↑
Poor meeting attendance ↑
Feedback frequency ↓
Feedback quality ↓
Customer satisfaction ↓
Age of PR’s last human activity ↑
Scope changes per sprint ↑
Ratio of issue types per sprint ↑
Time spent on unplanned work ↑
Zone metrics that may 
indicate this antipattern
[↑ ↓ trend suggestions 
antipattern]
Lead time ↑
PRs merged per developer ↓
Deployment frequency ↓
Lead time ↑
Flow state experience ↓
Lead time ↑

