from pathlib import Path
import subprocess
from typing import List

import pytest
from assertpy import assert_that
from Tests.utils import load_csv_data, prettify_error_output
import allure

class TestCalculateShares:
    
    def run_process(self, command: List[str]) -> str:
        result = subprocess.run(command, capture_output=True, text=True)
        std_out = result.stdout.strip()
        std_err = result.stderr.strip()
        if std_err:
            output = prettify_error_output(std_err)
        else:
            output = std_out
        return output
    
    @allure.title("Test Application CLI - Happy Path")
    @allure.description("Test to check if given values are calculated properly")
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
    def test_application_cli_happy_path(
        self,
        total_asset: float,
        security: str,
        target: float,
        current: float,
        unit_price: float,
        expected_output: str,
        run_command: List[str],
    ):
        with allure.step("Validating application output"):
            output = self.run_process(run_command)
            assert_that(output, "Expected output not found").contains(expected_output)
    
    @allure.title("Test Application CLI - Invalid Types")
    @allure.description("Test to check if application properly handle wrong types")
    @pytest.mark.parametrize(
    (
        "total_asset",
        "security",
        "target",
        "current",
        "unit_price",
        "expected_output",
    ),
        load_csv_data("invalid_types.csv"),
    indirect=[
        "total_asset",
        "security",
        "target",
        "current",
    ]
    )
    def test_application_cli_invalid_types(
        self,
        total_asset: float,
        security: str,
        target: float,
        current: float,
        unit_price: float,
        expected_output: str,
        run_command: List[str],
    ):
        with allure.step("Validating application output"):
            output = self.run_process(run_command)
            assert_that(output, "Expected output not found").contains(expected_output)
    
    @allure.title("Test Application CLI - Large Values")
    @allure.description("Test to check if application properly calculate large values")
    @pytest.mark.parametrize(
    (
        "total_asset",
        "security",
        "target",
        "current",
        "unit_price",
        "expected_output",
    ),
        load_csv_data("large_values.csv"),
    indirect=[
        "total_asset",
        "security",
        "target",
        "current",
    ]
    )
    def test_application_cli_large_values(
        self,
        total_asset: float,
        security: str,
        target: float,
        current: float,
        unit_price: float,
        expected_output: str,
        run_command: List[str],
    ):
        with allure.step("Validating application output"):
            output = self.run_process(run_command)
            assert_that(output, "Expected output not found").contains(expected_output)
    
    @allure.title("Test Application CLI - Validation Errors")
    @allure.description("Test to check if application properly handle wrongly passed argument ranges")
    @pytest.mark.parametrize(
    (
        "total_asset",
        "security",
        "target",
        "current",
        "unit_price",
        "expected_output",
    ),
        load_csv_data("validation_errors.csv"),
    indirect=[
        "total_asset",
        "security",
        "target",
        "current",
    ]
    )
    def test_application_cli_validation_errors(
        self,
        total_asset: float,
        security: str,
        target: float,
        current: float,
        unit_price: float,
        expected_output: str,
        run_command: List[str],
    ):
        with allure.step("Validating application output"):
            output = self.run_process(run_command)
            assert_that(output, "Expected output not found").contains(expected_output)
    
    @allure.title("Test Application CLI - Consistent Data")
    @allure.description("Test to check if application returning always the same data")
    @pytest.mark.parametrize(
    (
        "total_asset",
        "security",
        "target",
        "current",
        "unit_price",
        "expected_output",
    ),
        [("100000","IBM","20","10","150","IBM action: Buy number of shares: 66.67")],
    indirect=[
        "total_asset",
        "security",
        "target",
        "current",
    ]
    )     
    def test_returns_consistent_data(
        self,
        total_asset: float,
        security: str,
        target: float,
        current: float,
        unit_price: float,
        expected_output: str,
        run_command: List[str],):
        app_outputs = []
        with allure.step("Run Application CLI 5 times and validating application output"):
            for _ in range (0, 5):
                output = self.run_process(run_command)
                app_outputs.append(output)
            assert_that(len(set(app_outputs)), "Output data are not the same after each run").is_less_than_or_equal_to(1)
        
    @allure.title("Test Application CLI - Wrong Argument")
    @allure.description("Test to check if handle wrongly passed argument")
    @pytest.mark.parametrize("expected_output", ("the following arguments are required",))
    def test_application_cli_wrong_argument(self, expected_output: str, python_executable: str, main_cli_app_filepath: Path):
        with allure.step("Run Application CLI with wrong argument"):
            command = [python_executable, main_cli_app_filepath, "--count"]
            output = self.run_process(command)
            assert_that(output, "Expected output not found").contains(expected_output)