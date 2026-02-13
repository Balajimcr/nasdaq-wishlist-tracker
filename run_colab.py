#!/usr/bin/env python3
"""
NASDAQ Wishlist Tracker - Google Colab Launcher
Run this script directly in Google Colab after cloning the repo
"""

import os
import sys

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    os.system('pip install -q -r requirements.txt')
    print("✅ Dependencies installed!")

def setup_ngrok():
    """Setup ngrok authentication"""
    from pyngrok import ngrok

    # Check for environment variable first
    token = os.environ.get('NGROK_AUTH_TOKEN', '')

    if not token:
        print("\n⚠️  NGROK_AUTH_TOKEN not found!")
        print("\nOptions:")
        print("1. Set environment variable: NGROK_AUTH_TOKEN")
        print("2. Or enter token now")
        print("\nGet your token from: https://dashboard.ngrok.com/get-started/your-authtoken")
        token = input("\nEnter your ngrok token (or press Enter to skip): ").strip()

    if token:
        ngrok.set_auth_token(token)
        print("✅ ngrok configured!")
        return True
    else:
        print("❌ ngrok token required to expose app publicly")
        return False

def start_app():
    """Launch Flask app with ngrok tunnel"""
    from app import app
    from pyngrok import ngrok
    import threading

    print("\n🚀 Starting NASDAQ Wishlist Tracker...")

    # Start ngrok tunnel
    try:
        public_url = ngrok.connect(5000)
        print(f"\n{'='*60}")
        print(f"🌐 PUBLIC URL: {public_url}")
        print(f"{'='*60}")
        print("\n✅ App is running! Open the link above in your browser")
        print("\n💡 Tip: Bookmark this URL to access from any device")
        print("⏹️  Press Ctrl+C to stop the server\n")
    except Exception as e:
        print(f"\n❌ Error starting ngrok: {e}")
        print("\nApp will run locally only on http://localhost:5000")

    # Run Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)

def main():
    """Main execution flow"""
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║        📈 NASDAQ WISHLIST TRACKER                       ║
    ║        Google Colab Edition                             ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    # Step 1: Install dependencies
    install_dependencies()

    # Step 2: Setup ngrok
    if not setup_ngrok():
        print("\n⚠️  Continuing without ngrok (local access only)...")

    # Step 3: Start the app
    start_app()

if __name__ == '__main__':
    main()
