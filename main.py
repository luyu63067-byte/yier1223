"""读取练习 CSV，并汇总数量和销售额；仅使用 Python 标准库。"""

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path


def summarize(path: Path) -> tuple[int, int, Decimal]:
    orders = 0
    quantity = 0
    revenue = Decimal("0")
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        required = {"product", "quantity", "unit_price"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV 必须包含 product、quantity、unit_price 三列。")
        for line_number, row in enumerate(reader, start=2):
            try:
                count = int(row["quantity"])
                price = Decimal(row["unit_price"])
                if count < 0 or not price.is_finite() or price < 0:
                    raise ValueError
            except (TypeError, ValueError, InvalidOperation) as error:
                raise ValueError(f"第 {line_number} 行的数量或价格无效。") from error
            orders += 1
            quantity += count
            revenue += count * price
    return orders, quantity, revenue


def main() -> None:
    parser = argparse.ArgumentParser(description="读取 CSV 并汇总销售数据")
    parser.add_argument("csv_path", nargs="?", type=Path,
                        default=Path(__file__).parent / "data" / "sample.csv")
    args = parser.parse_args()
    try:
        orders, quantity, revenue = summarize(args.csv_path)
    except (OSError, ValueError) as error:
        parser.exit(1, f"读取失败：{error}\n")
    print(f"订单数量：{orders}")
    print(f"商品数量：{quantity}")
    print(f"销售总额：{revenue:.2f} 元")


if __name__ == "__main__":
    main()
