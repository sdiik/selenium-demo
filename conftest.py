import pytest
from testrail_reporter import add_result_for_case

def pytest_runtest_makereport(item, call):
    if call.when == "call":  # hanya setelah test case selesai
        case_id = getattr(item.function, "testrail_case_id", None)
        if case_id:
            # call.excinfo None = test passed; else failed
            status_id = 1 if call.excinfo is None else 5
            comment = "Test passed." if status_id == 1 else f"Test failed: {call.excinfo.value}"
            add_result_for_case(case_id[1:], status_id, comment)  # hapus "C" dari "C123"
