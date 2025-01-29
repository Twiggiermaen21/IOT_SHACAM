# SE4IoT - SOFTWARE ENGINEERING FOR INTERNET OF THINGS  

## SMART HOME AUTOMATED CONTROL AND MONITORING SYSTEM  


### SUBMITTED BY:  
**David Urban**  
david.urban@student.univaq.it  
**Kacper Pudelko**  
kacperhenryk.pudelko@student.univaq.it  
---
sdadadasd docs file
---

## Project Setup  
### Steps to Run the Project  
1. **Clone the Repository**  
   ```sh  
   git clone https://github.com/Twiggiermaen21/Smart-Home-Automated-Control-And-Monitoring-System-IoT.git  
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

4. **Simulate Additional Sensors in Wokwi**  
   - Modify `MQTT_CLIENT_ID` in Wokwi simulation (e.g., change value to `'wokwi_sensor2'`).  
   - Restart the Wokwi simulation to observe different sensor inputs.  

5. **Shutdown Services**  
   ```sh  
   docker compose down  
   ```  

---

## Technologies Used  
- **IoT Sensors**: Monitor home environment for automation.  
- **MQTT Protocol**: Enables seamless communication between devices.  
- **Docker & Docker Compose**: Simplifies deployment and scalability.  
- **Grafana**: Provides real-time data visualization.  
- **InfluxDB**: Stores time-series data for analysis.  
- **Node-RED**: Manages automation workflows.  

---

## Future Enhancements  
- **AI-based Automation**: Improve system intelligence with machine learning.  
- **Mobile App Integration**: Extend control and notifications to mobile devices.  
- **Voice Control Support**: Enable smart assistant compatibility.  

For more details, refer to the project report available in the `./report` directory.  

---

**Contributors**  
- **David Urban** - david.urban@student.univaq.it  
- **Kacper Pudelko** - kacperhenryk.pudelko@student.univaq.it  

---

© 2025 Smart Home Automated Control and Monitoring System. All rights reserved.

