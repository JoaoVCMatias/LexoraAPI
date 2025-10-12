# Looking to send emails in production? Check out our Email API/SMTP product!
import requests
from config import MAILTRAP_API_KEY

class MailTrapService:
    @staticmethod
    def teste():
        url = "https://sandbox.api.mailtrap.io/api/send/4096033"

        print(MAILTRAP_API_KEY)

        payload = "{\"from\":{\"email\":\"hello@example.com\",\"name\":\"Mailtrap Test\"},\"to\":[{\"email\":\"lexora.lab@gmail.com\"}],\"subject\":\"You are awesome!\",\"text\":\"Congrats for sending test email with Mailtrap!\",\"category\":\"Integration Test\"}"
        headers = {
          "Authorization": f"Bearer {MAILTRAP_API_KEY}",
          "Content-Type": "application/json"
        }

        print(headers)
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)