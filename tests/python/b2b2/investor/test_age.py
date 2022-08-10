from renlife_b2b_test import age
from renlife_b2b_test.controls import policy_calculate_ui
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from tests.python.b2b2.investor.vznos.investor_ubrir_min_max_vznos import precondition

def precondition_sum():
    precondition()
    policy_calculate_ui.UI(100000)

def test_age_minimal():
    precondition_sum()
    age.age_minimal(18)

def test_age_minimal_minus_1():
    precondition_sum()
    age.age_18_minus_1_day(18)

def test_age_minimal_plus_1():
    precondition_sum()
    age.age_18_plus_1_day(18)