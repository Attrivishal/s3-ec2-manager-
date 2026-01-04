#!/bin/bash

# Clear screen
clear

# Show beautiful header
echo -e "\033[1;36m"
figlet "AWS Automator"
echo -e "\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo ""

# Main menu
show_menu() {
    echo -e "\033[1;32m"
    echo "╔════════════════════════════════════════╗"
    echo "║        AWS AUTOMATION TOOL             ║"
    echo "╠════════════════════════════════════════╣"
    echo "║ \033[1;33m1\033[0m\033[1;32m) Start EC2 Instance               ║"
    echo "║ \033[1;33m2\033[0m\033[1;32m) Stop EC2 Instance                ║"
    echo "║ \033[1;33m3\033[0m\033[1;32m) List S3 Buckets                  ║"
    echo "║ \033[1;33m4\033[0m\033[1;32m) Create Lambda Function           ║"
    echo "║ \033[1;33m5\033[0m\033[1;32m) Check CloudWatch Logs            ║"
    echo "║ \033{1;33m6\033[0m\033[1;32m) Exit                              ║"
    echo "╚════════════════════════════════════════╝"
    echo -e "\033[0m"
    echo -n "Select option [1-6]: "
}

# Function to show progress
show_progress() {
    echo -ne "\033[1;36m["
    for i in {1..20}; do
        echo -ne "▇"
        sleep 0.05
    done
    echo -e "]\033[0m"
}

# Function for success message
success_msg() {
    echo -e "\n\033[42m\033[1;37m ✓ SUCCESS: $1 \033[0m\n"
}

# Function for error message
error_msg() {
    echo -e "\n\033[41m\033[1;37m ✗ ERROR: $1 \033[0m\n"
}

# Function to start EC2 (example)
start_ec2() {
    echo -e "\n\033[1;35m🚀 Starting EC2 Instance...\033[0m"
    show_progress
    
    # Your actual AWS CLI command here
    # aws ec2 start-instances --instance-ids i-1234567890abcdef0
    
    success_msg "EC2 instance started successfully!"
}

# Function to list S3 buckets
list_s3() {
    echo -e "\n\033[1;35m📦 Listing S3 Buckets...\033[0m"
    show_progress
    
    # Your actual AWS CLI command here
    # aws s3 ls
    
    # Simulate output
    echo -e "\033[1;37m┌─────────────────────────────────────┐"
    echo -e "│         S3 BUCKETS LIST            │"
    echo -e "├─────────────────────────────────────┤"
    echo -e "│ \033[32mmy-website-bucket\033[0m                  │"
    echo -e "│ \033[32mbackup-2024\033[0m                       │"
    echo -e "│ \033[32mlogs-archive\033[0m                      │"
    echo -e "└─────────────────────────────────────┘\033[0m"
}

# Main program loop
while true; do
    show_menu
    read choice
    
    case $choice in
        1)
            start_ec2
            ;;
        2)
            echo -e "\n\033[1;35m🛑 Stopping EC2 Instance...\033[0m"
            show_progress
            success_msg "EC2 instance stopped successfully!"
            ;;
        3)
            list_s3
            ;;
        4)
            echo -e "\n\033[1;35mλ Creating Lambda Function...\033[0m"
            show_progress
            success_msg "Lambda function created!"
            ;;
        5)
            echo -e "\n\033[1;35m📊 Checking CloudWatch Logs...\033[0m"
            show_progress
            echo -e "\033[1;37mNo errors found in logs.\033[0m"
            ;;
        6)
            echo -e "\n\033[1;35m👋 Goodbye! Thanks for using AWS Automator.\033[0m"
            exit 0
            ;;
        *)
            error_msg "Invalid option! Please choose 1-6"
            ;;
    esac
    
    # Wait for user to press enter
    echo -ne "\n\033[1;33mPress Enter to continue...\033[0m"
    read -r
    clear
done