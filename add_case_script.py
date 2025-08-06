from testrail_reporter import add_test_case

if __name__ == "__main__":
    section_id = 185
    title = "Test Case Login dengan username dan password valid"
    
    result = add_test_case(
        section_id=section_id,
        title="Test Case Login dengan username dan password valid",
        preconds="User sudah memiliki akun dan berada di halaman login",
        steps="""
        1. Buka halaman login
        2. Masukkan username yang valid
        3. Masukkan password yang valid
        4. Klik tombol 'Login'
        5. Verifikasi berhasil masuk ke halaman dashboard
        """,
        refs="REQ-001"
        )

    if result:
        print("Test case berhasil ditambahkan!")
    else:
        print("Gagal menambahkan test case.")