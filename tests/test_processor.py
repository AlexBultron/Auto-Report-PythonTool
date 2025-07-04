from app.data.processor import generate_report

def test_generate_report():
    report = generate_report()
    assert "average_value" in report
    assert len(report["data"]) == 5
