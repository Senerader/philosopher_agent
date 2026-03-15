---
source_path: vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf
visibility: public
page_start: 1
page_end: 12
section_title: Overview and metrics
chunk_index: 0
---

## Page 1

GitHub’s 
Engineering System 
Success Playbook

## Page 2

Introduction: GitHub engineering  
zones and metrics
What are GitHub engineering success zones? 
How to calculate your 12 metrics
Three steps to engineering success
Step 1: Identify the current barriers to success 
Step 2: Evaluate what needs to be done to 
achieve your goals 
Step 3: Implement your changes, monitor results, 
and adjust
Beyond the steps: Make the playbook  
work for you
Alternatives to the GitHub Engineering System 
Success Playbook
Stepping into action and towards success
Appendix: Engineering success antipatterns
Contents
03  
 
 
13
  
  
 
  
28  
31  
33
34

## Page 3

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
At GitHub, we know that better business outcomes aren’t driven just by good-quality code, 
speed, or developer happiness in isolation. It’s actually when quality, velocity, and developer 
happiness are working in unison that organizations see their best results. If you’re looking 
for engineering to provide greater value to your business, it’s crucial to strengthen these — 
let’s call them — foundational zones, and create better conditions for your teams to thrive.  
This is the crux of GitHub’s Engineering System Success Playbook (ESSP) — a three-
step process that can help you drive meaningful, measurable improvements in your 
organization, whether you’re looking to adopt a new AI tool like GitHub Copilot or identify 
and unlock bottlenecks that have been hindering performance. 
Inspired by multiple frameworks, including SPACE  and DevEx , DX Core 4 , and DORA , our 
playbook offers a balanced and comprehensive approach, helping you assign metrics to 
each “zone” that you can track over time and iterate as needed. 
At the heart of our ESSP is a systems thinking 1  approach that prioritizes long-term, 
sustainable improvements. While quick wins can be a great way to get an initiative started, 
they can produce negative downstream effects. For example, accelerating code review 
turnaround time can speed up development, but without addressing the broader system – 
like testing infrastructure and documentation practices – you may risk creating bottlenecks 
downstream and compromising code quality. 
This project was created in response to many customer requests for prescriptive guidance 
on creating meaningful downstream impact from changes in their engineering systems— 
CONTINUED ON NEXT PAGE
 PAGE — 3
Introduction: GitHub 
engineering zones and metrics
1:   A system  is a group of interrelated, or interdependent parts that together serve a function or purpose (‘Thinking in Systems’ by Donalla Meadows).  Systems thinking 
brings a focus to the  relationship between the multiple parts in the system ( The Systems Thinker ), recognising that the whole has emergent properties that are different to  
the sum of its parts.
Here’s a quick breakdown of the process: 
Step 1:  Identify the current barriers to success 
Step 2:  Evaluate what needs to be done to achieve your goals 
Step 3:  Implement your changes, monitor results, and adjust

## Page 4

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 4
often with the introduction of GitHub Copilot. We also engaged with DevEx and DevOps 
metrics vendors to understand both the challenges and successes they’ve experienced 
while helping customers elevate engineering performance or to justify the investment 
in GenerativeAI. So these steps were created to balance the inherent complexity of 
engineering success with practical, achievable steps for teams, including those earlier in 
their improvement journey. 
In this playbook, we’ll outline suggested metrics to monitor as part of your improvement 
efforts for each zone. Keep in mind that these metrics are downstream, or lagging 
metrics, and in the majority of cases should be complemented with leading metrics. 
Both leading and lagging metrics may be measured using telemetry and/or survey data, 
depending on your context, and the way these metrics are calculated will depend on  
your teams’ engineering workflows and the systems supporting them—for example, you 
may use Jira or ServiceNow alongside GitHub. 
As you dig into this playbook, we encourage you to keep a few concepts in mind: 
• Always bring a team perspective to improvement
• Select and use metrics with care to avoid gamification
• Balance the cost of measurement with the benefits of measurement
• Focus on improvements over time rather than overindexing on benchmarks
Engineering teams have the potential to fuel incredible change and accelerate business 
outcomes. With GitHub’s ESSP , you can unlock engineering’s potential through creating  
a culture of excellence that inspires and supports engineers to do their best work.
GitHub’s zones can be understood as a layered system: business outcomes sit at the 
top, supported by a foundation of quality, velocity, and developer happiness. Shaped 
by leading DevEx and DevOps metrics frameworks like SPACE  and DevEx , DX Core 4 , 
and DORA , together, they offer a practical and holistic view of your engineering system. 
For each zone, GitHub suggests three downstream metrics that you can monitor to 
improve your team’s engineering performance, as shown in the figure below.  
While these metrics are from industry best practices and are appropriate for many 
organizations, per SPACE, there can be reasons why an organization may prefer  
different downstream metrics. 
What are the GitHub engineering 
success zones?

## Page 5

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 5
Sustainable improvement in any of these metrics will generally take months. 
We recommend using leading indicators—metrics that are likely to change 
faster—in addition to these downstream metrics. Need some help choosing 
your leading metrics? We’ll give you more guidance below. 
Fig 1: GitHub’s engineering system success metrics
ESSP: Building on SPACE for Engineering Excellence
The SPACE framework provides a comprehensive approach to measuring and 
improving developer productivity. By capturing metrics across multiple dimensions, 
teams can develop a holistic view of their engineering effectiveness. The framework 
recommends measuring at least three of these key dimensions:
• Satisfaction:  Measures developer satisfaction with tools, processes,  
and work environment.
• Performance: Evaluates the outcomes and quality of development processes, 
focusing on both individual and team-level achievements.
• Activity: Counts measurable development actions like pull requests, commits,  
and code reviews.
GitHub’s engineering system success metrics

## Page 6

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 6
• Communication and collaboration:  Assesses how effectively team members 
and code work together, including cross-functional interactions, knowledge 
sharing patterns, and API usage.
• Efficiency and flow: Tracks system throughput and developer time, measuring 
both process efficiency and developers’ ability to maintain focus.
The ESSP builds upon SPACE by identifying 12 specific metrics that help teams 
improve engineering system performance. While the ESSP organizes these metrics 
along developer happiness, quality, velocity, and business outcomes, they map 
directly to the SPACE framework’s holistic approach. 
How to calculate your 12 metrics
Much of how to calculate the 12 metrics will depend on your engineering workflows and 
ecosystem. For example, your tech stack will influence how to measure each of these 
metrics. Perhaps you rely on tools beyond GitHub—like Jira or your incident management 
system—to calculate metrics like lead time or failed deployment recovery time. It’s also 
important to understand your teams’ workflows to determine which data to use from 
GitHub or other data sources in your engineering system. For example, what do you 
consider to be a production failure, and what data source in your engineering tools best 
reflects this definition? Similarly, what is your definition of “in production?” 
Some metrics, like satisfaction with tooling, are ideally suited for developer surveys. 
Surveys can also be a practical choice for metrics like change failure rate—offering valuable 
insights without the need for telemetry. Developers are well-equipped to provide such 
information, and engineering leaders may decide that the benefit of calculating a metric 
through telemetry doesn’t outweigh the cost and complexity. Organizations that don’t yet 
have mature DevEx and/or DevOps metrics tooling may find surveying a particularly  
useful option as they start their transformation journey. DevEx and DevOps metrics 
vendors can assist with compilation of these metrics where an organization does not  
have this capability.

## Page 7

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 7
In using the ESSP metrics it is important to consider these two ideas:
• There will be multiple factors (many outside GitHub) that will impact performance 
improvement. Tooling, team processes and culture, and contributions to the software 
development lifecycle beyond engineering (i.e. prioritization processes, incident 
responses processes) may impact performance in some metrics. 
• We believe that engineering is a team sport.  User-level usage metrics can provide 
insights into how individual developers are engaging with tools, helping organizations  
to support engineers to make the most of available resources. However, it’s crucial  
to approach user-level metrics with care, as misuse, unfair assumptions, or a one-  
size-fits-all mindset can result in overlooking the diversity of roles and contributions 
within a team. Depending on their specific job function, developers will face different 
challenges, and it’s critical to account for these nuances. For engineering system 
metrics we recommend that you focus on teams and organizations, rather than 
scrutinizing individual developers. Using metrics to single out developers or enforce 
rigid standards can erode trust and undermine the collaborative culture essential for 
engineering success.
Leading versus lagging metrics
In the GitHub ESSP , balancing both leading and lagging indicators and using companion 
metrics is essential to achieving engineering system performance improvements. 
• Lagging indicators —often synonyms with downstream metrics—reflect outcomes, such 
as deployment frequency and mean time to recovery, that are measured after work is 
completed. These lagging metrics are key to understanding long-term results, since 
gains often take time to be realized. 
• Leading indicators —typically closer to the source of friction, provide early signals about 
areas that may impact downstream metrics later on. For example, improvements in 
code review time alongside developer confidence in the code review process can signal 
potential improvements in deployment speed or quality. To truly measure progress, 
it’s important to complement each of the 12 engineering success metrics with leading 
indicators that reflect the team’s day-to-day coding activities and the points of friction 
to be addressed, allowing for proactive adjustments. Depending on your friction points, 
the SPACE Communication and Collaboration domain is important to consider as 
part of leading indicators selection. This balanced approach helps teams anticipate 
issues, validate progress, and ensure continuous improvement in alignment with the 
playbook’s goals.

## Page 8

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 8
• Companion metrics —Companion metrics are supplementary indicators that provide 
context to a primary metric, offering a more rounded understanding of performance. 
For instance, while lead time is a metric for assessing velocity, it can sometimes be 
misleading if used alone. Adding companion metrics like change failure rate helps to 
clarify if shorter lead times reflect actual improvements or if there’s a trade-off, such 
as decreased quality due to rushed deployments. However, it’s essential to strike a 
balance; too many companion metrics can dilute focus, and increase measurement 
costs, while too few can risk misinterpretation or misuse of the primary metric. 
Metric recommendations based on zone
Quality
Change failure rate
• SPACE dimension: Performance
• Definition: The percentage of changes 
to production or released to users that 
result in degraded service 2
• Improvement (positive) direction: 
Decrease is good
• Link to business outcomes: Lower 
change failure rate may mean higher 
reliability and fewer disruptions for 
customers
• Calculation advice:  What events are 
considered a production deployment? 
What event signals service failure?
(Median) Failed deployment recovery time
• SPACE dimension: Efficiency and flow
• Definition:  How long it takes an 
organization to recover from a failure  
in production 3
• Improvement (positive) direction:  
Decrease is good
• Link to business outcomes: Faster 
recovery from deployment failures may 
mean reduced downtime and maintains 
customer trust.
• Calculation advice: What event signals 
service failure? What event signals that 
the failure is resolved?
(Median) Code security and maintainability
• SPACE dimension:  Performance
• Definition:  Degree of threat resilience and minimized risk exposure, and ease of 
codebase maintenance, adaptability, and extension
• Improvement (positive) direction:  Increase is good
2    From  DORA:  https:/ /dora.dev/quickcheck/
3    From  DORA:  https:/ /dora.dev/quickcheck/

## Page 9

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
Velocity
(Median) Lead time
• SPACE dimension:  Efficiency and flow
• Definition: The amount of time it takes 
a commit to get into production 5
• Improvement (positive) direction:  
Decrease is good
• Link to business outcomes:  Shorter 
lead times may enable faster 
responses to market demands.
• Calculation advice:  What event signals 
first commit for a release? What 
event signals successful production 
deployment (consider incremental 
release handling)?
Deployment frequency
• SPACE dimension: Activity
• Definition:  How often are releases 
deployed to production 6
• Improvement (positive) direction:  
Increase is good
• Link to business outcomes:  Higher 
deployment frequency may enable  
rapid innovation and faster customer 
feedback cycles.
• Calculation advice: What event signals 
successful production deployment 
(consider incremental release handling)
(Mean) PRs merged per developer
• SPACE dimension: Activity
• Definition:  Number of pull requests successfully merged divided by total developers
• Improvement (positive) direction:  Increase is good
• Link to business outcomes: Enhanced code security and maintainability may reduce 
risks, lower costs, and support ongoing innovation.
• Calculation advice: What event signals code vulnerability and exposure threat? What 
quality attribute signals code maintainability? What quality attribute signals code 
adaptability and reusability? 
• Need to know: Availability of telemetry or survey data to evaluate both code maintainability 
and security
• Tips: This metric could be calculated through a combination of analytics from GitHub 
Advanced Security, SonarQube, or similar products or based on survey data. 4
4    Survey questions can support answering this question where telemetry is not available, for example: It’s easy for me to understand and modify the code that I work with.
1 = Never; 2 = Rarely; 3 = Sometimes; 4 = Very Often; 5 = Always (This question is from  DX’s  Developer Experience Index (used with permission))  
5    From DORA:  https:/ /dora.dev/quickcheck/
6    From DORA:  https:/ /dora.dev/quickcheck/
CONTINUED ON NEXT PAGE
 PAGE — 9

## Page 10

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
Developer happiness
(Median) Flow state experience
• SPACE dimension:  Efficiency and flow
• Definition:  I have significant time for 
deep, focused work during my work days. 
1 = Never; 2 = Rarely; 3 = Sometimes;  
4 = Very Often; 5 = Always 7
• Improvement (positive) direction:  
Increase is good
• Link to business outcomes: Improved 
flow state experience may enable 
engineers to deliver same or higher-
quality work faster, with fewer errors and 
interruptions.
• Calculation advice:  Ordered survey 
responses for organization or team. 
Identify middle value in results. Learn 
more about developer flow.
(Median) Engineering tooling satisfaction
• SPACE dimension:  Satisfaction  
and well-being
• Definition: How would you rate your 
overall satisfaction with the engineering 
tooling you use? 1 = Very unsatisfied,  
2 = Unsatisfied, 3 = Neutral, 4 = Satisfied, 
5 = Very satisfied 8
• Improvement (positive) direction: 
Increase is good
• Link to business outcomes: Greater 
satisfaction with engineering tooling 
may reduce friction, enabling faster and 
higher-quality software delivery.
• Calculation advice: Ordered survey 
responses for organization or team. 
Identify middle value in results. 
(Median) Copilot satisfaction
• SPACE dimension: Satisfaction and well-being
• Definition:  If you have been assigned a Copilot license, how would you rate your overall 
• Link to business outcomes: Higher PR merge rates per developer may indicate effective 
collaboration and accelerated delivery.
• Calculation advice: How many developers to include in calculation? What event signals 
that the PR is merged?
• Tips:  Focus on total PRs rather than calculating average for an individual and then 
calculating the mean. GitHub recommends taking particular care in the calculation of this 
metric. It should not be used to compare engineers to one another. Instead, the metric’s 
purpose is to provide a measure of output adjusted for the number of engineers working 
within a team or organization.
7      This question is from  DX’s  Developer Experience Index (used with permission)
8      This question is from  DX’s  Developer Experience Index (used with permission)
CONTINUED ON NEXT PAGE
 PAGE — 10

## Page 11

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
Business outcome
(Percentage) AI leverage
• SPACE dimension:  Activity
• Definition:  Opportunity being realized 
due to effective engagement with AI, 
through calculating the difference 
between potential and current AI-
driven productivity gains across 
employees working in engineering.
• Improvement (positive) direction: 
Increase is good
• Link to business outcomes: Higher 
AI leverage may reduce manual 
engineering effort, or accelerate or 
enhance the quality of delivery with 
increased cost efficiency.
• Calculation advice:  Average time-
savings associated with AI use. Average 
staff salary per week. Total staff who 
could benefit from AI in engineering. 
Total staff currently ‘engaged’ with AI for 
engineering. Cost of AI per week 
(Percentage) Engineering expenses  
to revenue
• SPACE dimension: Performance
• Definition:  The total engineering spending 
as a proportion of an organization’s total 
revenue.
• Improvement (positive) direction: 
Decrease is good
• Link to business outcomes: Lower 
engineering expense ratios may indicate 
efficient engineering investment and 
increased profitability.
• Calculation advice: What expenses are 
considered ‘total engineering’? What 
constitutes organizational revenue? 
• Tip:  Best monitored at organizational-level 
rather than team-level. 
satisfaction with Copilot? 1 = Very unsatisfied, 2 = Unsatisfied, 3 = Neutral, 4 = Satisfied, 
5 = Very satisfied, NA
• Improvement (positive) direction: Increase is good
• Link to business outcomes:  Higher satisfaction with Copilot may be linked to improved 
velocity or quality outcomes.
• Calculation advice:  Ordered survey responses for organization or team. Identify middle 
value in results
• Tips: This question should only be made available to staff with a Copilot license, or 
results from non-Copilot license holders omitted from the calculation.
CONTINUED ON NEXT PAGE
 PAGE — 11

## Page 12

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
(Percentage) Feature engineering expenses to total engineering expenses
• SPACE dimension:  Performance
• Definition: The proportion of engineering expenses for feature development as a 
portion of total engineering expenses.
• Improvement (positive) direction:  Increase is good
• Link to business outcomes: Higher allocation to feature engineering expenses 
may allow more direct investment in customer-facing improvements that drive 
revenue growth.
• Calculation advice:  What expenses are considered ‘feature development’? What 
expenses are considered ‘total engineering’? 
• Tip:  Best monitored at organizational-level rather than team-level
CONTINUED ON NEXT PAGE
 PAGE — 12

