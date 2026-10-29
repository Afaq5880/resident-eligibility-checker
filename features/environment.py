"""
behave environment hooks.

Kept intentionally light for a prototype: we simply make sure each scenario
starts from a clean slate so that state from one scenario can never leak into
another and give a misleading result.
"""


def before_scenario(context, scenario):
    # Clear any per-scenario state before each scenario runs.
    context.age = None
    context.income = None
    context.is_resident = None
    context.result = None
    context.error = None
