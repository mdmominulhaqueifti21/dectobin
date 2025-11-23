def decimal_to_binary(n):
    """
    Converts a decimal number to binary string.
    :param n: int or float
    :return: str
    """
    if isinstance(n, int):
        return bin(n)[2:]
    elif isinstance(n, float):
        whole, frac = str(n).split(".")
        whole_bin = bin(int(whole))[2:]
        frac_bin = ""
        frac = float("0." + frac)
        for _ in range(10):  # 10-bit precision for fraction
            frac *= 2
            bit = int(frac)
            frac_bin += str(bit)
            frac -= bit
        return f"{whole_bin}.{frac_bin}"
    else:
        raise TypeError("Input must be int or float")
