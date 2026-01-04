"""
S3 Manager - Standalone S3 Management Tool
Author: [Your Name]
Description: Simple tool to manage AWS S3 buckets and files
"""

import boto3
import os

def show_menu():
    """Display the S3 menu"""
    print("\n" + "="*40)
    print("        S3 STORAGE MANAGER")
    print("="*40)
    print("1. List all buckets")
    print("2. Create new bucket")
    print("3. Delete bucket")
    print("4. Upload file")
    print("5. List files in bucket")
    print("6. Exit")
    print("-"*40)

def list_buckets(s3_client):
    """List all S3 buckets"""
    try:
        response = s3_client.list_buckets()
        buckets = response['Buckets']
        
        if buckets:
            print(f"\nYou have {len(buckets)} S3 bucket(s):")
            for bucket in buckets:
                print(f"  • {bucket['Name']}")
        else:
            print("\nNo S3 buckets found")
            
    except Exception as e:
        print(f"Error: {e}")

def create_bucket(s3_client):
    """Create a new S3 bucket"""
    name = input("\nBucket name: ").strip().lower()
    
    if len(name) < 3 or len(name) > 63:
        print("Bucket name must be 3-63 characters")
        return
    
    try:
        s3_client.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
        )
        print(f"Created bucket: {name}")
        
    except Exception as e:
        print(f"Error: {e}")

def delete_bucket(s3_client):
    """Delete an S3 bucket"""
    name = input("\nBucket to delete: ").strip()
    
    try:
        s3_client.delete_bucket(Bucket=name)
        print(f"Deleted bucket: {name}")
    except Exception as e:
        print(f"Error: {e}")

def upload_file(s3_client):
    """Upload file to S3"""
    bucket = input("\nBucket name: ").strip()
    filename = input("File to upload: ").strip()
    
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    try:
        s3_client.upload_file(filename, bucket, filename)
        print(f"Uploaded {filename} to {bucket}")
    except Exception as e:
        print(f"Error: {e}")

def list_files(s3_client):
    """List files in a bucket"""
    bucket = input("\nBucket name: ").strip()
    
    try:
        files = s3_client.list_objects_v2(Bucket=bucket)
        
        if 'Contents' in files:
            print(f"\nFiles in {bucket}:")
            for item in files['Contents']:
                print(f"  • {item['Key']}")
        else:
            print(f"\nNo files in {bucket}")
            
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main program"""
    print("\nAWS S3 Manager")
    print("Region: ap-south-1 (Mumbai)")
    print("-"*40)
    
    # Connect to S3
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    while True:
        show_menu()
        
        try:
            choice = input("\nChoose 1-6: ").strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        
        if choice == '1':
            list_buckets(s3)
        elif choice == '2':
            create_bucket(s3)
        elif choice == '3':
            delete_bucket(s3)
        elif choice == '4':
            upload_file(s3)
        elif choice == '5':
            list_files(s3)
        elif choice == '6':
            print("\nGoodbye!")
            break
        else:
            print("Please choose 1-6")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()