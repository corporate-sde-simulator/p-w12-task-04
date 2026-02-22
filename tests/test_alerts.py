import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from alertingEngine import create_default_rules

class TestAlertingRules:
    def test_normal_cpu_no_alert(self):
        engine = create_default_rules()
        alerts = engine.check_metrics({'cpu_percent': 50})
        cpu_alerts = [a for a in alerts if a['rule'] == 'High CPU']
        assert len(cpu_alerts) == 0, "50% CPU should not trigger alert"

    def test_high_cpu_alerts(self):
        engine = create_default_rules()
        alerts = engine.check_metrics({'cpu_percent': 95})
        cpu_alerts = [a for a in alerts if a['rule'] == 'High CPU']
        assert len(cpu_alerts) == 1, "95% CPU should trigger alert"

    def test_high_memory_alerts(self):
        engine = create_default_rules()
        # 90% used = 10% free — should alert
        alerts = engine.check_metrics({'used_memory_percent': 90, 'free_memory_percent': 10})
        mem_alerts = [a for a in alerts if a['rule'] == 'High Memory']
        assert len(mem_alerts) == 1, "90% memory used should trigger alert"

    def test_error_rate_not_total(self):
        engine = create_default_rules()
        alerts = engine.check_metrics({'errors_per_minute': 5, 'total_errors': 500})
        err_alerts = [a for a in alerts if a['rule'] == 'High Error Rate']
        assert len(err_alerts) == 0, "5 errors/min should not trigger (total is misleading)"
