# 🚀 S3-EC2 Manager

A powerful terminal-based tool with beautiful UI for managing AWS S3 buckets and EC2 instances. Features color-coded menus, progress bars, and real-time status updates.

![AWS](https://img.shields.io/badge/AWS-S3%20%26%20EC2-orange)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Terminal UI](https://img.shields.io/badge/UI-Colorful%20Terminal-brightgreen)
![Boto3](https://img.shields.io/badge/SDK-Boto3-yellow)

## ✨ Features

### 🎨 **Beautiful Terminal Interface**
- **Color-coded menus** with ANSI escape sequences
- **Progress bars** for long-running AWS operations  
- **Formatted ASCII boxes** and tables for clean output
- **Real-time status indicators** (🟢 running/🔴 stopped)
- **Success/Error/Warning boxes** with visual feedback

### 📦 **S3 Storage Management**
- **📁 List buckets** with creation dates in formatted tables
- **➕ Create buckets** with region configuration (ap-south-1)
- **🗑️ Delete buckets** with safety confirmation prompts
- **⬆️ Upload files** with progress tracking and size display
- **📄 List files** with size calculations and beautiful formatting

### 🖥️ **EC2 Server Control**
- **📋 List instances** with colored status indicators
- **🚀 Launch instances** with customizable types (t2.micro/small/medium)
- **⏸️ Stop instances** to save costs with progress animation
- **▶️ Start instances** with estimated ready time
- **💀 Terminate instances** with double confirmation warnings

## 🖼️ Screenshots

### Main Interface
╔════════════════════════════════════════════════════════════╗
║ AWS MASTER TOOL v2.0 ║
║ Manage S3 Storage & EC2 Servers ║
╚════════════════════════════════════════════════════════════╝

📍 Region: ap-south-1 (Mumbai)
📅 2024-01-15 14:30:00
💡 Tip: Stop EC2 instances when not in use to save costs
──────────────────────────────────────────────────────────────

📦 S3 STORAGE MANAGEMENT

List all S3 buckets

Create new S3 bucket

Delete S3 bucket

Upload file to S3

List files in bucket

🖥️ EC2 SERVER MANAGEMENT
6. List all EC2 instances
7. Create new EC2 instance
8. Stop EC2 instance
9. Start EC2 instance
10. Delete EC2 instance

🎯 Enter your choice (0-10):

text

### Progress Bar Example
Uploading file.txt...
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]
✅ SUCCESS: Uploaded file.txt to my-bucket

text

## 📁 Project Structure
s3-ec2-manager/
├── aws_master_tool.py # Main application with beautiful UI
├── s3_manager.py # Standalone S3 manager (legacy)
├── ec2_manager.py # Standalone EC2 manager (legacy)
├── aws_tool.sh # Shell script for setup
├── requirements.txt # Python dependencies
├── README.md # This documentation
├── .gitignore # Git ignore rules
└── LICENSE # MIT License

text

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- AWS Account with S3 and EC2 access
- AWS CLI configured with credentials
- IAM permissions (see below)

### Step 1: Clone Repository
```bash
git clone https://github.com/Attrivishal/s3-ec2-manager-.git
cd s3-ec2-manager-
Step 2: Install Dependencies
bash
pip install -r requirements.txt
Step 3: Configure AWS
bash
# Configure AWS CLI
aws configure
# Enter your Access Key, Secret Key, Region (ap-south-1)

# Or set environment variables
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="ap-south-1"
🚀 Usage
Run the Main Tool (Recommended)
bash
python aws_master_tool.py
Run Legacy Tools (Optional)
bash
# Standalone S3 Manager
python s3_manager.py

# Standalone EC2 Manager  
python ec2_manager.py
Quick Examples
1. List All S3 Buckets
text
Choose option 1
Output:
┌────────────────────────────────────────────┐
│  1. my-backup-bucket       2024-01-10     │
│  2. website-assets         2024-01-12     │
└────────────────────────────────────────────┘
2. Create EC2 Instance
text
Choose option 7
Enter instance name: my-web-server
Choose instance type (1-3): 1
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]
✅ SUCCESS: Created instance: my-web-server (i-1234567890)
3. Upload File to S3
text
Choose option 4
Enter bucket name: my-backup-bucket
Enter file to upload: backup.zip
📊 File: backup.zip
📦 Size: 45.23 MB
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]
✅ SUCCESS: Uploaded backup.zip to my-backup-bucket
🔐 AWS IAM Permissions
Your IAM user/role needs these permissions:

json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:ListBucket",
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:RunInstances",
                "ec2:StartInstances",
                "ec2:StopInstances",
                "ec2:TerminateInstances",
                "ec2:CreateTags"
            ],
            "Resource": "*"
        }
    ]
}
🧠 Technical Architecture
Core Components
aws_master_tool.py: Main unified interface with enhanced UI

Colors class: ANSI color management for terminal output

Progress Bars: Dynamic character animation using sys.stdout

Box Drawing: Unicode characters for beautiful table formatting

Key Functions
UI Enhancements
python
def print_success(msg):          # Green success boxes
def print_error(msg):            # Red error boxes  
def print_warning(msg):          # Yellow warning boxes
def show_progress_bar(seconds):  # Animated progress bars
S3 Operations
python
def s3_list_buckets():           # List with formatted tables
def s3_create_bucket():          # Create with validation
def s3_upload_file():            # Upload with progress tracking
EC2 Operations
python
def ec2_list_instances():        # List with colored status
def ec2_create_instance():       # Launch with type selection
def ec2_stop_instance():         # Stop with confirmation
Dependencies
txt
boto3>=1.34.0        # AWS SDK for Python
⚡ Performance Tips
Instance Management: Use t2.micro for development to stay in free tier

Bucket Naming: Follow S3 naming conventions (3-63 characters, lowercase)

Region Selection: Default is ap-south-1 (Mumbai), change in code if needed

Key Pair: Update KeyName='MyWebServer-Key' in ec2_create_instance() function

🚨 Important Notes
⚠️ Security Warning
Never commit AWS credentials to version control

Use .env files or AWS CLI configuration

The .gitignore file excludes sensitive files

🔑 Key Configuration
Update these lines in your code:

python
# In ec2_create_instance() function:
KeyName='MyWebServer-Key'  # Change to your actual key pair name

# In main() function:
region_name='ap-south-1'   # Change to your preferred region
💰 Cost Management
EC2 instances incur hourly charges

S3 storage has monthly costs

Always stop instances when not in use

Monitor costs via AWS Billing Dashboard

🔧 Troubleshooting
Common Issues
1. "No credentials found"
bash
# Solution: Configure AWS CLI
aws configure
2. "Access Denied"
bash
# Solution: Check IAM permissions
# Ensure your user has S3 and EC2 permissions
3. "Bucket name invalid"
text
# Solution: Bucket names must be:
# - 3-63 characters
# - Lowercase letters, numbers, dots, hyphens
# - Start and end with letter/number
4. "Key pair not found"
text
# Solution: Create key pair in AWS Console
# Or update KeyName in ec2_create_instance() function
Debug Mode
Enable debug output by adding:

python
import boto3
boto3.set_stream_logger('')
📈 Roadmap
Planned Features
Cost Calculator: Estimate AWS spending

Auto-stop Scheduler: Schedule EC2 instances to stop automatically

Multi-region Support: Manage resources across different AWS regions

S3 Lifecycle Policies: Automate object expiration

CloudWatch Integration: Monitor instance metrics

Docker Support: Containerized deployment

In Progress
Unified Interface: Combine S3 and EC2 management

Beautiful UI: Color coding and progress bars

Error Handling: User-friendly error messages

Input Validation: Prevent common mistakes

🤝 Contributing
We welcome contributions! Here's how:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

Development Setup
bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install black flake8 pytest
Code Style
Follow PEP 8 guidelines

Use descriptive function names

Add docstrings to all functions

Include type hints where possible

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
AWS for the comprehensive Boto3 SDK

Python Community for excellent terminal tools

Open Source Contributors who make projects like this possible

Vishal Attri for creating and maintaining this tool

📞 Support
Found a bug or need help?

Check Issues

Create a new issue with details

Include error messages and steps to reproduce

Star History
https://api.star-history.com/svg?repos=Attrivishal/s3-ec2-manager-&type=Date

<div align="center">
Made with ❤️ by Vishal Attri

https://img.shields.io/badge/GitHub-Repository-black?logo=github
https://img.shields.io/badge/AWS-Certified-orange?logo=amazonaws
https://img.shields.io/badge/Python-3.8%252B-blue?logo=python

Happy Cloud Computing! ☁️🚀

