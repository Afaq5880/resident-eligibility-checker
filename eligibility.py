"""
Resident Support Eligibility Checker
------------------------------------

Core domain logic for a resident-facing local-authority service.

The service decides whether a resident qualifies for a Resident Support
hardship grant. It is deliberately small, but the rules and the input
validation are written to be unambiguous and auditable, so that the same
inputs always produce the same documented decision.

Business rules (as agreed with the Resident Support service manager):
  1. The applicant must be at least 18 years old.
  2. The applicant must be a resident of the local authority area.
  3. The applicant's household income must be BELOW the income threshold
     (strictly less than GBP 30,000).

An applicant is eligible only if all three rules are satisfied.

Invalid input (missing fields, wrong types, impossible values such as a
negative income) is rejected with a clear EligibilityError rather than
being allowed to produce a misleading decision.
"""

from dataclasses import dataclass

# --- Configuration -----------------------------------------------------------

MIN_AGE = 18
MAX_AGE = 120           # sanity ceiling to reject impossible ages
INCOME_THRESHOLD = 30000  # GBP; household income must be strictly below this


# --- Errors ------------------------------------------------------------------

class EligibilityError(ValueError):
    """Raised when the inputs to an eligibility check are invalid."""


# --- Result type -------------------------------------------------------------

@dataclass
class EligibilityResult:
    """The outcome of an eligibility decision."""
    eligible: bool
    reason: str

    def __str__(self) -> str:  # pragma: no cover - convenience only
        status = "ELIGIBLE" if self.eligible else "NOT ELIGIBLE"
        return f"{status}: {self.reason}"


# --- Validation --------------------------------------------------------------

def _validate(age, household_income, is_resident) -> None:
    """Validate raw inputs, raising EligibilityError on any problem."""
    if age is None or household_income is None or is_resident is None:
        raise EligibilityError(
            "All fields are required: age, household income and residency."
        )

    # bool is a subclass of int in Python, so guard against True/False slipping
    # through as an age or an income.
    if isinstance(age, bool) or not isinstance(age, int):
        raise EligibilityError("Age must be a whole number.")
    if age < 0:
        raise EligibilityError("Age cannot be negative.")
    if age > MAX_AGE:
        raise EligibilityError(f"Age cannot be greater than {MAX_AGE}.")

    if isinstance(household_income, bool) or not isinstance(household_income, (int, float)):
        raise EligibilityError("Household income must be a number.")
    if household_income < 0:
        raise EligibilityError("Household income cannot be negative.")

    if not isinstance(is_resident, bool):
        raise EligibilityError("Residency must be either true or false.")


# --- Core decision -----------------------------------------------------------

def check_eligibility(age, household_income, is_resident) -> EligibilityResult:
    """
    Decide whether an applicant qualifies for Resident Support.

    Args:
        age: applicant's age in whole years.
        household_income: total household income in GBP.
        is_resident: True if the applicant lives in the local authority area.

    Returns:
        EligibilityResult with .eligible (bool) and a human-readable .reason.

    Raises:
        EligibilityError: if any input is missing, the wrong type, or an
                          impossible value.
    """
    _validate(age, household_income, is_resident)

    failures = []
    if age < MIN_AGE:
        failures.append(f"applicant must be at least {MIN_AGE}")
    if not is_resident:
        failures.append("applicant must be a resident of the local authority area")
    if household_income >= INCOME_THRESHOLD:
        failures.append(
            f"household income must be below GBP {INCOME_THRESHOLD:,}"
        )

    if failures:
        return EligibilityResult(
            eligible=False,
            reason="Not eligible because " + "; ".join(failures) + ".",
        )

    return EligibilityResult(
        eligible=True,
        reason="All criteria met: applicant qualifies for Resident Support.",
    )


# --- Simple manual entry point ----------------------------------------------
# Lets the prototype be driven from the command line as well as from the BDD
# tests, which is useful when capturing evidence or demonstrating to a
# stakeholder.

def _prompt() -> None:  # pragma: no cover - interactive helper
    print("Resident Support Eligibility Checker")
    print("-" * 36)
    try:
        age = int(input("Applicant age (whole years): ").strip())
        income = float(input("Household income (GBP): ").strip())
        resident_raw = input("Resident of the area? (y/n): ").strip().lower()
        is_resident = resident_raw in ("y", "yes", "true", "1")
        result = check_eligibility(age, income, is_resident)
        print()
        print(result)
    except EligibilityError as exc:
        print()
        print(f"Input error: {exc}")
    except ValueError:
        print()
        print("Input error: age must be a whole number and income a number.")


if __name__ == "__main__":  # pragma: no cover
    _prompt()
