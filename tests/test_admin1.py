from datetime import datetime

from hdx.database.views import build_view

from hapi_schema.db_admin1 import DBAdmin1, view_params_admin1


def test_admin1_view(run_view_test):
    """Check that admin1 view references location."""
    view_admin1 = build_view(view_params_admin1.__dict__)
    run_view_test(
        view=view_admin1,
        whereclause=(
            view_admin1.c.id == 1,
            view_admin1.c.location_code == "FOO",
        ),
    )


def test_admin1_reference_period_constraint(run_constraints_test):
    """Check that reference_period_end cannot be less than start"""
    run_constraints_test(
        new_row=DBAdmin1(
            location_ref=1,
            code="FOO-003",
            name="Province 3",
            is_unspecified=False,
            reference_period_start=datetime(2023, 1, 2),
            reference_period_end=datetime(2023, 1, 1),
            hapi_updated_date=datetime(2023, 1, 1),
            hapi_replaced_date=None,
        ),
        expected_constraint="reference_period",
    )
