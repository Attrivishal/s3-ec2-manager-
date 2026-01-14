#!/usr/bin/env python3
"""
AWS Status Checker - Simple version for Cron Jobs
Author: Vishal Attri
Run this file to check S3 and EC2 status ONLY (no menu)
Perfect for daily automated checks!
"""

import boto3
import os
from datetime import datetime

# ====================== SIMPLE UI ======================
def print_separator():
    print("=" * 70)

def print_section(title):
    print(f"\n📌 {title}")
    print("-" * 50)

# ====================== AWS CONFIG ======================
REGION = 'ap-south-1'

# ====================== S3 CHECK ======================
def check_s3():
    """Check all S3 buckets"""
    print_section("S3 BUCKETS STATUS")
    
    try:
        s3 = boto3.client('s3', region_name=REGION)
        response = s3.list_buckets()
        buckets = response['Buckets']
        
        if buckets:
            print(f"✅ Found {len(buckets)} bucket(s):")
            for bucket in buckets:
                name = bucket['Name']
                created = bucket['CreationDate'].strftime('%Y-%m-%d %H:%M')
                
                # Try to get bucket size
                try:
                    objects = s3.list_objects_v2(Bucket=name)
                    file_count = len(objects.get('Contents', []))
                    print(f"   📁 {name}")
                    print(f"      Created: {created}")
                    print(f"      Files: {file_count}")
                except:
                    print(f"   📁 {name} (Cannot access details)")
                    print(f"      Created: {created}")
        else:
            print("📭 No S3 buckets found")
            
    except Exception as e:
        print(f"❌ Failed to check S3: {str(e)}")

# ====================== EC2 CHECK ======================
def check_ec2():
    """Check all EC2 instances"""
    print_section("EC2 INSTANCES STATUS")
    
    try:
        ec2 = boto3.client('ec2', region_name=REGION)
        response = ec2.describe_instances()
        
        all_instances = []
        for reservation in response['Reservations']:
            all_instances.extend(reservation['Instances'])
        
        if all_instances:
            print(f"✅ Found {len(all_instances)} instance(s):")
            
            running_count = 0
            stopped_count = 0
            
            for instance in all_instances:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                # Get instance name from tags
                name = "No Name"
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                            break
                
                # Count status
                if state == 'running':
                    running_count += 1
                    status = "🟢 RUNNING"
                elif state == 'stopped':
                    stopped_count += 1
                    status = "🔴 STOPPED"
                else:
                    status = f"🟡 {state.upper()}"
                
                print(f"   🖥️  {name}")
                print(f"      ID: {instance_id}")
                print(f"      Status: {status}")
                print(f"      Type: {instance.get('InstanceType', 'Unknown')}")
            
            # Summary
            print(f"\n📊 SUMMARY:")
            print(f"   🟢 Running: {running_count}")
            print(f"   🔴 Stopped: {stopped_count}")
            print(f"   📊 Total: {len(all_instances)}")
            
        else:
            print("🖥️  No EC2 instances found")
            
    except Exception as e:
        print(f"❌ Failed to check EC2: {str(e)}")

# ====================== MAIN FUNCTION ======================
def main():
    """Main function to run all checks"""
    print_separator()
    print(f"AWS STATUS CHECK - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_separator()
    
    # Run all checks
    check_s3()
    check_ec2()
    
    print_separator()
    print("✅ Status check completed!")
    print_separator()

# ====================== RUN THE SCRIPT ======================
if __name__ == "__main__":
    main()
