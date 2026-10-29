Feature: Resident Support eligibility checking
  As a Resident Support service manager
  I want eligibility decisions to be applied consistently and validated
  So that residents receive fair, auditable outcomes and bad data is caught early

  # User story:
  #   As a resident (or a desk officer entering a resident's details),
  #   I want to check whether I qualify for Resident Support,
  #   so that I get a clear, consistent decision with a reason.
  #
  # Acceptance criteria:
  #   - An adult resident whose household income is below the threshold is eligible.
  #   - The age and income limits behave correctly exactly on their boundaries.
  #   - Invalid input (e.g. a negative income) is rejected with a clear error,
  #     rather than producing a misleading decision.

  Scenario: Eligible adult resident on a low income
    Given an applicant aged 35
    And the applicant is a resident of the local authority area
    And the applicant has a household income of 24000
    When the eligibility check is run
    Then the applicant should be eligible

  Scenario: Boundary applicant exactly on the age and income limits
    Given an applicant aged 18
    And the applicant is a resident of the local authority area
    And the applicant has a household income of 30000
    When the eligibility check is run
    Then the applicant should be not eligible
    And the reason should mention the income threshold

  Scenario: Invalid input is rejected gracefully
    Given an applicant aged 40
    And the applicant is a resident of the local authority area
    And the applicant has a household income of -500
    When the eligibility check is run
    Then the service should report an input error
    And the error message should mention "negative"
