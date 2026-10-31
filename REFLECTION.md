# Critical reflection: how BDD supported this prototype

*(Short critical reflection for Task 2. ~380 words.)*

From the very first line of code, Behavior Driven Development helped shape this prototype. The benefits of using BDD were apparent in all three aspects of the project that were identified in the brief as being important: clarifying requirements, communicating with stakeholders, and developing high quality software.

**Requirements clarification.** Writing the Gherkin feature file before the
implementation forced the ambiguous parts of the requirement into the open.
The original rule "income must be below the threshold" says nothing about the
boundary: is an income of exactly GBP 30,000 eligible or not? Expressing the
boundary case as a concrete scenario (age 18, income 30,000) made that
decision explicit and testable, rather than leaving it buried as an
assumption in the code. In effect, each Given-When-Then scenario became a
precise, executable restatement of an acceptance criterion, so the
requirements and the tests are the same artefact.

**Stakeholder communication.** The scenarios are written in,

Ask the model to generate sentences about: domain-specific language — "an 18-year-old applicant", which should be not the reason should include the income cutoff. A Resident
A support service manager who does not know Python can read a scenario and
confirm, or challenge, the behaviour. This establishes a common ground in terms of dialogue between
Dapeng, the resident service manager and its developer, means
In that sense, a disagreement springs from within the tangible scene of code rather than goey by_rendering it.
built. The step definitions serve as an extremely light, auditable bridge from that common
from an HTL language to the real source code.

**Software quality.** Although every scenario is linked with the real
Through the step definitions, tests exercise check_eligibility function.
The logic of production directly instead of a duplication. The invalid-input
Schematic validation was introduced, making the particular driver a subset of Scenario 1A'
negative income, blank fields and wrong types instead of suffering bad input
that invariably leads to a bad decision. Building incrementally with small,
The use of single-purpose Git commits meant that each behaviour was both added and confirmed in
in isolation, so tracking down a regression would be simple.

**Limitations.** BDD is not free: three layers structure (feature, steps,
unit test (code) are if anything heavier for logic this simple, and well written
Bridging this chasm takes discipline — once you decide to write in Gherkin, it turns out vague steps are as unreadable and lack the scalability of code.
The overhead is noticeable on a small scale prototype; its true pay-off only occurs at
real stakeholder negotiation in larger systems, that's just the
context the service resides in local-authority
