---
source_path: vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf
visibility: public
page_start: 22
page_end: 27
section_title: Step 3 implement changes monitor and adjust
chunk_index: 3
---

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

## Page 23

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 23
engineering lead, or cross-functional team, depending on the nature of the intervention. 
Link the implementation of changes to senior or executive KPIs (key performance 
indicators) or targets.
• Foster communication and transparency: Clearly communicate to all relevant 
stakeholders when an intervention is being rolled out, why it’s being done, and what 
the expected outcomes are. This transparency fosters trust and encourages team 
members to actively support the change. Encourage feedback during the rollout to 
help identify any immediate issues or resistance. Remember that tooling or technology 
changes also often require accompanying policy, process, or cultural changes.
• Train teams when necessary:  Some changes may require new skills or processes. For 
example, if implementing a new automated deployment pipeline, make sure teams are 
trained in how to use the tooling. Offer support and guidance to reduce friction during 
adoption.
3.2 Monitor performance post-implementation:
• Track key metrics: Once changes are implemented, track the identified metrics across 
the zones. Compare the new metrics with the baseline established in step one to 
evaluate the impact of the intervention. However, be realistic about the time it takes 
for metrics to shift and expect some variance in performance rather than consistent 
gains. Most change initiatives will require the use of a set of leading indicators. Often, 
qualitative data like surveys are a useful leading indicator in addition to close to code 
metrics such as pull request review times, depending on the current and future state 
and barriers being addressed by the changes. Learnings from any pilots can be useful in 
understanding likely timeframes to achieve downstream improvements.
• Gather qualitative feedback: In addition to metrics, gather feedback from developers, 
operations, and other stakeholders on how the changes are impacting their day-to-day 
work. Use interviews and team retrospectives to understand whether the changes are 
positively affecting team morale, collaboration, or overall satisfaction.
• Identify early wins and challenges: Keep an eye out for both early successes and 
challenges. Celebrate small wins, such as reductions in pull request review times  
or improved test coverage, to build momentum. On the flip side, be prepared to  
identify and address any resistance or unforeseen issues early, before they grow  
into larger problems.

## Page 24

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 24
3.3 Adjust and iterate:
• Analyze what’s working and what’s not: After an initial period of implementation, review 
the data and feedback to confirm that the changes are having the desired effect. Are 
the target metrics improving? Are there trade-offs that need to be reconsidered? For 
example, are quality targets being maintained while velocity is improving? It’s essential 
to critically assess whether the changes are solving the barriers identified in step one.
• Pivot if necessary: If changes are not delivering the expected results, don’t hesitate to 
pivot. It’s better to adjust mid-course than to persist with solutions that aren’t working. 
Revisit the other potential actions from step two, and consider alternative approaches 
or adjustments.
• Maintain continuous feedback loops: Make monitoring and feedback an ongoing 
process. Don’t treat implementation as a one-time effort. Use team retrospectives, 
stakeholder reviews, and performance dashboards to maintain a cycle of continuous 
improvement. Regularly check in on the health of the zones and be proactive in 
adjusting the changes as needed. Consider using automated alerting to make sure  
that if a metric is falling outside expected performance ranges, it can be reviewed and 
acted upon.
Tools needed for step three:
• Analytics and metrics dashboards
• Survey and feedback tools
• Project and change management tools
Skills needed for step three:
• Implementation management
• Data analysis and monitoring
• Change management
• Technical problem-solving and iteration
Tips for a successful step three:
• Don’t expect immediate perfection:  Not all changes will produce immediate or 
dramatic improvements. Be patient, and allow time for the changes to make a positive

## Page 25

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 25
impact. Surveys are a great tool for the earlier stages of an intervention. Remember, it 
may take time for the team to adjust and for the changes to be fully embedded.
• Keep iterating on the changes: Remember that even after successful implementation, 
further improvements can always be made. Teams should be encouraged to treat 
the process as ongoing and remain open to refining changes as new challenges arise. 
Changes in operating circumstances can also prompt the need to consider further 
iterations.
• Watch out for unintended consequences: Some changes may introduce new friction 
points or affect other areas of the workflow in unexpected ways. For example, speeding 
up deployments may lead to more frequent post-release bugs if the quality zone isn’t 
balanced. Be vigilant in identifying these side effects and address them promptly.
• Check in on psychological safety: Make sure that teams still feel comfortable speaking 
up about issues post-implementation. Teams should feel empowered to offer honest 
feedback about what’s working and what isn’t, without fear of judgment.
• Evaluate long-term impact: Over time, make sure that the improvements are sustained 
and that new challenges aren’t introduced. Look for enduring improvements in team 
performance and morale.
• Use feedback for further learning:  Treat failures as opportunities for learning . If a 
change doesn’t work, use the data and feedback gathered to understand why, and  
apply those

## Page 26

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 26
Maximizing the impact of your engineering system requires intentionality—which can be 
achieved through a systematic approach, a learning mindset, and investment in the tools, 
skills, and time needed to drive sustainable improvements. 
GitHub provides a suite of tools, including GitHub Copilot, to support you in achieving 
success in your software development, but these tools also need to be deployed 
intentionally regarding the problems you’d like to solve, and with an awareness that tooling 
changes often require social, process, and cultural changes. 
How GitHub implements change
Following our incremental/piloting approach described above, GitHub very carefully rolled out the 
changes identified in step two to an increasing number of applications. Even beyond our piloting 
efforts, we still feature flag our process and tooling changes so that if an unexpected situation 
arises as we scale the rollout, we can quickly revert to the previous process/tooling. 
For example, when we rolled out changes to the deployment pipeline, we changed how we 
measured deployment rollbacks. Previously, our metrics looked at a raw count of rollbacks, but 
given our intervention to deploy changes to staff before customers, we began tracking rollback 
metrics with a more granular view, measuring when a rollback included customer impact 
versus impacting internal staff. We also began tracking how soon issues were identified after a 
problematic deployment. This allowed us to show that the changes to the pipeline did improve 
our quality metrics, by completely preventing external incidents in some cases, and being able 
to respond to defects faster, thus reducing our change failure rate. Similarly, when implementing 
our end-to-end testing strategy, we were able to measure when the tests uncovered an issue that 
would have otherwise made it to production. This also reduced our change failure rate. 
We also rolled out UI changes of our deployment tooling incrementally, which allowed the team 
to gather feedback and pivot approaches along the way. As part of the rollout, the team identified 
that while the UI improvements were helpful, some developers craved a more direct support 
model. In response, the team built alerts to proactively alert a support team if intervention is 
needed. While the UI could guide developers, the support model allowed for quicker resolution for 
more complex scenarios.

## Page 27

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 27
A note on Copilot metrics:
The ESSP is part of GitHub’s commitment to support our customers’ understanding 
and growth of Copilot impact. GitHub will continue to connect with our customers to 
understand their highest data priorities, and develop and deliver a roadmap accordingly. 
Our current priority is to focus on exposing leading indicators of Copilot success (such 
as those on the Metrics API), which can be used alongside customer-sourced (or partner 
supported) lagging indicators. 
When implementing GitHub Copilot, we recommend using leading indicators to guide 
your pilot and scaling efforts. Surveying developers on their experience with GitHub Copilot 
provides early insights into areas needing additional training, where GitHub Copilot is most 
beneficial, and potential time savings in achieving your engineering goals.

