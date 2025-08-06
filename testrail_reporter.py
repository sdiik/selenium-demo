# testrail_reporter.py
import requests
import os

TESTRAIL_URL = os.getenv("TESTRAIL_URL")
TESTRAIL_EMAIL = os.getenv("TESTRAIL_EMAIL")
TESTRAIL_API_KEY = os.getenv("TESTRAIL_API_KEY")
TESTRAIL_RUN_ID = os.getenv("TESTRAIL_RUN_ID")


auth = (TESTRAIL_EMAIL, TESTRAIL_API_KEY)
   
def add_test_case(section_id, title, template_id=1, type_id=1, priority_id=2, refs=None, preconds=None, steps=None):
    """
    section_id: ID dari Section/folder test case di TestRail
    title: Judul test case
    template_id: Template case ID (default 1)
    type_id: Jenis test case (default 1 - Functional)
    priority_id: Prioritas (default 2 - Medium)
    refs: Referensi (misal: JIRA ID atau Requirement ID)
    preconds: String untuk preconditions
    steps: String untuk test steps

    return: dict JSON response atau None jika gagal
    """
    url = f"{TESTRAIL_URL}index.php?/api/v2/add_case/{section_id}"
    
    payload = {
        "title": title,
        "template_id": template_id,
        "type_id": type_id,
        "priority_id": priority_id,
    }

    if refs:
        payload["refs"] = refs
    if preconds:
        payload["custom_preconds"] = preconds
    if steps:
        payload["custom_steps"] = steps

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, auth=auth, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"✅ Test case '{title}' berhasil ditambahkan di section {section_id}")
        return response.json()
    else:
        print(f"❌ Gagal menambah test case: {response.text}")
        return None

def add_result_for_case(run_id, case_id, status_id, comment=""):
    """
    run_id: ID dari Test Run
    case_id: ID dari test case
    status_id:
        1 = Passed
        2 = Blocked
        3 = Untested (default)
        4 = Retest
        5 = Failed
    comment: Komentar untuk hasil test

    return: dict JSON response atau None jika gagal
    """
    url = f"{TESTRAIL_URL}index.php?/api/v2/add_result_for_case/{run_id}/{case_id}"
    
    payload = {
        "status_id": status_id,
        "comment": comment
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, auth=auth, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"✅ Hasil untuk case {case_id} berhasil ditambahkan")
        return response.json()
    else:
        print(f"❌ Gagal update TestRail: {response.text}")