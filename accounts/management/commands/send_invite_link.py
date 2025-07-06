import uuid
from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send registration invite to email'
    
    def add_arguments(self, parser):
        parser.add_argument('email', nargs='+', type=str)
        
    def handle(self, *args, **options):
        for email in options['email']:
            token = str(uuid.uuid4())
            cache.set(email, token, timeout=3600) # 1 hour
            
            registration_url = f"frontend url"
            
            send_mail(
                subject="You're invited to synoloops task app",
                message=f"Here's the link to register: {registration_url}, and your token {token}",
                from_email= None,
                recipient_list=[email],
                fail_silently= False,
            )
            self.stdout.write(self.style.SUCCESS(f"Invite sent to {email}"))