

# SMART HOME AUTOMATED CONTROL AND MONITORING SYSTEM  

---
sdadadasd docs file
---

## Project Setup  
### Steps to Run the Project  
1. **Clone the Repository**  
   ```sh  
   git clone https://github.com/Twiggiermaen21/IOT_SHACAM.git
   ```  
2. **Build and Start Services Using Docker**  
   ```sh  
   docker compose build  
   docker compose up  
   ```  
3. **Access the Services**  
   - **Grafana Dashboard**: [http://localhost:3000/dashboards](http://localhost:3000/dashboards)  
     - Username: `admin`, Password: `admin`  
   - **Node-RED UI**: [http://localhost:1880](http://localhost:1880)  
   - **InfluxDB Database**: [http://localhost:8086](http://localhost:8086)  
     - Username: `admin`, Password: `password`  
 

4. **Shutdown Services**  
   ```sh  
   docker compose down  
   ```  

---

## Technologies Used  
- **IoT Sensors**: Utilize Python scripts to simulate smart home sensor behavior and data generation.  
- **MQTT Protocol**: Enables seamless communication between devices.  
- **Docker & Docker Compose**: Simplifies deployment and scalability.  
- **Grafana**: Provides real-time data visualization.  
- **InfluxDB**: Stores time-series data for analysis.  
- **Node-RED**: Manages automation workflows.  



---

**Contributors**  
- **David Urban** - david.urban@student.univaq.it  
- **Kacper Pudelko** - kacperhenryk.pudelko@student.univaq.it  

---



