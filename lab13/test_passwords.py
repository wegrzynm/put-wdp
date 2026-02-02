"""Unit tests for password_utils module."""
# pylint: disable=redefined-outer-name
import pytest
from password_utils import (check_password_strength, hash_password,
                            is_common_password, validate_password)


def test_weak_password():
    """Test that short password is classified as Weak."""
    assert check_password_strength("abc") == "Weak"

def test_strong_password():
    """Test that complex password is classified as Strong."""
    assert check_password_strength("MyStr0ng!Pass2024") == "Strong"


def test_empty_password_raises_error():
    """Test that empty password raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        check_password_strength("")
    assert "empty" in str(exc_info.value).lower()

def test_none_password_raises_error():
    """Test that None password raises ValueError."""
    with pytest.raises(ValueError):
        check_password_strength(None)


def test_sha256_hash_length():
    """Test that SHA-256 hash has correct length (64 characters)."""
    result = hash_password("test123")
    assert len(result) == 64

def test_sha512_hash_length():
    """Test that SHA-512 hash has correct length (128 characters)."""
    result = hash_password("test123", "sha512")
    assert len(result) == 128

def test_same_password_same_hash():
    """Test that same password always produces same hash."""
    hash1 = hash_password("mypassword")
    hash2 = hash_password("mypassword")
    assert hash1 == hash2

def test_different_passwords_different_hashes():
    """Test that different passwords produce different hashes."""
    hash1 = hash_password("password1")
    hash2 = hash_password("password2")
    assert hash1 != hash2

def test_unsupported_algorithm_raises_error():
    """Test that unsupported algorithm raises ValueError."""
    with pytest.raises(ValueError):
        hash_password("test123", "sha1")


def test_common_password_detected():
    """Test that common passwords are detected."""
    assert is_common_password("123456")
    assert is_common_password("password")
    assert is_common_password("qwerty")

def test_uncommon_password_not_detected():
    """Test that unique passwords are not flagged as common."""
    assert not is_common_password("MyUniqueP@ssw0rd2024")

def test_common_password_case_insensitive():
    """Test that common password check is case insensitive."""
    assert is_common_password("PASSWORD")
    assert is_common_password("Password")


def test_valid_password():
    """Test that valid password passes all checks."""
    result = validate_password("SecurePass123!")
    assert result['valid']
    assert not result['errors']

def test_too_short_password():
    """Test that short password fails validation."""
    result = validate_password("Short1!")
    assert not result['valid']
    assert any("8 characters" in error for error in result['errors'])

def test_common_password_fails():
    """Test that common password fails validation."""
    result = validate_password("password1")
    assert result['is_common']


def test_md5_hash():
    """Test MD5 hash algorithm."""
    result = hash_password("test123", "md5")
    assert len(result) == 32


def test_md5_hash_length():
    """Test that MD5 hash has correct length (32 characters)."""
    result = hash_password("password", "md5")
    assert len(result) == 32


def test_generate_password_hash_no_salt():
    """Test generate_password_hash without salt."""
    from password_utils import generate_password_hash
    result = generate_password_hash("mypassword")
    assert len(result) == 64
    assert isinstance(result, str)


def test_generate_password_hash_with_salt():
    """Test generate_password_hash with salt."""
    from password_utils import generate_password_hash
    result1 = generate_password_hash("mypassword", "salt123")
    result2 = generate_password_hash("mypassword", "salt456")
    assert len(result1) == 64
    assert len(result2) == 64
    assert result1 != result2


def test_generate_password_hash_same_salt_same_hash():
    """Test that same password and salt produces same hash."""
    from password_utils import generate_password_hash
    result1 = generate_password_hash("password", "mysalt")
    result2 = generate_password_hash("password", "mysalt")
    assert result1 == result2


def test_hash_password_empty_raises_error():
    """Test that empty password raises ValueError in hash_password."""
    with pytest.raises(ValueError):
        hash_password("")


def test_validate_password_empty():
    """Test that empty password is handled correctly."""
    result = validate_password("")
    assert not result['valid']
    assert "empty" in result['errors'][0].lower()


def test_validate_password_none():
    """Test that None password is handled correctly."""
    result = validate_password(None)
    assert not result['valid']


@pytest.mark.parametrize("password,expected", [
    ("abc", "Weak"),
    ("12345", "Weak"),
    ("short", "Weak"),
    ("abcdefgh", "Weak"),
    ("Abcdefgh", "Medium"),
    ("Abcdefgh1", "Medium"),
    ("abcdefgh12", "Medium"),
    ("MyStr0ng!Pass", "Strong"),
    ("Complex!Pass123", "Strong"),
    ("VerySecure@2024!", "Strong"),
    ("Minimum8", "Medium"),
    ("Exactly12Chr", "Strong"),
    ("SixteenChars!!!!", "Strong"),
    ("a", "Weak"),
    ("A1b2C3d4E5f6", "Strong"),
])
def test_password_strength_parametrized(password, expected):
    """Test password strength with multiple inputs."""
    assert check_password_strength(password) == expected


@pytest.fixture(name='test_passwords')
def sample_passwords_fixture():
    """Provide sample passwords for testing."""
    return {
        'weak': ['abc', '123', 'pass', 'short', 'lower'],
        'medium': ['Password', 'Abcdefgh', 'abcd1234', 'Short123'],
        'strong': ['MyStr0ng!Pass2024', 'C0mpl3x!P@ssw0rd',
                   'Secure$Pass2024!', 'VeryL0ng&Complex']
    }


@pytest.fixture(name='common_list')
def common_passwords_list_fixture():
    """Provide list of known common passwords."""
    return ["123456", "password", "qwerty", "admin", "letmein", "welcome"]


def test_weak_passwords_with_fixture(test_passwords):
    """Test all weak passwords from fixture."""
    for password in test_passwords['weak']:
        assert check_password_strength(password) == "Weak"

def test_medium_passwords_with_fixture(test_passwords):
    """Test all medium passwords from fixture."""
    for password in test_passwords['medium']:
        assert check_password_strength(password) == "Medium"

def test_strong_passwords_with_fixture(test_passwords):
    """Test all strong passwords from fixture."""
    for password in test_passwords['strong']:
        assert check_password_strength(password) == "Strong"

def test_all_common_passwords_detected(common_list):
    """Test that all common passwords are detected."""
    for password in common_list:
        assert is_common_password(password)

def test_validate_with_fixtures(test_passwords):
    """Test validate_password with fixture data."""
    for password in test_passwords['strong']:
        result = validate_password(password)
        assert result['valid']
        assert not result['is_common']


if __name__ == "__main__":
    print("=" * 60)
    print("PRZYKŁADY - ZADANIA ROZSZERZONE")
    print("=" * 60)

    print("\nZ10: Parametryzacja testów (@pytest.mark.parametrize)")
    print("-" * 60)
    print("Testowanie wielu przypadków jedną funkcją testową:\n")

    example_cases = [
        ("abc", "Weak"),
        ("abcdefgh", "Weak"),
        ("Abcdefgh", "Medium"),
        ("MyStr0ng!Pass", "Strong"),
        ("Exactly12Chr", "Strong"),
    ]

    for pwd, expected_strength in example_cases:
        result = check_password_strength(pwd)
        status = "✓" if result == expected_strength else "✗"
        print(f"{status} '{pwd}': {result} (oczekiwano: {expected_strength})")

    print("\nZ11: Testy fixtures (współdzielenie danych testowych)")
    print("-" * 60)
    print("Używanie fixtures do grupowania danych testowych:\n")

    example_data = {
        'weak': ['abc', '123', 'pass'],
        'medium': ['Password', 'Abcdefgh'],
        'strong': ['MyStr0ng!Pass2024', 'C0mpl3x!P@ssw0rd']
    }

    print("Fixture: sample_passwords")
    for category, password_list in example_data.items():
        print(f"\n  Kategoria '{category}':")
        for pwd in password_list:
            strength = check_password_strength(pwd)
            status = "✓" if strength.lower() == category.lower() else "✗"
            print(f"    {status} '{pwd}': {strength}")

    print("\nFixture: common_passwords_list")
    example_common = ["123456", "password", "qwerty", "admin"]
    for pwd in example_common:
        is_common = is_common_password(pwd)
        status = "✓" if is_common else "✗"
        print(f"  {status} '{pwd}': {'TAK' if is_common else 'NIE'}")
