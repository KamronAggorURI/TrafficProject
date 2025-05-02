
# Rhode Island Traffic Data Collection and Visualization

### This project collects live traffic incident data from the MapQuest Traffic API and visualizes it on a Streamlit web app using Folium. It includes an automated EC2-based data collection pipeline that saves `.csv` datasets for later analysis or manual download.
---

## Project Structure
```
/code
  |-> app.py                     # Streamlit app - I integrated Folium to display the traffic maps
  |-> ri_map_fetcher.py          # My helper class for geocoding purposes as well as fetching traffic incident data from https://www.mapquestapi.com/traffic/v2/incidents
/scripts
  |-> traffic_data_collection.py # Python script run on AWS EC2 instance, cron scheduler for fetch component
README.md                        # Description and instructions
requirements.txt                 # Dependencies for Streamlit app
```
---

## Overview

1. **Data Collection**
    - `traffic_data_collection.py` runs on an AWS EC2 instance that fetches every 15 minutes using a cron scheduler.
    - Calls the MapQuest Traffic API using an **API_KEY** -> RI Incidents.
    - Script component then appends this data to `traffic_incidents.csv` on the EC2 instance, completing this flow.

2. **Visualization**
    - The Streamlit app (`app.py`) will visualize traffic incidents using the collected `.csv` - not entirely necessary but it does look pretty cool.

3. **Manual Download**
    - Although you could create an automatic downloading flow, I have opted to download the .csv manually using the terminal.

---

## Requirements

- Python 3.12 (My current version)
- MapQuest Developer API Key ('`YOUR_API_KEY`' in scripts)
- AWS EC2 instance (Amazon Linux) with:
    - `python3`, `pip3`
    - Your `.pem` SSH key for secure access
    - Please take care if this is your first time using AWS, as it will prompt you for payment information. Although for this implementation it shouldn't incur any costs.

---

## Key Bash Commands

### SSH -> EC2 Instance
```bash
ssh -i ~/path/to/key_one.pem ec2-user@<EC2_PUBLIC_IP>
```

### Copy Python script to EC2
```bash
scp -i ~/path/to/key_one.pem ~/local/path/traffic_data_collection.py ec2-user@<EC2_PUBLIC_IP>:/home/ec2-user/
```

### Check Python installation on EC2
```bash
python3 --version
pip3 --version
```

### Install required Python libraries on EC2
```bash
pip3 install requests pandas
```

### Set up cron schedule on EC2
```bash
crontab -e
```

Add this line to run the script every 15 minutes:
```bash
*/15 * * * * /usr/bin/python3 /home/ec2-user/traffic_data_collection.py >> /home/ec2-user/traffic_log.txt 2>&1
```

### Download `.csv` from EC2 to PC
```bash
scp -i ~/path/to/key_one.pem ec2-user@<EC2_PUBLIC_IP>:/home/ec2-user/traffic_incidents.csv ~/Downloads/
```
---

## Notes

- **API Key Setup**  
  Replace `YOUR_API_KEY` in the Python scripts with your actual MapQuest API key.

- **Security**  
  Keep your `.pem` file secure! Do not foolishly share or commit it anywhere like I probably accidentally did somewhere.

- **Logs**  
  `/home/ec2-user/traffic_log.txt` on EC2 helps a lot for debugging cron.

---

## Future Plans

- Automate `.csv` uploads for cloud access
- Expand the Streamlit app

---

## License

This project is for educational and research purposes. Please respect API usage limits and terms of service.
