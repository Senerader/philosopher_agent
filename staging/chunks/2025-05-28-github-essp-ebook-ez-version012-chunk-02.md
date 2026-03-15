---
source_path: vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf
visibility: public
page_start: 18
page_end: 22
section_title: Step 2 evaluate what needs to be done
chunk_index: 2
---

## Page 18

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 18
Step 2: Evaluate what needs to be done  
to achieve your target goal
Purpose of step two:
The goal of this step is to identify, evaluate, and agree on changes that could address the 
barriers identified in step one. By doing this, teams can determine the most effective way 
to achieve their future state and drive improvements in business outcomes. The focus 
is on identifying actionable changes that are aligned with team goals and organizational 
priorities, ensuring interventions lead to tangible, sustainable improvements. These 
changes may be technology changes or additions, but they may be cultural, social, or 
process-related changes, too.
Tasks for step two:
 2.1 Evaluate and prioritize changes:
• Identify potential solutions: Based on the barriers identified in step one, begin by 
brainstorming possible changes that would reduce each barrier. For example, if a barrier 
relates to slow deployments due to manual processes, one intervention might be 
implementing automated deployment pipelines. If developer happiness is low, consider 
initiatives that address workload balance or provide better tooling.
• Estimate cost and/or resource requirements: For each intervention, estimate the 
resources required, including time, personnel, tooling, and budget. Consider both the 
initial implementation effort and ongoing effort. Use this to support evaluation of the 
feasibility of each intervention.
2.2 Conduct a risk, cost, benefit analysis for the changes:
• Identify risks: Each change will have risks. For instance, automating a process may 
inadvertently introduce new errors or bugs if not tested thoroughly. For cultural changes, 
risks might include pushback from the team or slow adoption. Assess the potential 
risks for each change, including both technical risks and people-related risks.
• Weigh the benefits against the risks and costs: For each change, clearly outline the 
expected benefits and how they will support achievement of the future state. Make sure 
to balance this with any potential negative impact on other areas of the business (e.g., 
increasing velocity at the cost of quality or developer happiness). Also account for the

## Page 19

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 19
cost and/or resource implications identified in task 2.1.
• Start with a pilot:  For significant changes or changes with high risk, consider starting 
with a pilot. Test the solution with a few teams or using a smaller subset of the process 
before scaling across the organization. This allows for faster learning and iteration, and 
reduces the chance of large-scale disruption.
• Create a mitigation plan:  For high-priority changes with notable risks, develop a risk 
mitigation plan. This could involve rolling out the intervention in phases or involving 
additional stakeholders to ensure the solution is robust.
2.3 Engage with key stakeholders:
• Review with teams:  Share the proposed changes with engineering teams to get 
feedback. Are the changes realistic? Will the changes support long-term goals, 
or are there concerns about their implementation? Developers, testers, product 
managers, and other team members will have unique insights into the practicalities of 
implementing changes. If you have undertaken a pilot, share the findings from the pilot.
• Secure buy-in:  For more significant changes, secure buy-in from leadership  and other 
stakeholders. Present the expected benefits alongside the potential risks and cost or 
resource requirements. It’s important that there is alignment across all levels of the 
organization, especially when the interventions involve process changes or resource 
investments. Also be realistic about the timeframe for implementation and the 
realization of benefits.
• Incorporate feedback: Be open to adjusting interventions based on feedback from 
stakeholders, including those involved in any pilots. Some changes may need to be 
deprioritized if they are deemed too risky or resource-intensive, while others may be 
refined based on team input.
Data needed for step two:
• Barriers and priorities from step one
• Information on potential changes
• Information on available resources, budgets, etc.
• Outcomes from any pilots

## Page 20

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 20
Skills needed for step two:
• Business case development (cost, risk, and benefit analysis)
• Stakeholder engagement
• Technical acumen and root-cause analysis 
• Research skills to explore potential change options
• Coaching skills to steer and co-create desired behaviors in the pilot
Tips for a successful step two:
• Don’t forget long-term sustainability: Even though it can be tempting to focus on quick 
wins, make sure the selected changes are sustainable long-term. Avoid changes that 
solve short-term problems but create additional maintenance burdens down the road. 
For example, deploying new tools or software across the organization may immediately 
accelerate velocity, but without investing in training, support, and change management 
strategies, it can lead to frustration, errors, and reduced performance.
• Consider trade-offs across zones:  Remember that changes may affect more than one 
zone at once. Make sure that changes to improve one zone (such as velocity) do not 
significantly negatively impact another (such as developer happiness or quality). 
• Involve your team early: Changes are more likely to succeed if they’re co-created with 
the team. Avoid imposing top-down changes without gathering input from those who 
will be most impacted.
• Identify success metrics: Before implementing any changes, define how success 
will be measured. Establish which metrics or indicators will show that the intervention 
is leading towards your future state. Consider both leading and lagging indicators for 
your target future. For example, a reduction in deployment time may be your lagging 
indicator, but developer perception of PR duration and reduction in PR dwell time are 
leading indicators. 
• Stay agile and iterative: Don’t wait until you have the perfect solution to implement 
changes. Adopt an iterative approach where small changes can be tested with leading 
indicators, refined, and scaled over time. This reduces risk and ensures that the team 
can pivot if an intervention isn’t yielding the expected results.
• Focus on high-impact, low-effort wins: If your team is overwhelmed by potential 
changes, start with the solutions that are both easy to implement and have high 
potential impact. These can provide immediate wins and build momentum for tackling 
larger, more complex barriers.

## Page 21

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 21
How GitHub identifies  
and pilots changes
With a baseline established and hypothesis on the key bottlenecks relating to quality 
improvements, we assigned a team to dig deep on deployment rollbacks. The team proposed 
a few changes that would allow for earlier detection of production issues, and opportunities to 
respond to issues more quickly. Each proposal was estimated based on level of effort and level of 
impact. 
These changes included extending a wait time between deployments to allow for more time to 
test code in between deployments, ultimately making a code rollback easier. This was a very low 
effort change, with a potentially high impact. The team also proposed making changes to how 
rollbacks were triggered and executed, which reduced the amount of time a rollback would take, 
thus improving time to restore. This was a medium effort change, but the potential positive impact 
was deemed high. 
The team also proposed strategies to detect change failure earlier in the process, including: 
• Implementing an end-to-end testing strategy during deployments  
(leveraging GitHub Actions), 
• A stage-based deployment model, which would deploy code to internal  
 staff before deploying to customers 
• An automated error detection system, which would alert when new  
exceptions were detected during a deployment. 
The team also recognised the value of our secret scanning and code scanning features, and 
sought to embed them even more deeply in our practices. These suggestions were made by 
consulting with many teams and experts, including application developers, observability teams, 
reliability teams, and delivery teams. 
In parallel, and based on feedback from developers about difficulties in responding to 
unpredictable and confusing deployments, the team proposed simplifying notifications, surfacing 
helpful log messages during the deployment process, and streamlining the UI. We also saw an 
opportunity to improve the developer experience by increasing our transparency for when a 
deployment was likely to start, and to enhance the monitoring experience during the deployment. 
It was important to weigh these proposals against the potential risks. Some of the proposed plans 
required slowing down deployments, which would increase the mean lead time for changes, and

## Page 22

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 22
reduce deployment frequency metrics in our velocity zone. We weighed the impact to our velocity 
and determined how much of an impact we were able to withstand in order to see gains in quality 
metrics. To counteract some of the reductions in velocity, the team also proposed increasing the 
number of changes that could be deployed at once. This analysis was done very carefully to make 
sure that an increase in changes would not result in a reduction of quality. 
Once we decided which process and tooling changes to pursue—just like our features—we then 
took an incremental approach to roll-out. You can work in incremental changes in two different 
ways: 
• The number of changes you make at a given time. Keep the scope small  
so you know which change is driving what impact
• In terms of the distribution of the change (then scale to build confidence)
We also used a test application that allowed us to A/B test our process and tooling changes to 
more accurately understand their impact on key metrics.
Step 3: Implement your changes, monitor  
the results, and adjust
Purpose of step three:
The goal of this step is to scale the prioritized changes, including monitoring the 
progress towards reaching your target future state. Successful implementation requires 
ongoing monitoring and willingness to adjust to make sure changes are delivering the 
desired improvements and are contributing to your business outcomes. By tracking 
performance and iterating as needed, teams can make sustained progress and avoid 
regressing.
Tasks for step three:
 3.1 Implement the changes:
• Assign ownership and responsibilities: Ownership ensures accountability and 
makes it easier to monitor progress, so each intervention should have a clear owner 
responsible for its implementation and success. The owner may be a developer,

