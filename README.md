# Enterprise Transaction Monitor & Analytics

This project is a distributed microservices ecosystem designed to handle, process, and visualize high-frequency financial transactions. It demonstrates cross-language communication (Go & Python), persistent data storage, and advanced cloud monitoring.

[Magyar Leírás](#magyar) | [English Version](#english)

---

<a name="magyar"></a>
## 🇭🇺 Projekt Célok és Követelmények

### Célkitűzés
Egy elosztott mikroservice ökoszisztéma felépítése, amely képes nagy mennyiségű pénzügyi tranzakció fogadására, feldolgozására és vizualizációjára. A projekt célja a többnyelvű (Go és Python) architektúra, a felhős adatbázis-kezelés és a professzionális monitorozás bemutatása.

### Technológiai Stack
* **Szolgáltatások:** Go (Ingress API), Python FastAPI (Feldolgozó motor).
* **Adattárolás:** PostgreSQL (AWS RDS).
* **Infrastruktúra:** Terraform (IaC).
* **Monitorozás:** Prometheus & Grafana.
* **Telepítés:** AWS App Runner vagy EKS.

### Funkcionális Követelmények
1.  **Tranzakció fogadás:** Publikus végpont JSON alapú tranzakciós adatok fogadására.
2.  **Validáció és Feldolgozás:** Üzleti logika megvalósítása (pl. pénznem ellenőrzés, alapvető csalásmegelőzési szűrők).
3.  **Adatperzisztencia:** Validált tranzakciók mentése relációs adatbázisba megfelelő indexeléssel.
4.  **Analitikai Dashboard:** Élő statisztikák (forgalom, sikeres/sikertelen)

---

<a name="english"></a>
## 🇺🇸 Project Goals & Requirements

### Objective
Build a scalable system that ingests transaction data via a Go frontend, processes it through a Python backend, stores it in a managed PostgreSQL database, and provides real-time observability.

### Tech Stack
* **Services:** Go (Ingress API), Python FastAPI (Processing Engine).
* **Storage:** PostgreSQL (AWS RDS).
* **Infrastructure:** Terraform (IaC).
* **Monitoring:** Prometheus & Grafana.
* **Deployment:** AWS App Runner / EKS (Elastic Kubernetes Service).

### Functional Requirements
1.  **Transaction Ingestion:** A public endpoint to receive JSON transaction data.
2.  **Validation & Processing:** Backend logic to validate business rules (e.g., currency checks, fraud detection patterns).
3.  **Data Persistence:** Store validated transactions in a relational database with proper indexing.
4.  **Analytics Dashboard:** Live visualization of transaction volume, success rates, and total turnover.