"""
AWS Master Tool - Manage S3 Storage & EC2 Servers
Author: [Your Name]
Description: Single tool to manage both S3 and EC2 services with beautiful UI
"""

import boto3
import os
import sys
import time
from datetime import datetime

# ====================== UI ENHANCEMENTS ======================

class Colors:
    """ANSI color codes for terminal"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Display beautiful header"""
    clear_screen()
    print(Colors.CYAN + Colors.BOLD)
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                  " + Colors.YELLOW + "AWS MASTER TOOL v2.0" + Colors.CYAN + "                    ║")
    print("║            Manage S3 Storage & EC2 Servers                 ║")
    print("╚════════════════════════════════════════════════════════════╝" + Colors.END)
    print(f"\n📍 {Colors.YELLOW}Region: ap-south-1 (Mumbai){Colors.END}")
    print(f"📅 {Colors.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
    print(f"💡 {Colors.GREEN}Tip: Stop EC2 instances when not in use to save costs{Colors.END}")
    print(Colors.CYAN + "─" * 62 + Colors.END)

def show_progress_bar(seconds=2, message="Processing"):
    """Show animated progress bar"""
    print(f"\n{Colors.BLUE}{message}...{Colors.END}")
    sys.stdout.write("[")
    for i in range(20):
        time.sleep(seconds / 20)
        sys.stdout.write("▓")
        sys.stdout.flush()
    sys.stdout.write("]\n")

def print_success(msg):
    """Print success message in green box"""
    print(f"\n{Colors.GREEN}╔════════════════════════════════════════════════════════════╗")
    print(f"║                    ✅ SUCCESS                         ║")
    print(f"║    {msg:<52}   ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Colors.END}")

def print_error(msg):
    """Print error message in red box"""
    print(f"\n{Colors.RED}╔════════════════════════════════════════════════════════════╗")
    print(f"║                    ❌ ERROR                           ║")
    print(f"║    {msg:<52}   ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Colors.END}")

def print_warning(msg):
    """Print warning message in yellow box"""
    print(f"\n{Colors.YELLOW}╔════════════════════════════════════════════════════════════╗")
    print(f"║                    ⚠️  WARNING                         ║")
    print(f"║    {msg:<52}   ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Colors.END}")

def print_menu_box():
    """Display menu in a beautiful box"""
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}┌────────────────────────────────────────────────────────────┐")
    print(f"│                    MAIN MENU                         │")
    print(f"├────────────────────────────────────────────────────────────┤{Colors.END}")
    
    print(f"{Colors.CYAN}│  {Colors.BOLD}📦 S3 STORAGE MANAGEMENT{Colors.END}{Colors.CYAN}                              │")
    print(f"│   {Colors.GREEN}1.{Colors.END} List all S3 buckets                              │")
    print(f"│   {Colors.GREEN}2.{Colors.END} Create new S3 bucket                             │")
    print(f"│   {Colors.GREEN}3.{Colors.END} Delete S3 bucket                                 │")
    print(f"│   {Colors.GREEN}4.{Colors.END} Upload file to S3                                │")
    print(f"│   {Colors.GREEN}5.{Colors.END} List files in bucket                             │")
    
    print(f"│                                                        │")
    print(f"│  {Colors.BOLD}🖥️  EC2 SERVER MANAGEMENT{Colors.END}{Colors.CYAN}                               │")
    print(f"│   {Colors.GREEN}6.{Colors.END} List all EC2 instances                           │")
    print(f"│   {Colors.GREEN}7.{Colors.END} Create new EC2 instance                          │")
    print(f"│   {Colors.GREEN}8.{Colors.END} Stop EC2 instance                                │")
    print(f"│   {Colors.GREEN}9.{Colors.END} Start EC2 instance                               │")
    print(f"│   {Colors.GREEN}10.{Colors.END} Delete EC2 instance                            │")
    print(f"│                                                        │")
    print(f"│   {Colors.RED}0.{Colors.END} Exit program                                      │")
    print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")

# ====================== ENHANCED AWS FUNCTIONS ======================

def s3_list_buckets():
    """List all S3 buckets with beautiful display"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}📁 LISTING S3 BUCKETS{Colors.END}")
    print(f"{Colors.CYAN}────────────────────────────────────────────{Colors.END}")
    
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    try:
        response = s3.list_buckets()
        buckets = response['Buckets']
        
        if buckets:
            print(f"\n{Colors.GREEN}✅ Found {len(buckets)} S3 bucket(s):{Colors.END}")
            print(f"{Colors.WHITE}┌────────────────────────────────────────────┐")
            
            for i, bucket in enumerate(buckets, 1):
                creation_date = bucket['CreationDate'].strftime('%Y-%m-%d')
                name = bucket['Name']
                print(f"│ {Colors.YELLOW}{i:2}.{Colors.END} {name:<30} {Colors.CYAN}{creation_date}{Colors.END} │")
            
            print(f"└────────────────────────────────────────────┘{Colors.END}")
        else:
            print(f"\n{Colors.YELLOW}📭 No S3 buckets found{Colors.END}")
            
    except Exception as e:
        print_error(f"Failed to list buckets: {str(e)}")

def s3_create_bucket():
    """Create a new S3 bucket with interactive UI"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}➕ CREATE NEW S3 BUCKET{Colors.END}")
    print(f"{Colors.CYAN}────────────────────────────────────────────{Colors.END}")
    
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    name = input(f"\n{Colors.YELLOW}📝 Enter bucket name: {Colors.END}").strip().lower()
    
    if len(name) < 3 or len(name) > 63:
        print_error("Bucket name must be 3-63 characters")
        return
    
    show_progress_bar(2, "Creating bucket")
    
    try:
        s3.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
        )
        print_success(f"Created bucket: {Colors.BOLD}{name}{Colors.GREEN}")
        print(f"{Colors.GREEN}🔗 URL: https://{name}.s3.ap-south-1.amazonaws.com{Colors.END}")
        
    except Exception as e:
        print_error(f"Failed to create bucket: {str(e)}")

def s3_delete_bucket():
    """Delete an S3 bucket with confirmation"""
    print(f"\n{Colors.RED}{Colors.BOLD}🗑️  DELETE S3 BUCKET{Colors.END}")
    print(f"{Colors.RED}────────────────────────────────────────────{Colors.END}")
    
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    name = input(f"\n{Colors.YELLOW}⚠️  Enter bucket name to delete: {Colors.END}").strip()
    
    # Confirm deletion
    print_warning(f"This will PERMANENTLY delete bucket: {name}")
    confirm = input(f"{Colors.RED}Type 'DELETE' to confirm: {Colors.END}").strip()
    
    if confirm == 'DELETE':
        show_progress_bar(3, f"Deleting bucket {name}")
        
        try:
            # First, empty the bucket
            try:
                objects = s3.list_objects_v2(Bucket=name)
                if 'Contents' in objects:
                    for obj in objects['Contents']:
                        s3.delete_object(Bucket=name, Key=obj['Key'])
            except:
                pass
            
            # Then delete bucket
            s3.delete_bucket(Bucket=name)
            print_success(f"Deleted bucket: {Colors.BOLD}{name}{Colors.GREEN}")
            
        except Exception as e:
            print_error(f"Failed to delete bucket: {str(e)}")
    else:
        print(f"\n{Colors.GREEN}✅ Deletion cancelled{Colors.END}")

def s3_upload_file():
    """Upload a file to S3 with progress"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}⬆️  UPLOAD FILE TO S3{Colors.END}")
    print(f"{Colors.CYAN}────────────────────────────────────────────{Colors.END}")
    
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    bucket = input(f"\n{Colors.YELLOW}📦 Enter bucket name: {Colors.END}").strip()
    filename = input(f"{Colors.YELLOW}📄 Enter file to upload: {Colors.END}").strip()
    
    if not os.path.exists(filename):
        print_error(f"File not found: {filename}")
        return
    
    file_size = os.path.getsize(filename)
    size_mb = file_size / (1024 * 1024)
    
    print(f"\n{Colors.BLUE}📊 File: {filename}")
    print(f"📦 Size: {size_mb:.2f} MB{Colors.END}")
    
    show_progress_bar(3, f"Uploading {filename}")
    
    try:
        s3.upload_file(filename, bucket, os.path.basename(filename))
        print_success(f"Uploaded {Colors.BOLD}{filename}{Colors.GREEN} to {Colors.BOLD}{bucket}{Colors.GREEN}")
        
    except Exception as e:
        print_error(f"Upload failed: {str(e)}")

def s3_list_files():
    """List files in an S3 bucket with details"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}📄 LIST FILES IN BUCKET{Colors.END}")
    print(f"{Colors.CYAN}────────────────────────────────────────────{Colors.END}")
    
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    bucket = input(f"\n{Colors.YELLOW}📦 Enter bucket name: {Colors.END}").strip()
    
    show_progress_bar(1, f"Scanning {bucket}")
    
    try:
        files = s3.list_objects_v2(Bucket=bucket)
        
        if 'Contents' in files:
            print(f"\n{Colors.GREEN}📁 Files in {Colors.BOLD}{bucket}{Colors.GREEN}:{Colors.END}")
            print(f"{Colors.WHITE}┌────┬────────────────────────────┬─────────────────┐")
            print(f"│ No │          File Name           │     Size       │")
            print(f"├────┼────────────────────────────┼─────────────────┤")
            
            total_size = 0
            for i, item in enumerate(files['Contents'], 1):
                size = int(item['Size'])
                total_size += size
                size_str = f"{size/1024:.1f} KB" if size < 1024*1024 else f"{size/(1024*1024):.2f} MB"
                
                # Truncate long filenames
                filename = item['Key']
                if len(filename) > 25:
                    filename = filename[:22] + "..."
                
                print(f"│ {i:2} │ {filename:<25} │ {size_str:<15} │")
            
            print(f"├────┼────────────────────────────┼─────────────────┤")
            total_str = f"{total_size/(1024*1024):.2f} MB" if total_size > 0 else "0 B"
            print(f"│    │ {Colors.YELLOW}Total:{Colors.END} {len(files['Contents']):2} files   │ {Colors.YELLOW}{total_str:<15}{Colors.END} │")
            print(f"└────┴────────────────────────────┴─────────────────┘{Colors.END}")
        else:
            print(f"\n{Colors.YELLOW}📭 No files found in {bucket}{Colors.END}")
            
    except Exception as e:
        print_error(f"Failed to list files: {str(e)}")

def ec2_list_instances():
    """List all EC2 instances with status colors"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}🖥️  LIST EC2 INSTANCES{Colors.END}")
    print(f"{Colors.CYAN}────────────────────────────────────────────{Colors.END}")
    
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    try:
        response = ec2.describe_instances()
        instances = []
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)
        
        if instances:
            print(f"\n{Colors.GREEN}✅ Found {len(instances)} EC2 instance(s):{Colors.END}")
            print(f"{Colors.WHITE}┌────┬────────────────────┬──────────────────────┬──────────┐")
            print(f"│ No │      Name          │      Instance ID     │  Status  │")
            print(f"├────┼────────────────────┼──────────────────────┼──────────┤")
            
            for i, instance in enumerate(instances, 1):
                # Get instance name from tags
                name = "No Name"
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                            break
                
                state = instance['State']['Name']
                instance_id = instance['InstanceId'][:19]
                
                # Color code status
                if state == 'running':
                    status_color = Colors.GREEN + "▶ Running" + Colors.END
                elif state == 'stopped':
                    status_color = Colors.RED + "⏹ Stopped" + Colors.END
                elif state == 'pending':
                    status_color = Colors.YELLOW + "⏳ Pending" + Colors.END
                else:
                    status_color = state
                
                # Truncate long names
                if len(name) > 18:
                    name = name[:15] + "..."
                
                print(f"│ {i:2} │ {name:<18} │ {instance_id:<20} │ {status_color:<8} │")
            
            print(f"└────┴────────────────────┴──────────────────────┴──────────┘{Colors.END}")
            
            # Show summary
            running = sum(1 for i in instances if i['State']['Name'] == 'running')
            stopped = sum(1 for i in instances if i['State']['Name'] == 'stopped')
            print(f"\n{Colors.CYAN}📊 Summary: {Colors.GREEN}{running} running{Colors.END} | {Colors.RED}{stopped} stopped{Colors.END} | {len(instances)} total{Colors.END}")
            
        else:
            print(f"\n{Colors.YELLOW}🖥️  No EC2 instances found{Colors.END}")
            
    except Exception as e:
        print_error(f"Failed to list instances: {str(e)}")

def ec2_create_instance():
    """Create a new EC2 instance with options"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}➕ CREATE NEW EC2 INSTANCE{Colors.END}")
    print(f"{Colors.CYAN}────────────────────────────────────────────{Colors.END}")
    
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    name = input(f"\n{Colors.YELLOW}📝 Enter instance name: {Colors.END}").strip()
    
    print(f"\n{Colors.BLUE}Select instance type:{Colors.END}")
    print(f"  {Colors.GREEN}1.{Colors.END} t2.micro (Free tier, 1 vCPU, 1GB RAM)")
    print(f"  {Colors.GREEN}2.{Colors.END} t2.small (1 vCPU, 2GB RAM)")
    print(f"  {Colors.GREEN}3.{Colors.END} t2.medium (2 vCPU, 4GB RAM)")
    
    choice = input(f"\n{Colors.YELLOW}Choose (1-3, default 1): {Colors.END}").strip()
    
    instance_types = ['t2.micro', 't2.small', 't2.medium']
    instance_type = instance_types[0]  # default
    
    if choice == '2':
        instance_type = 't2.small'
    elif choice == '3':
        instance_type = 't2.medium'
    
    print(f"\n{Colors.BLUE}Selected: {Colors.YELLOW}{instance_type}{Colors.END}")
    
    show_progress_bar(3, f"Launching {name}")
    
    try:
        response = ec2.run_instances(
            ImageId='ami-0f5ee92e2d63afc18',      # Amazon Linux 2 in Mumbai
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            KeyName='MyWebServer-Key',            # ⚠️ CHANGE TO YOUR KEY NAME
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': name}]
            }]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
        print_success(f"Created instance: {Colors.BOLD}{name}{Colors.GREEN} ({instance_id})")
        print(f"{Colors.GREEN}⏳ Instance is starting... (takes 2-3 minutes){Colors.END}")
        print(f"{Colors.CYAN}💡 Check status with option 6 (List instances){Colors.END}")
        
    except Exception as e:
        print_error(f"Failed to create instance: {str(e)}")

def ec2_stop_instance():
    """Stop an EC2 instance"""
    print(f"\n{Colors.YELLOW}{Colors.BOLD}🛑 STOP EC2 INSTANCE{Colors.END}")
    print(f"{Colors.YELLOW}────────────────────────────────────────────{Colors.END}")
    
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    instance_id = input(f"\n{Colors.YELLOW}⚠️  Enter instance ID to stop: {Colors.END}").strip()
    
    show_progress_bar(2, f"Stopping {instance_id}")
    
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print_success(f"Stopping {Colors.BOLD}{instance_id}{Colors.GREEN}")
        print(f"{Colors.YELLOW}⏳ Takes about 1 minute to stop completely{Colors.END}")
        
    except Exception as e:
        print_error(f"Failed to stop instance: {str(e)}")

def ec2_start_instance():
    """Start an EC2 instance"""
    print(f"\n{Colors.GREEN}{Colors.BOLD}▶️  START EC2 INSTANCE{Colors.END}")
    print(f"{Colors.GREEN}────────────────────────────────────────────{Colors.END}")
    
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    instance_id = input(f"\n{Colors.YELLOW}🎬 Enter instance ID to start: {Colors.END}").strip()
    
    show_progress_bar(2, f"Starting {instance_id}")
    
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print_success(f"Starting {Colors.BOLD}{instance_id}{Colors.GREEN}")
        print(f"{Colors.GREEN}⏳ Takes 1-2 minutes to be ready{Colors.END}")
        
    except Exception as e:
        print_error(f"Failed to start instance: {str(e)}")

def ec2_delete_instance():
    """Delete an EC2 instance permanently"""
    print(f"\n{Colors.RED}{Colors.BOLD}🗑️  DELETE EC2 INSTANCE{Colors.END}")
    print(f"{Colors.RED}────────────────────────────────────────────{Colors.END}")
    
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    instance_id = input(f"\n{Colors.YELLOW}⚠️  Enter instance ID to delete: {Colors.END}").strip()
    
    print_warning(f"This will PERMANENTLY DELETE instance: {instance_id}")
    print_warning("All data will be lost!")
    
    confirm = input(f"\n{Colors.RED}Type 'DELETE' to confirm: {Colors.END}").strip()
    
    if confirm == 'DELETE':
        show_progress_bar(4, f"Terminating {instance_id}")
        
        try:
            ec2.terminate_instances(InstanceIds=[instance_id])
            print_success(f"Deleting {Colors.BOLD}{instance_id}{Colors.GREEN}")
            print(f"{Colors.RED}⏳ Takes 2-3 minutes to remove completely{Colors.END}")
            
        except Exception as e:
            print_error(f"Failed to delete instance: {str(e)}")
    else:
        print(f"\n{Colors.GREEN}✅ Deletion cancelled{Colors.END}")

def main():
    """Main program loop"""
    print_header()
    
    while True:
        print_menu_box()
        
        try:
            choice = input(f"\n{Colors.MAGENTA}🎯 Enter your choice (0-10): {Colors.END}").strip()
        except KeyboardInterrupt:
            print(f"\n\n{Colors.CYAN}👋 Goodbye! Thanks for using AWS Master Tool.{Colors.END}")
            break
        
        # Exit
        if choice == '0':
            print(f"\n{Colors.CYAN}{Colors.BOLD}")
            print("╔════════════════════════════════════════════════════════════╗")
            print("║                    👋 GOODBYE!                           ║")
            print("║         Thanks for using AWS Master Tool                ║")
            print("╚════════════════════════════════════════════════════════════╝")
            print(Colors.END)
            break
        
        # S3 Operations
        elif choice == '1':
            s3_list_buckets()
        elif choice == '2':
            s3_create_bucket()
        elif choice == '3':
            s3_delete_bucket()
        elif choice == '4':
            s3_upload_file()
        elif choice == '5':
            s3_list_files()
        
        # EC2 Operations
        elif choice == '6':
            ec2_list_instances()
        elif choice == '7':
            ec2_create_instance()
        elif choice == '8':
            ec2_stop_instance()
        elif choice == '9':
            ec2_start_instance()
        elif choice == '10':
            ec2_delete_instance()
        
        # Invalid choice
        else:
            print_error("Please enter a number between 0 and 10")
        
        # Pause before showing menu again
        if choice != '0':
            input(f"\n{Colors.CYAN}↵ Press Enter to continue...{Colors.END}")
            print_header()

# Start the program
if __name__ == "__main__":
    main()