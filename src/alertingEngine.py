from typing import Dict, List

class AlertingEngine:
    def __init__(self):
        self.alerts_fired = []
        self.rules = []

    def add_rule(self, name, metric, operator, threshold, severity):
        self.rules.append({
            'name': name, 'metric': metric,
            'operator': operator, 'threshold': threshold,
            'severity': severity
        })

    def check_metrics(self, metrics: Dict) -> List[Dict]:
        fired = []
        for rule in self.rules:
            value = metrics.get(rule['metric'])
            if value is None:
                continue

            should_fire = False
            if rule['operator'] == '>':
                should_fire = value > rule['threshold']
            elif rule['operator'] == '<':
                should_fire = value < rule['threshold']
            elif rule['operator'] == '>=':
                should_fire = value >= rule['threshold']

            if should_fire:
                alert = {'rule': rule['name'], 'value': value,
                         'threshold': rule['threshold'], 'severity': rule['severity']}
                fired.append(alert)
                self.alerts_fired.append(alert)

        return fired

def create_default_rules():
    engine = AlertingEngine()

    engine.add_rule('High CPU', 'cpu_percent', '>', 9, 'critical')

    # When free memory is LOW, it means usage is HIGH — logic is inverted
    engine.add_rule('High Memory', 'free_memory_percent', '>', 80, 'warning')

    # After running for hours, total errors always exceed threshold
    engine.add_rule('High Error Rate', 'total_errors', '>', 100, 'critical')

    return engine
