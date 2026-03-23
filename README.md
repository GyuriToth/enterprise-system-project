<p align="center">
<pre>
  ██████╗ ██╗   ██╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗    ████████╗ ██████╗ ████████╗██╗  ██╗
 ██╔════╝ ╚██╗ ██╔╝██╔═══██╗██╔══██╗██╔════╝ ╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗╚══██╔══╝██║  ██║
 ██║  ███╗ ╚████╔╝ ██║   ██║██████╔╝██║  ███╗ ╚████╔╝        ██║   ██║   ██║   ██║   ███████║
 ██║   ██║  ╚██╔╝  ██║   ██║██╔══██╗██║   ██║  ╚██╔╝         ██║   ██║   ██║   ██║   ██║  ██║
 ╚██████╔╝   ██║   ╚██████╔╝██║  ██║╚██████╔╝   ██║          ██║   ╚██████╔╝   ██║   ██║  ██║
  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝          ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝
</pre>
</p>

# Enterprise Transaction Monitor & Analytics

Ez a projekt egy elosztott mikroservice ökoszisztéma, amit arra terveztem, hogy nagy sebességű pénzügyi tranzakciókat fogadjon, dolgozzon fel és vizualizáljon. A rendszer egy hibrid-felhő architektúrát használ: a szolgáltatások lokálisan (Docker), míg az adatbázis éles felhő környezetben (AWS RDS) fut.

[Magyar Leírás](#magyar) | [English Version](#english)

---

<a name="magyar"></a>
## 🇭🇺 Projekt Áttekintés

### Architektúra és Működés
A projekt a modern szoftverfejlesztés több rétegét kapcsolja össze:
1.  **Ingress (Go):** Egy gyors frontend/API réteg, amely fogadja a tranzakciókat.
2.  **Logic (Python FastAPI):** A feldolgozó motor, amely üzleti logikát és **csalásfigyelést** végez (minden 4000 egység feletti tranzakciót automatikusan `flagged` státusszal jelöl meg).
3.  **Infrastructure as Code (Terraform):** Az AWS RDS (PostgreSQL) példányt nem kézzel kattintgattam össze, hanem kódból (IaC) hoztam létre, biztosítva az újrafelhasználhatóságot.
4.  **Observability (Prometheus & Grafana):** Teljes rálátás a rendszer egészségére (TPS, hibaarány, csalási kísérletek).

### Technológiai Stack
* **Backend:** Python (FastAPI, SQLAlchemy, Psycopg2)
* **Frontend:** Go (Standard library, HTML templates)
* **Adattárolás:** PostgreSQL (Menedzselt AWS RDS példány)
* **Infrastruktúra:** Terraform, Docker
* **Monitorozás:** Prometheus (Metrics scraping), Grafana (Custom Dashboard)

### Telepítés és Futtatás
1.  **Infrastruktúra:**
    ```bash
    cd terraform
    terraform init
    terraform apply
    ```
2.  **Konfiguráció:** Frissítsd a `docker-compose.yml` fájlban a `DATABASE_URL`-t a Terraform által kiadott `db_endpoint` címmel.
3.  **Indítás:**
    ```bash
    docker compose up --build -d
    ```
4.  **Elérés:** * Frontend: `http://localhost:8081`
    * Grafana: `http://localhost:3000` (admin/admin)

---

<a name="english"></a>
## 🇺🇸 Project Overview

### Architecture
This system demonstrates a real-world hybrid-cloud microservices pattern:
* **Go Ingress:** Handles incoming transaction data with high efficiency.
* **Python Processing:** A FastAPI service responsible for business logic and **automated fraud detection** (flagging any transaction over 4000).
* **Cloud Persistence:** Uses **AWS RDS (PostgreSQL)** for reliable, managed data storage, provisioned via **Terraform**.
* **Real-time Observability:** A full monitoring stack using **Prometheus** to scrape application metrics and **Grafana** for visualization.

### Tech Stack
* **Services:** Go, Python (FastAPI).
* **Infrastructure:** Terraform (IaC), Docker.
* **Database:** Managed PostgreSQL on AWS.
* **Monitoring:** Prometheus, Grafana.

### Key Technical Challenges Solved
* **Cross-Language Communication:** Orchestrating Go and Python services within a shared Docker network.
* **Infrastructure Automation:** Moving away from local DBs to managed cloud instances using Terraform.
* **Observability:** Implementing custom Prometheus counters to track financial metrics and fraud patterns in real-time.

### Quick Start
1.  Provision the AWS RDS instance using `terraform apply`.
2.  Update the `DATABASE_URL` in `docker-compose.yml`.
3.  Run `docker compose up --build -d` to spin up the local ecosystem.
4.  Head over to `localhost:8081` to send your first transaction and watch it appear on the Grafana dashboard (`localhost:3000`).

---

### Cleanup
To avoid AWS costs when not in use:
```bash
cd terraform
terraform destroy
