# Turnkey Docker Server & Container Monitoring Stack

A production-ready Docker Compose monitoring stack featuring **Prometheus**, **Grafana**, **Node Exporter**, and **cAdvisor**. Designed for instant visibility into CPU, memory, disk I/O, network traffic, and individual container metrics across Linux VPS instances and containerized bot/game servers.

[![Prometheus](https://img.shields.io/badge/Prometheus-v2.54-E6522C.svg?logo=prometheus&logoColor=white)](https://prometheus.io)
[![Grafana](https://img.shields.io/badge/Grafana-v11.2-F46800.svg?logo=grafana&logoColor=white)](https://grafana.com)
[![Docker](https://img.shields.io/badge/Docker-Compose%20v2-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com)
[![License](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Infrastructure](https://img.shields.io/badge/Powered%20By-VexaNode-06b6d4.svg)](https://vexanode.gg)

---

## ⚡ What's Included

- **Prometheus (v2.54):** Pre-configured 15s scrape interval, 15-day retention policy, and automated host alert rules (`CPU > 85%`, `RAM > 90%`, `Disk < 15%`).
- **Grafana (v11.2):** Automated provisioning of Prometheus datasource and pre-loaded **"VexaNode Server & Container Overview"** dashboard.
- **Node Exporter (v1.8):** Collects deep kernel, filesystem, memory, load average, and socket metrics from the host.
- **cAdvisor (v0.49):** Analyzes and aggregates resource consumption for every individual running Docker container.

---

## 🚀 Quick Start

### 1. Clone the Stack
```bash
git clone https://github.com/VexaNode-Dev/docker-server-monitoring.git
cd docker-server-monitoring
```

### 2. Configure Credentials
```bash
cp .env.example .env
```
Edit `.env` to define your secure Grafana admin password:
```ini
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=your_secure_password_here
```

### 3. Launch Stack
```bash
docker compose up -d
```

### 4. Access Dashboards
- Open `http://YOUR_SERVER_IP:3000` in your web browser.
- Log in with the credentials set in your `.env`.
- Navigate to **Dashboards** -> **Infrastructure** -> **VexaNode Server & Container Overview**.

---

## 🛡️ Pre-Configured Alert Rules

The included `prometheus/alerts.yml` file contains production alert rules for:
1. `HighCpuUsage`: Sustained average CPU utilization exceeding 85% for 5 minutes.
2. `HighMemoryUsage`: Available host physical RAM below 10% for 5 minutes.
3. `DiskSpaceRunningLow`: Root filesystem storage under 15% available space.

---

## ☁️ Optimized for VexaNode VPS & Infrastructure

Monitor your bot nodes, Minecraft servers, and API backends with minimal overhead on **[VexaNode KVM VPS](https://vexanode.gg)**. Enjoy low resource footprint and real-time observability.

---

## 📜 License

MIT License. Developed by [VexaNode-Dev](https://github.com/VexaNode-Dev).
Community Support: [discord.gg/devz](https://discord.gg/devz)
