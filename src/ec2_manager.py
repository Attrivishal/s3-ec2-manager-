"""
EC2 Manager - Standalone EC2 Management Tool
Author: [Your Name]
Description: Simple tool to manage AWS EC2 instances
"""

import boto3

def show_menu():
    """Display the EC2 menu"""
    print("\n" + "="*40)
    print("        EC2 SERVER MANAGER")
    print("="*40)
    print("1. List all instances")
    print("2. Create new instance")
    print("3. Stop instance")
    print("4. Start instance")
    print("5. Delete instance")
    print("6. Exit")
    print("-"*40)

def list_instances(ec2_client):
    """List all EC2 instances"""
    try:
        response = ec2_client.describe_instances()
        
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)
        
        if instances:
            print(f"\nYou have {len(instances)} EC2 instance(s):")
            for instance in instances:
                # Get instance name
                name = 'No Name'
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                            break
                
                print(f"  • {name} ({instance['InstanceId']}) - {instance['State']['Name']}")
        else:
            print("\nNo EC2 instances found")
            
    except Exception as e:
        print(f"Error: {e}")

def create_instance(ec2_client):
    """Create a new EC2 instance"""
    name = input("\nInstance name: ").strip()
    
    try:
        response = ec2_client.run_instances(
            ImageId='ami-0f5ee92e2d63afc18',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='boto3-key',  # ⚠️ CHANGE TO YOUR KEY NAME
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': name}]
            }]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Created instance: {name} ({instance_id})")
        print("Wait 2 minutes for it to start")
        
    except Exception as e:
        print(f"Error: {e}")

def stop_instance(ec2_client):
    """Stop an EC2 instance"""
    instance_id = input("\nInstance ID to stop: ").strip()
    
    try:
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping {instance_id}...")
    except Exception as e:
        print(f"Error: {e}")

def start_instance(ec2_client):
    """Start an EC2 instance"""
    instance_id = input("\nInstance ID to start: ").strip()
    
    try:
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Starting {instance_id}...")
    except Exception as e:
        print(f"Error: {e}")

def delete_instance(ec2_client):
    """Delete an EC2 instance"""
    instance_id = input("\nInstance ID to delete: ").strip()
    
    confirm = input(f"Type 'delete' to delete {instance_id}: ")
    
    if confirm == 'delete':
        try:
            ec2_client.terminate_instances(InstanceIds=[instance_id])
            print(f"Deleting {instance_id}...")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Cancelled")

def main():
    """Main program"""
    print("\nAWS EC2 Manager")
    print("Region: ap-south-1 (Mumbai)")
    print("-"*40)
    
    # Connect to EC2
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    while True:
        show_menu()
        
        try:
            choice = input("\nChoose 1-6: ").strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        
        if choice == '1':
            list_instances(ec2)
        elif choice == '2':
            create_instance(ec2)
        elif choice == '3':
            stop_instance(ec2)
        elif choice == '4':
            start_instance(ec2)
        elif choice == '5':
            delete_instance(ec2)
        elif choice == '6':
            print("\nGoodbye!")
            break
        else:
            print("Please choose 1-6")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()