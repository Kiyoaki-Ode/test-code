"""
シンプルな計算機アプリ
四則演算（加算・減算・乗算・除算）をサポートします。
"""


def add(a: float, b: float) -> float:
    """加算"""
    return a + b


def subtract(a: float, b: float) -> float:
    """減算"""
    return a - b


def multiply(a: float, b: float) -> float:
    """乗算"""
    return a * b


def divide(a: float, b: float) -> float:
    """除算（ゼロ除算チェックあり）"""
    if b == 0:
        raise ValueError("ゼロで割ることはできません。")
    return a / b


def calculate(expression: str) -> float:
    """
    文字列式を解析して計算する。
    対応する演算子: +, -, *, /
    例: "3 + 5", "10 / 2"
    """
    expression = expression.strip()
    for op in ["+", "-", "*", "/"]:
        if op in expression:
            parts = expression.split(op, 1)
            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())
                except ValueError:
                    raise ValueError(f"無効な数値が含まれています: '{expression}'")
                if op == "+":
                    return add(a, b)
                elif op == "-":
                    return subtract(a, b)
                elif op == "*":
                    return multiply(a, b)
                elif op == "/":
                    return divide(a, b)
    raise ValueError(f"無効な式です: '{expression}'")


def main():
    """メインループ: インタラクティブな計算機"""
    print("===== シンプル計算機 =====")
    print("使い方: 数値 演算子 数値 (例: 3 + 5)")
    print("演算子: + (加算), - (減算), * (乗算), / (除算)")
    print("終了するには 'q' または 'quit' を入力してください。")
    print("=" * 26)

    while True:
        user_input = input("\n計算式を入力: ").strip()

        if user_input.lower() in ("q", "quit", "exit"):
            print("計算機を終了します。")
            break

        if not user_input:
            continue

        try:
            result = calculate(user_input)
            # 整数で表せる場合はint表示
            if result == int(result):
                print(f"結果: {int(result)}")
            else:
                print(f"結果: {result}")
        except ValueError as e:
            print(f"エラー: {e}")


if __name__ == "__main__":
    main()
