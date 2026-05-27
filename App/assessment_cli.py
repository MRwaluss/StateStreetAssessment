from enum import Enum
import argparse

class Action(Enum):
    BUY = "Buy"
    SELL = "Sell"
    NOTHING = "Nothing"

    def __str__(self):
        return self.value

def validate_inputs(total_asset: int, target: int, current: int, unit_price: int):
    if total_asset <= 0:
        raise ValueError("total_asset must be greater than 0")

    if unit_price <= 0:
        raise ValueError("unit_price must be greater than 0")

    if not (0 <= target <= 100):
        raise ValueError("target must be in range 0-100")

    if not (0 <= current <= 100):
        raise ValueError("current must be in range 0-100")

def calculate_shares(total: int, target: int, current: int, unit_price: int) -> Action | tuple[Action, int]:
    variance: int = current - target
    if variance < 0:
        action = Action.BUY
    elif variance == 0:
        action = Action.NOTHING
    else:
        action = Action.SELL

    shares = round(abs(variance) * total / (100 * unit_price), 2)
    return action, shares

def main():
    parser = argparse.ArgumentParser(description="Rebalancing tool")

    parser.add_argument("--total_asset", type=float, required=True)
    parser.add_argument("--security", type=str, required=True)
    parser.add_argument("--target", type=float, required=True)
    parser.add_argument("--current", type=float, required=True)
    parser.add_argument("--unit_price", type=float, required=True)
    
    args = parser.parse_args()
    
    validate_inputs(args.total_asset,
                    args.target,
                    args.current,
                    args.unit_price)


    action, shares = calculate_shares(
        args.total_asset,
        args.target,
        args.current,
        args.unit_price
    )

    print(f"{args.security} action: {action} number of shares: {shares}")

if __name__ == "__main__":
    main()