"""Security-focused tests."""
import pytest
import time
from password_utils import check_password_strength, hash_password, is_common_password


class TestSQLInjectionAttempts:
    
    def test_sql_injection_in_password(self):
        malicious_inputs = [
            "'; DROP TABLE users; --",
            "' OR '1'='1",
            "admin'--",
            "1; DELETE FROM passwords WHERE '1'='1",
        ]
        
        for payload in malicious_inputs:
            try:
                result = check_password_strength(payload)
                assert isinstance(result, str)
                assert result in ["Weak", "Medium", "Strong"]
            except Exception as e:
                pytest.fail(f"Function crashed with SQL injection attempt: {e}")
    
    def test_special_characters_in_password(self):
        special_passwords = [
            "pass\x00word",
            "pass\nword",
            "pass\tword",
            "pass\\word",
            "pass'word",
            'pass"word',
        ]
        
        for password in special_passwords:
            try:
                result = check_password_strength(password)
                assert isinstance(result, str)
            except Exception as e:
                pytest.fail(f"Function crashed with special character: {e}")


class TestTimingAttacks:
    
    def test_hash_timing_consistency(self):
        short_password = "a"
        long_password = "a" * 1000
        
        start = time.perf_counter()
        for _ in range(100):
            hash_password(short_password)
        short_time = time.perf_counter() - start
        
        start = time.perf_counter()
        for _ in range(100):
            hash_password(long_password)
        long_time = time.perf_counter() - start
        
        assert long_time < short_time * 10
    
    def test_common_password_check_timing(self):
        first_password = "123456"
        last_password = "qwerty123"
        
        start = time.perf_counter()
        for _ in range(1000):
            is_common_password(first_password)
        first_time = time.perf_counter() - start
        
        start = time.perf_counter()
        for _ in range(1000):
            is_common_password(last_password)
        last_time = time.perf_counter() - start
        
        assert abs(first_time - last_time) < first_time * 2


if __name__ == "__main__":
    print("Z6: Testy bezpieczeństwa - SQL Injection")
    sql_tests = TestSQLInjectionAttempts()
    
    print("Testowanie prób SQL injection...")
    try:
        sql_tests.test_sql_injection_in_password()
        print("✓ Test SQL injection")
    except Exception as e:
        print(f"✗ Test SQL injection nieudany: {e}")
    
    print("\nTestowanie znaków specjalnych...")
    try:
        sql_tests.test_special_characters_in_password()
        print("✓ Test znaków specjalnych zaliczony - wszystkie obsłużone bezpiecznie")
    except Exception as e:
        print(f"✗ Test znaków specjalnych nieudany: {e}")
    
    print("\nZ7: Testy timing attacks")
    timing_tests = TestTimingAttacks()
    
    print("Testowanie spójności czasu hashowania...")
    try:
        timing_tests.test_hash_timing_consistency()
        print("✓ Bezpieczne przed timing attack w hashowaniu")
    except AssertionError:
        print("✗ Ostrzeżenie: Potencjalna podatność na timing attack w hashowaniu")
    
    print("\nTestowanie czasu sprawdzania popularnych haseł...")
    try:
        timing_tests.test_common_password_check_timing()
        print("✓ Bezpieczne przed timing attack w sprawdzaniu haseł")
    except AssertionError:
        print("✗ Ostrzeżenie: Potencjalny timing attack w sprawdzaniu haseł")
    
    print("\n" + "="*50)
    print("Testy bezpieczeństwa zakończone!")
    print("="*50)
