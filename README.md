# Resident Support Eligibility Checker

A small Python prototype for a local-authority resident-facing service,
developed using **Behaviour-Driven Development (BDD)** with the
[`behave`](https://behave.readthedocs.io/) framework.

This repository is the practical artefact for **Task 2** of the Agile
Programming assignment: an Agile requirements and testing demonstration.

---

## 1. Prototype description

The service decides whether a resident qualifies for a **Resident Support**
hardship grant. It is deliberately small, but the rules and input validation
are written to be unambiguous and auditable, so that the same inputs always
produce the same documented decision.

**Business rules** (agreed with the Resident Support service manager):

1. The applicant must be at least **18** years old.
2. The applicant must be a **resident** of the local authority area.
3. The applicant's **household income must be below GBP 30,000** (strictly).

An applicant is eligible only if **all three** rules are met. Invalid input
(missing fields, wrong types, or impossible values such as a negative income)
is rejected with a clear error rather than producing a misleading decision.

## 2. Main user / stakeholder and the problem it solves

- **Primary user:** a resident, or a front-desk officer entering a resident's
  details on their behalf.
- **Key stakeholder:** the **Resident Support service manager**, who is
  accountable for consistent, fair and auditable decisions.
- **Problem solved:** previously, eligibility was judged manually and
  inconsistently. This prototype encodes the agreed rules once, so every
  applicant is assessed the same way and every decision comes with a reason.

## 3. User story and acceptance criteria

> **As a** resident (or a desk officer entering a resident's details),
> **I want** to check whether I qualify for Resident Support,
> **so that** I get a clear, consistent decision with a reason.

**Acceptance criteria**

- An adult resident whose household income is below the threshold is **eligible**.
- The age and income limits behave correctly **exactly on their boundaries**
  (age 18 passes; income of exactly 30,000 fails).
- **Invalid input** (e.g. a negative income) is rejected with a clear error,
  rather than producing a misleading decision.

## 4. Project structure

```
resident-eligibility-checker/
├── eligibility.py                  # Core logic + input validation
├── behave.ini                      # behave configuration
├── requirements.txt                # Dependencies (behave)
├── README.md                       # This file
├── REFLECTION.md                   # Critical reflection on BDD
├── .gitignore
├── features/
│   ├── eligibility.feature         # Gherkin scenarios (BDD)
│   ├── environment.py              # Per-scenario setup hooks
│   └── steps/
│       └── eligibility_steps.py    # Step definitions (Gherkin -> code)
└── evidence/
    ├── passing_run.txt / .png      # Terminal evidence: all scenarios pass
    ├── failing_run.txt / .png      # Terminal evidence: a deliberate failure
    └── git_log.txt                 # Evidence of incremental commit history
```

## 5. How to set up and run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the BDD test suite
behave

# (optional) run the prototype interactively
python eligibility.py
```

A successful run reports **3 scenarios passed** and all steps passing.

## 6. The BDD scenarios

| # | Scenario | Type | Expected outcome |
|---|----------|------|------------------|
| 1 | Eligible adult resident on a low income | Success | Eligible |
| 2 | Boundary applicant exactly on age and income limits | Boundary | Not eligible (income) |
| 3 | Invalid input is rejected gracefully | Invalid input | Input error raised |

## 6a. Traceability: requirement → scenario → step → code

This mapping shows that each acceptance criterion is exercised by a scenario,
which is wired through a step definition to the real production code.

| Acceptance criterion | Gherkin scenario | Step definition | Code under test |
|---|---|---|---|
| Adult resident below threshold is eligible | Scenario 1 | `step_run_check` → `step_expect_eligible` | `check_eligibility()` |
| Age 18 passes; income of exactly 30,000 fails | Scenario 2 | `step_run_check` → `step_expect_not_eligible`, `step_reason_mentions_income` | `check_eligibility()` rule checks |
| Invalid input (negative income) is rejected gracefully | Scenario 3 | `step_run_check` → `step_expect_error`, `step_error_mentions` | `_validate()` raising `EligibilityError` |

The step definitions import and call `check_eligibility` directly, so the
tests exercise the actual prototype logic rather than a copy of it.

## 7. Git history

The prototype was built **incrementally**, one concern per commit. See
`evidence/git_log.txt` for the full history, or run `git log --oneline`.

> **Repository link:** _add your GitHub URL here after pushing_, e.g.
> `https://github.com/<your-username>/resident-eligibility-checker`

Push instructions are in Section 8.

## 8. Publishing to GitHub (to get your repo link)

```bash
# create an EMPTY repo on github.com first (no README), then:
git remote add origin https://github.com/<your-username>/resident-eligibility-checker.git
git branch -M main
git push -u origin main
```

Then paste the resulting URL into Section 7 above and into your report.
