"""
Step definitions for the Resident Support eligibility feature.

Each step maps a line of the Gherkin scenario onto the prototype's source
code in eligibility.py, keeping the scenarios, the step definitions and the
implementation aligned.
"""

from behave import given, when, then

from eligibility import check_eligibility, EligibilityError


# --- Given -------------------------------------------------------------------

@given("an applicant aged {age:d}")
def step_set_age(context, age):
    context.age = age


@given("the applicant is a resident of the local authority area")
def step_is_resident(context):
    context.is_resident = True


@given("the applicant is not a resident of the local authority area")
def step_is_not_resident(context):
    context.is_resident = False


@given("the applicant has a household income of {income:d}")
def step_set_income(context, income):
    context.income = income


# --- When --------------------------------------------------------------------

@when("the eligibility check is run")
def step_run_check(context):
    # Reset outcome holders, then run the real prototype logic.
    context.result = None
    context.error = None
    try:
        context.result = check_eligibility(
            context.age, context.income, context.is_resident
        )
    except EligibilityError as exc:
        context.error = str(exc)


# --- Then --------------------------------------------------------------------

@then("the applicant should be eligible")
def step_expect_eligible(context):
    assert context.error is None, f"Unexpected input error: {context.error}"
    assert context.result is not None, "No result was produced."
    assert context.result.eligible is True, (
        f"Expected the applicant to be eligible, but got: {context.result}"
    )


@then("the applicant should be not eligible")
def step_expect_not_eligible(context):
    assert context.error is None, f"Unexpected input error: {context.error}"
    assert context.result is not None, "No result was produced."
    assert context.result.eligible is False, (
        f"Expected the applicant to be not eligible, but got: {context.result}"
    )


@then("the reason should mention the income threshold")
def step_reason_mentions_income(context):
    assert context.result is not None, "No result was produced."
    assert "income" in context.result.reason.lower(), (
        f"Expected the reason to mention income, but got: {context.result.reason}"
    )


@then("the service should report an input error")
def step_expect_error(context):
    assert context.error is not None, (
        "Expected an input error to be reported, but the check succeeded "
        f"with: {context.result}"
    )


@then('the error message should mention "{word}"')
def step_error_mentions(context, word):
    assert context.error is not None, "Expected an input error, but none occurred."
    assert word.lower() in context.error.lower(), (
        f"Expected the error to mention '{word}', but got: {context.error}"
    )
