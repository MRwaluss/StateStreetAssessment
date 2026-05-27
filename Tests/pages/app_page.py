from playwright.sync_api import Page, Locator

class AppPage:
    def __init__(self, page: Page):
        self.page: Page = page
        self.security_name_input: Locator = self.page.get_by_label("Security name")
        self.total_asset_value_input: Locator = self.page.get_by_label("Total asset value")
        self.target_allocation_input: Locator = self.page.get_by_label("Target allocation (%)")
        self.current_allocation_input: Locator = self.page.get_by_label("Current allocation (%)")
        self.unit_price_input: Locator = self.page.get_by_label("Unit price")
        self.calculate_button: Locator = self.page.get_by_role("button", name="Calculate")
        self.calculation_result: Locator = self.page.get_by_test_id("stAlertContentInfo")

    def open(self) -> None:
        self.page.goto("http://localhost:8888")

    def fill_security_name(self, security_name: str) -> None:
        self.security_name_input.fill(security_name)

    def fill_total_asset_value(self, total_asset_value: float) -> None:
        self.total_asset_value_input.fill(str(total_asset_value))
    
    def fill_target_allocation(self, target_allocation: float) -> None:
        self.target_allocation_input.fill(str(target_allocation))
    
    def fill_current_allocation(self, current_allocation: float) -> None:
        self.current_allocation_input.fill(str(current_allocation))
            
    def fill_unit_price(self, unit_price: float) -> None:
        self.unit_price_input.fill(str(unit_price))

    def click_calculate(self) -> None:
        self.calculate_button.click()

    def get_calculation_result(self) -> str:
        self.calculation_result.wait_for(state="visible")
        return self.calculation_result.inner_text()