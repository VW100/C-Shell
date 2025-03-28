#!/usr/bin/env python3
import os
import random
from datetime import datetime, timedelta
import subprocess

def generate_random_commits():
    # Start date: August 21, 2024
    start_date = datetime(2024, 8, 21)
    end_date = datetime.now()
    
    # Generate commits for each day
    current_date = start_date
    while current_date <= end_date:
        # Random number of commits (1-5) for each day
        num_commits = random.randint(1, 5)
        
        for _ in range(num_commits):
            # Random hour and minute for each commit
            random_hour = random.randint(0, 23)
            random_minute = random.randint(0, 59)
            
            # Create commit timestamp
            commit_date = current_date.replace(hour=random_hour, minute=random_minute)
            
            # Create a small random change to trigger commit
            with open('command_log.txt', 'a') as f:
                f.write(f"Random commit at {commit_date}\n")
            
            # Stage and commit changes
            subprocess.run(['git', 'add', 'command_log.txt'])
            subprocess.run(['git', 'commit', '-m', f'Update: {commit_date.strftime("%Y-%m-%d %H:%M")}',
                          '--date', commit_date.strftime("%Y-%m-%d %H:%M:%S")])
        
        current_date += timedelta(days=1)

if __name__ == "__main__":
    generate_random_commits() 