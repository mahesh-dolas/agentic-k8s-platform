class IncidentMemory:


    def __init__(self):

        self.incidents = []


    def remember(self, incident):

        self.incidents.append(
            incident
        )


    def search(self, keyword):

        matches = []

        for incident in self.incidents:

            if keyword.lower() in incident["issue"].lower():

                matches.append(
                    incident
                )


        return matches


    def list_incidents(self):

        return self.incidents