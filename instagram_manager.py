"""
Instagram Manager - Educational Automation Tool
⚠️ FOR EDUCATIONAL PURPOSES ONLY
Use responsibly and follow Instagram Terms of Service
"""

import os
import time
import random
import threading
import logging
import json
from datetime import datetime
import getpass
from instagrapi import Client
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class InstagramManager:
    def __init__(self):
        self.client = Client()
        self.running = True
        self.session_file = 'session.json'
        
    def educational_warning(self):
        """Show educational disclaimer"""
        print(Fore.YELLOW + "="*60)
        print(Fore.RED + "⚠️  EDUCATIONAL TOOL - USE RESPONSIBLY")
        print(Fore.YELLOW + "="*60)
        print(Fore.CYAN + "This tool is for learning:")
        print("• Python Automation")
        print("• API Integration") 
        print("• Error Handling")
        print("• Threading Concepts")
        print(Fore.YELLOW + "="*60)
        
        confirm = input(Fore.WHITE + "Type 'LEARN' to continue: ")
        return confirm.upper() == 'LEARN'

    def smart_login(self, username, password):
        """Educational login demonstration"""
        try:
            print(Fore.CYAN + f"🔐 Learning: API Authentication...")
            
            # Educational delay
            time.sleep(2)
            
            self.client.login(username, password)
            print(Fore.GREEN + "✅ Authentication Successful")
            return True
            
        except Exception as e:
            print(Fore.RED + f"❌ Learning: Error Handling - {e}")
            return False

    def send_educational_message(self, thread_id, message):
        """Send message with educational logging"""
        try:
            print(Fore.BLUE + f"📚 Learning: Message API Call...")
            
            result = self.client.direct_send(message, thread_ids=[thread_id])
            
            print(Fore.GREEN + f"✅ Message Sent: {message[:50]}...")
            logging.info(f"Educational message sent: {message[:50]}")
            return True
            
        except Exception as e:
            print(Fore.RED + f"❌ Learning: API Error - {e}")
            return False

    def scheduled_messaging_demo(self, username, password, thread_id, messages):
        """Educational messaging demonstration"""
        if not self.educational_warning():
            return

        if not self.smart_login(username, password):
            return

        print(Fore.GREEN + "\n🎓 Starting Educational Demo...")
        print(Fore.CYAN + "Demonstrating:")
        print("• API Rate Limiting")
        print("• Error Handling") 
        print("• Thread Safety")
        print("• Logging Systems\n")

        message_count = 0
        max_demo_messages = 5  # Educational limit
        
        for i, message in enumerate(messages[:max_demo_messages]):
            if not self.running:
                break
                
            success = self.send_educational_message(thread_id, message)
            if success:
                message_count += 1
                
            # Educational delay between API calls
            delay = random.uniform(5, 10)
            print(Fore.YELLOW + f"⏰ Learning: Rate Limiting ({delay:.1f}s)")
            time.sleep(delay)

        print(Fore.GREEN + f"\n✅ Educational Demo Complete!")
        print(Fore.CYAN + f"📊 Messages Sent: {message_count}")
        print(Fore.YELLOW + "🎯 Concepts Learned: API Integration, Error Handling, Rate Limiting")

def main():
    """Main educational demonstration"""
    manager = InstagramManager()
    
    print(Fore.CYAN + "🤖 Instagram API Educational Tool")
    print(Fore.YELLOW + "📚 Python Automation Learning Platform\n")
    
    # Get demo inputs
    username = input("Enter Instagram Username: ").strip()
    password = getpass.getpass("Enter Password: ")
    thread_id = input("Enter Thread ID (for demo): ").strip()
    
    # Educational messages
    messages = [
        "Hello! This is an educational demo message.",
        "Learning Python automation concepts.",
        "Understanding API rate limiting.",
        "Exploring error handling in Python.",
        "Studying threading and async operations."
    ]
    
    # Start educational demo
    manager.scheduled_messaging_demo(username, password, thread_id, messages)

if __name__ == "__main__":
    main()