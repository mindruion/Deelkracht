from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django_auth_ldap.backend import LDAPBackend


class Command(BaseCommand):
    help = 'seed db'

    def handle(self, *args, **options):
        call_command('loaddata', 'main/fixtures/settings.json')
        call_command('loaddata', 'main/fixtures/groups.json')
        call_command('loaddata', 'main/fixtures/users.json')
        call_command('loaddata', 'faqs/fixtures/faqs.json')
        call_command('loaddata', 'observations/fixtures/registrations.json')
        call_command('loaddata', 'proposals/fixtures/fundings.json')
        call_command('loaddata', 'proposals/fixtures/institutions.json')
        call_command('loaddata', 'proposals/fixtures/relations.json')
        call_command('loaddata', 'studies/fixtures/agegroups.json')
        call_command('loaddata', 'studies/fixtures/compensations.json')
        call_command('loaddata', 'studies/fixtures/recruitments.json')
        call_command('loaddata', 'studies/fixtures/traits.json')
        call_command('loaddata', 'tasks/fixtures/registrations.json')
        call_command('loaddata', 'tasks/fixtures/registrationkinds.json')

