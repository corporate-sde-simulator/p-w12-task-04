"""Metrics collector helper. Clean file."""
class MetricsSnapshot:
    def __init__(self, cpu=50, memory_used=60, errors_per_min=0):
        self.data = {
            'cpu_percent': cpu,
            'used_memory_percent': memory_used,
            'free_memory_percent': 100 - memory_used,
            'errors_per_minute': errors_per_min,
            'total_errors': errors_per_min * 60,
        }
