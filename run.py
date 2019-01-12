import os

from customer_service.app import create

if __name__ == "__main__":
    create().run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
