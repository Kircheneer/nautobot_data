from nautobot.extras.jobs import *

class Test(Job):
    class Meta:
        name = "Test job"
        description = "Testing jobs"

    tenant = StringVar(
        descriptioN="Name of the tenant"
    )

    def run(self, data, commit):
        tenant = Tenant(name=data['tenant'])
        tenant.validated_save()
        self.log_success(f'Tenant {tenant} created.')
        return tenant
