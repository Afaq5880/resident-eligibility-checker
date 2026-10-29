# Critical reflection: how BDD supported this prototype

*(Short critical reflection for Task 2. ~380 words.)*

Behaviour-Driven Development shaped this prototype from the first line of
code, and its value showed up in three areas the brief asks about:
requirements clarification, stakeholder communication, and software quality.

**Requirements clarification.** Writing the Gherkin feature file *before* the
implementation forced the ambiguous parts of the requirement into the open.
The original rule "income must be below the threshold" says nothing about the
boundary: is an income of exactly GBP 30,000 eligible or not? Expressing the
boundary case as a concrete scenario (age 18, income 30,000) made that
decision explicit and testable, rather than leaving it buried as an
assumption in the code. In effect, each `Given-When-Then` scenario became a
precise, executable restatement of an acceptance criterion, so the
requirements and the tests are the same artefact.

**Stakeholder communication.** The scenarios are written in plain,
domain-focused language — "an applicant aged 18", "the applicant should be not
eligible", "the reason should mention the income threshold". A Resident
Support service manager who cannot read Python can still read a scenario and
confirm, or challenge, the behaviour. This creates a shared vocabulary between
the resident, the service manager and the developer, and it means
disagreements surface over a readable scenario rather than after the code is
built. The step definitions act as a thin, auditable bridge from that shared
language to the actual source code.

**Software quality.** Because every scenario is tied to the real
`check_eligibility` function through the step definitions, the tests exercise
the production logic directly rather than a copy of it. The invalid-input
scenario in particular pushed me to add explicit validation (rejecting a
negative income, missing fields and wrong types) instead of letting bad data
flow through to a misleading decision. Building incrementally with small,
single-purpose Git commits meant each behaviour was added and verified in
isolation, so a regression would be easy to locate.

**Limitations.** BDD is not free: the three-layer structure (feature, steps,
code) is heavier than a unit test for logic this simple, and well-written
Gherkin takes discipline — vague steps quickly become as unreadable as code.
For a small prototype the overhead is noticeable; its real payoff comes on
larger systems with genuine stakeholder negotiation, which is exactly the
local-authority context this service sits in.
