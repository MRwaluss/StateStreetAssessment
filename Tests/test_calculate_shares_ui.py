

import allure
from assertpy import assert_that
import pytest

from Tests.pages.app_page import AppPage
from Tests.utils import load_csv_data


class TestCalculateSharesUI:
    
    @pytest.mark.parametrize(
    (
        "total_asset",
        "security",
        "target",
        "current",
        "unit_price",
        "expected_output",
    ),
        load_csv_data("happy_path.csv"),
    indirect=[
        "total_asset",
        "security",
        "target",
        "current",
    ]
    )
    def test_application_ui_happy_path(
        self,
        total_asset: float,
        security: str,
        target: float,
        current: float,
        unit_price: float,
        expected_output: str,
        login_page: AppPage,
    ):
        with allure.step("Fill all necessary input boxes"):
            login_page.fill_security_name(security)
            login_page.fill_total_asset_value(total_asset)
            login_page.fill_target_allocation(target)
            login_page.fill_current_allocation(current)
            login_page.fill_unit_price(unit_price)
        
        with allure.step("Click calculates button"):
            login_page.click_calculate()
        
        with allure.step("Validating UI application output"):
            output = login_page.get_calculation_result()
            assert_that(output, "Expected output not found").contains(expected_output) 