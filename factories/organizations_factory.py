
from models.organization import Organization


class OrganizationFactory:
    def __init__(self,world,network):
        self.world = world
        self.network = network
        
       
    def create_organizations(self,organization_deatils):
        self.check_location(organization_deatils)
        organizations = []
        org_id = 0
        for organizations_location,details in organization_deatils.items():
            for i in range(details['how_many']):
                org_id +=1
                org_name = f'org{org_id}'
                new = Organization(self.world,
                                    self.network,
                                    org_name,
                                    organizations_location,
                                    details['peers'],
                                    details['ordering_service']
                                    )
                organizations.append(new)
        return organizations
        
    def check_location(self,organizations):
        organizations_location = list(organizations.keys())
        for location in organizations_location:
            if location not in self.world.locations:
                raise RuntimeError(f'There are not measurements for the location {location}. Only available locations: {self._world.locations}')