---
source_path: vault/public/assets/2025-05-28-GitHub-ESSP-Ebook-EZ-Version012.pdf
visibility: public
page_start: 13
page_end: 17
section_title: Step 1 identify barriers to success
chunk_index: 1
---

## Page 13

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
Three steps to 
engineering success
CONTINUED ON NEXT PAGE
 PAGE — 13
These three steps are the heart of GitHub’s ESSP , as they highlight your current friction 
points and manage your expectations for how changes will drive improvements. As 
you consider your future state, GitHub recommends thinking across the zones: quality, 
velocity, developer happiness, and how together they contribute to business outcomes. 
As part of the three-step process, GitHub also recommends the use of leading 
indicators—like close to code telemetry such as number of commits, and surveys—to 
monitor the early impact of the agreed changes on your engineering system. Your choice 
of leading indicators will depend on the friction points being addressed.
Fig 2: Three steps to engineering success

## Page 14

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 14
Step 1: Identify the current barriers to success
The purpose of step one:
The goal of this step is to develop a clear understanding of the obstacles preventing 
improvements. By understanding your current state and your desired future state, 
and the gaps and barriers to reach the future state, teams can prioritize areas that 
need attention and ensure changes are targeted and effective. This step encourages 
understanding of your current performance baseline. That being said, if these current 
performance baselines have not yet been quantified, it is still possible to start working 
towards improvements.
Tasks for step one:
1.1 Audit current processes, gather data, and understand organizational priorities:
• Build an understanding of your development lifecycle:  Put together a complete 
picture of your teams’ SDLC  processes and workflows, from idea to ship to learn . 
Identify the different tasks and process flows, while also recognising that teams may 
have different development lifecycles. Understanding the lifecycle is an essential 
requisite to calculating metrics and determining bottlenecks. Need help charting your 
lifecycle? There are many different ways to chart  your lifecycle . Check out GitHub’s 
documentation on building diagrams.
• Gather available metrics:  Collect your team’s data on existing metrics for the zones, 
so that you have a baseline. You don’t need advanced telemetry data to get started: 
qualitative insights from developer surveys or focus groups can offer initial baselines. 
These qualitative baselines capture team sentiments and highlight areas needing 
attention. As you progress, you can make a plan to incorporate quantitative data to 
refine your baselines and expand your view. By regularly reviewing progress against your 
baselines, your organization can make informed decisions, adjust strategies proactively, 
and celebrate tangible achievements on your path to engineering success.
• Industry benchmarks: Benchmarks are reference points drawn from industry data, 
often representing average performance, or higher percentiles such as P75 or P90, for 
specific metrics (See the DX Core 4  benchmarks  and the DORA report benchmarks ). 
While benchmarks can reveal how your team’s performance compares to others, 
remember to take into account differences in team workflows. There is benefit in 
focusing on improvements over time rather than benchmarks.

## Page 15

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 15
• Understand zone priorities: Engage with stakeholders to clarify which zones are 
currently most critical for the organization given your business goals. Remember that 
developer happiness is just as critical as the other zones. This helps to align the team’s 
efforts with business goals and strategy.
1.2 Conduct qualitative research:
• Gather feedback:  Interview or survey developers and other key stakeholders to 
understand their pain points across the development lifecycle, remembering to include 
the outer loop. 
• Focus on where friction exists: where there seems to be delays and what impacts 
engineers’ satisfaction. For organizations with more mature analytics capabilities, 
you may be able to go beyond the recommended zone metrics to understand 
more granular trends associated with your development lifecycles, like periods of 
delay when progressing a pull request from submission to merge.
• Make sure that you’re seeking information on cultural, social, or process factors 
that may affect the development lifecycle. Are team members feeling supported 
and motivated? Is there a mindset that’s adversely impacting quality or velocity? 
Are internal tools or processes slowing down work?
1.3 Prioritize key metrics and barriers:
• Map findings to the zones:  Categorize each identified barrier by which zones it impacts 
and onto your developer lifecycles.
• Prioritize the metrics to target:  Once barriers are identified, prioritize which metrics 
should be targeted for improvement. Consider any trade-offs between elements of  
your desired future state and the barriers that are most actionable, keeping in mind  
your business goals. 
Tools needed for step one:
• Analytics and metrics dashboards 
• Survey and feedback tools (to support focus groups, interviews, etc.)
• Process mapping tools

## Page 16

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 16
Skills needed for step one:
• Data analysis skills
• Stakeholder engagement
• Technical acumen and root-cause analysis 
Tips for a successful step one:
• Focus on root causes, not just symptoms: While undertaking research, avoid being 
misled by surface-level issues. For example, slow velocity might be attributed to manual 
testing, but the root cause could be a lack of trust in automated testing. Dig deeper to 
uncover the underlying problems. Common antipatterns in software engineering can 
be a great place to start.
•  A note: Antipatterns are common solutions to common problems where the 
solution doesn’t actually resolve the problem and may inadvertently cause 
undesired consequences. Check out this GitHub resource on antipatterns  for a 
detailed look into how they might manifest within your team.
• Involve the right people:  During tasks 1.1 and 1.2, gather input from various roles 
such as developers, testers, operations, security, and product managers to ensure a 
comprehensive view of the workflow. This prevents overlooking critical perspectives or 
bottlenecks.
• Balance quantitative and qualitative data: Metrics alone don’t tell the full story. Make 
sure data-driven analysis includes feedback from the team to capture cultural and 
morale-related barriers that may not appear in the numbers. Learn more  about the 
value of both qualitative and quantitative data to improve engineering system success.
• Don’t overwhelm yourself with too many barriers:  Focus on the most impactful 
barriers rather than trying to tackle everything at once. Prioritize key areas that will 
provide the greatest momentum towards your future state.
• Ensure psychological safety: Create an environment where team members feel safe 
enough to share their frustrations and challenges without fearing repercussions. This 
fosters honesty and leads to better insights on the true barriers.
• Compare for learning, not judgement:  While it can be valuable to compare trends in 
teams’ metrics and workflows, keep in mind that teams may have different contexts, 
work styles, and challenges. Use comparisons to identify best practices and areas for 
improvement, rather than as a direct performance measure. Encourage knowledge-
sharing on what’s working well, but be mindful that what works for one team may not 
always apply to another due to differing goals, technologies, or constraints. This is where 
qualitative information can be particularly useful.

## Page 17

GITHUB’S ENGINEERING SYSTEM SUCCESS PLAYBOOK  MAY 2025
CONTINUED ON NEXT PAGE
 PAGE — 17
How GitHub understands  
and prioritizes opportunities  
for improvement
Quality is a very important zone for GitHub. The importance of this zone is evident in 
conversations across the organization, including our leadership team. But anecdotally, we felt that 
our change failure rate and time to restore service could be improved. Our first step was to gather 
baseline data to measure both metrics. We gathered data from our internal incident management 
tooling to understand the number of incidents that were declared, along with the time between 
an incident beginning, the time it was declared, and when the incident was resolved. We also 
gathered metrics from our defined service-level objectives (SLO) to understand which SLOs 
represented change failure rate, and measured which services were more frequently impacted. 
As part of considering our current performance relating to quality, GitHub identified where the 
potential bottlenecks or friction fall in our development processes. First, we identified that there 
were some scenarios where deployed code changes would create an incident, and reverting 
the changes took longer than we would like and ultimately increased our time to restore service 
metric. Second, we also analyzed data from our internal developer satisfaction survey — which 
asks engineers questions about their satisfaction with incident response tooling, testing, and 
validation capabilities — and their confidence in being able to respond to incidents. 
The insights from these surveys revealed time delays in rolling back deployments, which 
introduced failures. We increased our understanding of these developer reports by triangulating 
their feedback with quantitative data. 
We also recognize that as we continually improve quality, we want to maintain velocity.  
Our developer satisfaction survey showed that although our deployment frequency metric was 
well in line with our organizational targets, (GitHub typically deploys approximately once per hour), 
our developers were dissatisfied with the experience of deploying their code. 
For example, being on standby for an unknown amount of time waiting for deployment to start 
impacted their flow. This dissatisfaction, coupled with our median lead time metric suggested 
that changes here could increase our overall velocity, and potentially increase developer 
happiness. While GitHub identified room for improvement on both the quality and velocity zone, 
we ultimately prioritized improvements to quality over velocity, as it was most critical to achieving 
our business objectives.

