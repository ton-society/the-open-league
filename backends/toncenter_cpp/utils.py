from tonsdk.utils import Address


def to_user_friendly(address: str) -> str:
    return Address(address).to_string(True, True, True)


def to_raw(address: str) -> str:
    return Address(address).to_string(False).upper()
