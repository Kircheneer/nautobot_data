from nautobot.extras.jobs import *
from nautobot.tenancy.models import Tenant


class NewTenant(Job):
    class Meta:
        name = "New tenant"
        description = "Create a tenant"
        field_order = ['tenant']

    tenant = StringVar(
        description="Name of the new tenant"
    )

    def run(self, data, commit):
        # Create the new site
        tenant = Tenant(
            name=data['tenant']
        )
        if commit:
            tenant.validated_save()
        self.log_success(f"Successfully created tenant {tenant}.")

        return tenant
