# EC2 Instance Monitoring CLI Tool

A Python-based CLI tool to process and monitor EC2 instance data from a JSON file.

## 🚀 Features

- List all instances
- Filter running instances
- Filter stopped instances
- Identify costly instances (t2.large, t2.medium)
- Handle missing data using `.get()`
- Export output to a file

## 🧠 Tech Stack

- Python
- JSON
- CLI (sys.argv)

## 📂 Project Structure

ec2-monitor/
│
├── monitor.py
├── ec2_real.json
├── README.md

## ⚙️ Usage

python monitor.py all  
python monitor.py running  
python monitor.py stopped  
python monitor.py costly  
python monitor.py all output.txt  

## 👨‍💻 Author

Abhishek Sharma