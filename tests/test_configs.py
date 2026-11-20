import json
import unittest
import os

class TestMonitoringStack(unittest.TestCase):
    def test_grafana_dashboard_json(self):
        dashboard_path = os.path.join("grafana", "dashboards", "overview.json")
        self.assertTrue(os.path.exists(dashboard_path))
        with open(dashboard_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data.get("uid"), "vexanode-overview")
        self.assertEqual(len(data.get("panels", [])), 3)

    def test_required_files_exist(self):
        files = [
            "docker-compose.yml",
            os.path.join("prometheus", "prometheus.yml"),
            os.path.join("prometheus", "alerts.yml"),
            os.path.join("grafana", "provisioning", "datasources", "datasource.yml"),
            os.path.join("grafana", "provisioning", "dashboards", "dashboard.yml")
        ]
        for file in files:
            self.assertTrue(os.path.exists(file), f"Missing required file: {file}")

if __name__ == "__main__":
    unittest.main()
