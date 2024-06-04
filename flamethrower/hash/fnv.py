K_OFFSET_32 = 5381
K_OFFSET_64 = 14695981039346656037

K_PRIME_32 = 33
K_PRIME_64 = 1099511628211


def fnv1_32_hash(data: bytes):
    """
    FNV-1 32-bit hash function.

    Args:
        data (bytes): Data to hash.

    Returns:
        int: Hash value.
    """
    hash_value = K_OFFSET_32

    for byte in data:
        hash_value = (hash_value * K_PRIME_32) ^ byte

    return hash_value & 0xFFFFFFFF


def fnv1a_32_hash(data: bytes):
    """
    FNV-1a 32-bit hash function.

    Args:
        data (bytes): Data to hash.

    Returns:
        int: Hash value.
    """
    hash_value = K_OFFSET_32

    for byte in data:
        hash_value = (hash_value ^ byte) * K_PRIME_32

    return hash_value & 0xFFFFFFFF


def fnv1_64_hash(data: bytes):
    """
    FNV-1 64-bit hash function.

    Args:
        data (bytes): Data to hash.

    Returns:
        int: Hash value.
    """
    hash_value = K_OFFSET_64

    for byte in data:
        hash_value = (hash_value * K_PRIME_64) ^ byte

    return hash_value


def fnv1a_64_hash(data: bytes):
    """
    FNV-1a 64-bit hash function.

    Args:
        data (bytes): Data to hash.

    Returns:
        int: Hash value.
    """
    hash_value = K_OFFSET_64

    for byte in data:
        hash_value = (hash_value ^ byte) * K_PRIME_64

    return hash_value
